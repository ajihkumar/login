# Generated by Django 4.0.3 on 2022-05-04 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0011_alter_studentextra_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentextra',
            name='parentname',
            field=models.CharField(default=-1.0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('in_active', 'In_Active'), ('waitlist', 'Waitlist'), ('prospects', 'Prospects'), ('toured', 'Toured'), ('applied', 'Applied')], max_length=10),
        ),
        migrations.AlterField(
            model_name='studentextra',
            name='Age',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='studentextra',
            name='mobile',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
