# Generated by Django 3.2.3 on 2021-05-23 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
