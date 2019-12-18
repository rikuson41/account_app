from django.test import TestCase
from django.urls import reverse
# from django.utils import timezone

from account.models import OutGo


class TestIndex(TestCase):
    def test_get(self):
        OutGo.objects.create(category='食費', name="お菓子", price=100)
        OutGo.objects.create(category='日用品', name="ハンガー", price=100)

        res = self.client.get(reverse('index'))
        self.assertTemplateUsed(res, 'account/index.html')
        self.assertContains(res, '食費')
        self.assertContains(res, "お菓子")
        self.assertContains(res, '100円')
        self.assertContains(res, "今月の支出: 200円")
        self.assertEqual(len(res.context['data']), 2)


"""class TestCreate(TestCase):
    def test_post(self):
        res_create = self.client.post(reverse('edit', args=(1,)),
                               data={'category': '食費', 'name': 'テスト',
                                     'price': 200})
        res_index = self.client.get(reverse('index'))
        self.assertTemplateUsed(res_create, 'account/create.html')
        self.assertTemplateUsed(res_index, 'account/index.html')
        self.assertContains(res_index, 'テスト')
        self.assertContains(res_index, 200)
        self.assertContains(res_index, '食費')
"""


"""class TestEdit(TestCase):
    def test_post(self):
        product = OutGo.objects.create(id=1, category='食費', name="お菓子",
                                       price=100)
        res = self.client.post(reverse('edit', args=(1,)),
                                data={'category': 'その他', 'name': '変更',
                                      'price': 200})
        self.assertTemplateUsed(res, 'account/edit.html')
        product.refresh_from_db()
        self.assertEqual(product.name, '変更')
        self.assertEqual(product.price, 200)
        self.assertEqual(product.category, 'その他')
"""
