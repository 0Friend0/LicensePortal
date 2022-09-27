# Generated by Django 4.1.1 on 2022-09-24 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('licenses', '0004_alter_client_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='license_own',
        ),
        migrations.AddField(
            model_name='license',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='licenses.client'),
        ),
    ]