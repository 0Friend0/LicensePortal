# Generated by Django 4.1.1 on 2022-09-26 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licenses', '0008_alter_license_client'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='license',
            options={'ordering': ['client']},
        ),
    ]