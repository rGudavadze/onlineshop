# Generated by Django 3.2.9 on 2021-12-26 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created',)},
        ),
    ]