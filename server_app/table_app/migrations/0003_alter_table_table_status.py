# Generated by Django 4.2.1 on 2023-05-30 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table_app', '0002_alter_table_table_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='table_status',
            field=models.CharField(choices=[('Vacant', 'Vacant'), ('Occupied', 'Occupied')], max_length=10),
        ),
    ]
