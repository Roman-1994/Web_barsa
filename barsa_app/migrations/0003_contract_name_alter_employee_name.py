# Generated by Django 4.0.5 on 2022-06-16 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barsa_app', '0002_cities_coach_contract_footballers_posts_teams_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='name',
            field=models.CharField(default='1', max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=50, verbose_name='ФИО сотрудника'),
        ),
    ]
