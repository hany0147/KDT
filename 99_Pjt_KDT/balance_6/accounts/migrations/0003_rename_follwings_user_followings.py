# Generated by Django 3.2.18 on 2023-04-20 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_follwings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='follwings',
            new_name='followings',
        ),
    ]