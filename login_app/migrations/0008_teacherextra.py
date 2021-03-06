# Generated by Django 4.0.3 on 2022-04-26 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login_app', '0007_alter_customuser_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joindate', models.DateField(auto_now_add=True)),
                ('mobile', models.CharField(max_length=40)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
