# Generated by Django 4.2.1 on 2023-06-01 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table_app', '0009_alter_table_table_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='table',
            options={'verbose_name': 'Dining Table', 'verbose_name_plural': 'Dining Tables'},
        ),
    ]
