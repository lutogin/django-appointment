# Generated by Django 2.2.2 on 2019-06-07 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_auto_20190607_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reception',
            name='to_doc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='appointment.Doctor'),
        ),
    ]
