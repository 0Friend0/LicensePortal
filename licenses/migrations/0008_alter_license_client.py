# Generated by Django 4.1.1 on 2022-09-24 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('licenses', '0007_rename_client_name_license_client_alter_client_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='client',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='licenses.client'),
            preserve_default=False,
        ),
    ]
