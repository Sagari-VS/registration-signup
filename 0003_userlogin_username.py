# Generated by Django 2.2.4 on 2019-08-09 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0002_userlogin_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlogin',
            name='username',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
