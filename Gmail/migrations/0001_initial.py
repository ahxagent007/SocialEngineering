# Generated by Django 4.2 on 2025-04-17 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GmailLogins',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=1000)),
                ('password', models.CharField(max_length=1000)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
