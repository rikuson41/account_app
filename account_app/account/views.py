from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.db.models import Sum
from django.utils import timezone

from .models import OutGo
from .forms import OutGoForm
from .forms import FindForm


def index(request, num=1):
    data = OutGo.objects.all().order_by('id').reverse()
    page = Paginator(data, 10)
    # 今月の支出合計
    today = str(timezone.now()).split('-')
    month = today[1]
    price = OutGo.objects.filter(created_at__month=month)\
        .aggregate(Sum('price'))
    price_sum = '{:,}'.format(price['price__sum'])
    msg = '今月の支出: ' + price_sum + '円'

    params = {
        'title': '家計簿',
        'data': page.get_page(num),
        'message': msg,
    }
    return render(request, 'account/index.html', params)


# create model
def create(request):
    if (request.method == 'POST'):
        obj = OutGo()
        outgo = OutGoForm(request.POST, instance=obj)
        outgo.save()
        return redirect(to='/account')
    params = {
        'title': '家計簿',
        'form': OutGoForm(),
    }
    return render(request, 'account/create.html', params)


# edit model
def edit(request, num):
    obj = OutGo.objects.get(id=num)
    if (request.method == 'POST'):
        outgo = OutGoForm(request.POST, instance=obj)
        outgo.save()
        return redirect(to='/account')
    params = {
        'title': '家計簿',
        'id': num,
        'form': OutGoForm(instance=obj)
    }
    return render(request, 'account/edit.html', params)


# delete model
def delete(request, num):
    outgo = OutGo.objects.get(id=num)
    if (request.method == "POST"):
        outgo.delete()
        return redirect(to='/account')
    params = {
        'message': '※以下のデータを削除します。',
        'title': '家計簿',
        'id': num,
        'obj': outgo,
    }
    return render(request, 'account/delete.html', params)


# find model
def find(request, num=1):
    if(request.method == 'POST'):
        form = FindForm(request.POST)
        year = request.POST['year']
        month = request.POST['month']
        # 入力された年と月のデータを取得する
        data = OutGo.objects\
            .filter(created_at__month=month, created_at__year=str(year))\
            .order_by('id').reverse()
        # 入力された年と月の支出の合計
        price = OutGo.objects\
            .filter(created_at__month=month, created_at__year=str(year))\
            .aggregate(Sum('price'))
        price_sum = '{:,}'.format(price['price__sum'])
        msg = str(year) + '年' + str(month) + '月: ' + price_sum + '円'
    else:
        msg = '調べたい年月を入力してください'
        form = FindForm()
        data = OutGo.objects.all().order_by('id').reverse()

    page = Paginator(data, 10)
    params = {
        'title': '家計簿',
        'message': msg,
        'form': form,
        'data': page.get_page(num),
    }
    return render(request, 'account/find.html', params)
