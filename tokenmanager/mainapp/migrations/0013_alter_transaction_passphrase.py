# Generated by Django 4.1.7 on 2023-03-13 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_alter_transaction_asset_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='passphrase',
            field=models.CharField(default='', max_length=200),
        ),
    ]
