# Generated by Django 4.1.5 on 2023-01-24 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillName', models.CharField(max_length=50)),
                ('skillLength', models.IntegerField(max_length=10)),
            ],
        ),
    ]
