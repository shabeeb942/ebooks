# Generated by Django 4.1.7 on 2023-05-20 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_products_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='author',
        ),
    ]
