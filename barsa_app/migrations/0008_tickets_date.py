# Generated by Django 4.0.5 on 2022-06-27 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barsa_app', '0007_alter_tickets_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
