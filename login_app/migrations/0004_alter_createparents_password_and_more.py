# Generated by Django 4.0.3 on 2022-04-20 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_createstaffs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createparents',
            name='password',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='createparentss',
            name='password',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='createstaffs',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]