# Generated by Django 3.2.9 on 2022-01-01 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_review_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-created',)},
        ),
    ]
