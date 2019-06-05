from django.contrib import admin
from appointment.models import Doctor, Reception


@admin.register(Doctor)
class AdminDoctor(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'specialization', 'start_work_time', 'end_work_time')
    fields = ['last_name', 'first_name', 'specialization', 'start_work_time', 'end_work_time']


@admin.register(Reception)
class AdminReception(admin.ModelAdmin):
    list_display = ('pacient_fio', 'to_doc', 'date')
    fields = ['pacient_fio', 'to_doc', 'date']
