# Generated by Django 4.1.7 on 2023-03-13 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_transaction_request_alter_transaction_receiver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='request',
        ),
    ]