from django import forms
from appointment.models import Reception, Doctor
from django.db import models


class ReceptionForm(forms.Form):
    all_doc_query = Doctor.objects.all().values('id', 'last_name', 'first_name')

    doc_select = []
    for item in all_doc_query:
        doc_select.append((item['id'], item['last_name'] + ' ' + item['first_name']))

    to_doc = forms.ChoiceField(
        choices=doc_select,
        label='Выберите доктора',
        required=True
    )
    date = forms.DateTimeField(
        widget=forms.SelectDateWidget(),
        label='Выберите дату приема'
    )
    time = forms.IntegerField(
        min_value=8,
        max_value=18,
        label='Выберите час приема'
    )
    fio = forms.CharField(label='ФИО', required=True)
