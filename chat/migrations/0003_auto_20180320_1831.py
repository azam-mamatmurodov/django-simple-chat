# Generated by Django 2.0.3 on 2018-03-20 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20180320_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='member',
        ),
        migrations.RemoveField(
            model_name='chatroom',
            name='owner',
        ),
        migrations.DeleteModel(
            name='ChatRoom',
        ),
    ]