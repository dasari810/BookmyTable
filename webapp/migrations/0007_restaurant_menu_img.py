# Generated by Django 3.1.2 on 2020-11-21 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_reservation_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='menu_img',
            field=models.FileField(default=False, upload_to=''),
        ),
    ]
