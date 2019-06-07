from django.db import models
from django.utils import timezone


class Doctor(models.Model):
    """ Модель доктора """
    first_name = models.CharField(max_length=128, verbose_name='Имя')
    last_name = models.CharField(max_length=128, verbose_name='Фамилия')
    specialization = models.CharField(max_length=64, verbose_name='Специализация')
    start_work_time = models.TimeField(help_text='Время начала приема', verbose_name='Начало приема')
    end_work_time = models.TimeField(help_text='Время окончания приема', verbose_name='Конец приема приема')

    def __str__(self):
        return self.last_name + ' ' + self.first_name

    class Meta:
        verbose_name_plural = 'Врачи'
        verbose_name = 'Врачa'
        ordering = ['last_name']


# class Pacient(models.Model):
#     to_doc = models.ForeignKey(Doctor, on_delete=models.SET_NULL)
#     fio = models.CharField(max_length=64, help_text='ФИО')
#     appointment_date = models.DateTimeField(default=datetime.date.today(), help_text='Время и дата записи')


class Reception(models.Model):
    """ Модель рецепшена """
    to_doc = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='records')
    date = models.DateTimeField(default=timezone.now, help_text='Время и дата записи', verbose_name='Время')
    pacient_fio = models.CharField(max_length=128, help_text='ФИО пациента', verbose_name='ФИО')

    def __str__(self):
        return 'Прием № %s' % self.id

    class Meta:
        ordering = ['date']
        verbose_name_plural = 'Приемы'
        verbose_name = 'Прием'
