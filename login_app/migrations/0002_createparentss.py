# Generated by Django 4.0.3 on 2022-04-11 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='createparentss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='', max_length=20)),
                ('secondname', models.CharField(default='', max_length=15)),
                ('username', models.CharField(default='', max_length=15)),
                ('mail', models.EmailField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=150)),
                ('password', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=20)),
            ],
        ),
    ]
