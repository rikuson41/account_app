from django import forms

from account.models import OutGo


class OutGoForm(forms.ModelForm):

    class Meta:
        model = OutGo
        fields = ('category', 'name', 'price', 'created_at')
        widgets = {
            'created_at': forms.SelectDateWidget(years=[x for x in
                                                 range(2010, 2030)])
        }


class FindForm(forms.Form):
    months = []
    for i in range(1, 13):
        months.append((str(i), str(i)))

    years = []
    for i in range(2010, 2030):
        years.append((str(i), str(i)))

    year = forms.ChoiceField(label='year', required=False, choices=years)
    month = forms.ChoiceField(label='month', required=False, choices=months)
