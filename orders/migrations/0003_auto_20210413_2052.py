# Generated by Django 3.0.6 on 2021-04-13 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210412_1954'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',), 'verbose_name': 'order', 'verbose_name_plural': 'orders'},
        ),
    ]