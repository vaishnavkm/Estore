# Generated by Django 3.1.3 on 2020-12-03 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_new_models'),
    ]

    operations = [
        migrations.CreateModel(
            name='register_id',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=10)),
                ('first_name', models.TextField(max_length=10)),
                ('last_name', models.TextField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('password1', models.CharField(max_length=10)),
                ('password2', models.CharField(max_length=10)),
                ('number', models.IntegerField()),
            ],
        ),
    ]
