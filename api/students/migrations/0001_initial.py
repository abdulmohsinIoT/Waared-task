# Generated by Django 4.1.7 on 2023-02-15 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('faculty_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=256)),
                ('date_of_birth', models.DateTimeField()),
            ],
            options={
                'db_table': 'students',
            },
        ),
    ]
