# Generated by Django 2.2.6 on 2019-10-20 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('user_email', models.CharField(max_length=200)),
                ('user_contact', models.CharField(max_length=200)),
                ('user_password', models.CharField(max_length=200)),
            ],
        ),
    ]
