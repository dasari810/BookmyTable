# Generated by Django 3.1.2 on 2020-11-23 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_restaurant_menu_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_methods', models.TextField(default=False)),
                ('cuisine', models.TextField(default=False)),
                ('features', models.TextField(default=False)),
                ('landmark', models.TextField(default=False)),
                ('website', models.TextField(default=False)),
                ('best_selling_items', models.TextField(default=False)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.restaurant')),
            ],
        ),
    ]