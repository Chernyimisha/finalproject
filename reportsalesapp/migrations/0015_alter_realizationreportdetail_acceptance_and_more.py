# Generated by Django 5.0.4 on 2024-04-15 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportsalesapp', '0014_alter_realizationreportdetail_order_dt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realizationreportdetail',
            name='acceptance',
            field=models.IntegerField(blank=True, help_text='Стоимость платной приёмки', verbose_name='Платная приемка'),
        ),
        migrations.AlterField(
            model_name='realizationreportdetail',
            name='deduction',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Прочие удержания/выплаты', max_digits=10, verbose_name='Удержания'),
        ),
        migrations.AlterField(
            model_name='realizationreportdetail',
            name='storage_fee',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Стоимость хранения', max_digits=10, verbose_name='Хранение'),
        ),
    ]
