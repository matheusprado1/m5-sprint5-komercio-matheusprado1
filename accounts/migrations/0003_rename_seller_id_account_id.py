# Generated by Django 4.1 on 2022-08-24 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_rename_id_account_seller_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="account",
            old_name="seller_id",
            new_name="id",
        ),
    ]
