# Generated by Django 3.1 on 2021-08-22 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=100)),
                ('teacher_mobile', models.BigIntegerField()),
                ('teacher_email', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
