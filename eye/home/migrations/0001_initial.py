# Generated by Django 4.0.5 on 2023-04-18 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name100', models.CharField(max_length=40)),
                ('phonenumbe100', models.CharField(max_length=10)),
                ('email100', models.CharField(max_length=40)),
                ('feedback100', models.TextField()),
            ],
        ),
    ]