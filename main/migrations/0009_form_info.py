# Generated by Django 5.2.1 on 2025-07-06 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_presencerecord_delete_form_data_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='form_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_type', models.CharField()),
            ],
        ),
    ]
