# Generated by Django 5.0.4 on 2024-04-14 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportsalesapp', '0002_alter_realizationreport_create_dt_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realizationreport',
            old_name='realizationreport_id',
            new_name='number',
        ),
    ]