# Generated by Django 2.2.2 on 2019-06-05 18:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'ordering': ['last_name'], 'verbose_name': 'Врачa', 'verbose_name_plural': 'Врачи'},
        ),
        migrations.AlterField(
            model_name='doctor',
            name='end_work_time',
            field=models.TimeField(help_text='Время окончания приема', verbose_name='Конец приема приема'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='first_name',
            field=models.CharField(max_length=128, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='last_name',
            field=models.CharField(max_length=128, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(max_length=64, verbose_name='Специализация'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='start_work_time',
            field=models.TimeField(help_text='Время начала приема', verbose_name='Начало приема'),
        ),
        migrations.AlterField(
            model_name='reception',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Время и дата записи', verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='reception',
            name='pacient_fio',
            field=models.CharField(help_text='ФИО пациента', max_length=128, verbose_name='ФИО'),
        ),
    ]
