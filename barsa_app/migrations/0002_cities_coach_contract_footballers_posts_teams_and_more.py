# Generated by Django 4.0.5 on 2022-06-15 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barsa_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('distance', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=11)),
                ('age', models.IntegerField()),
                ('date_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms_contract', models.CharField(max_length=100)),
                ('date_sign', models.DateField()),
                ('end_date', models.DateField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Footballers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=11)),
                ('age', models.IntegerField()),
                ('date_birth', models.DateField()),
                ('contract', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='barsa_app.contract')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('duties', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('coach', models.ManyToManyField(to='barsa_app.coach')),
                ('footballer', models.ManyToManyField(to='barsa_app.footballers')),
            ],
        ),
        migrations.CreateModel(
            name='Stadiums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('capacity', models.PositiveIntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='barsa_app.cities')),
            ],
        ),
        migrations.CreateModel(
            name='GameCalendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='barsa_app.cities')),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='barsa_app.coach')),
                ('footballer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='barsa_app.footballers')),
                ('stadium', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='barsa_app.stadiums')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='barsa_app.teams')),
            ],
        ),
        migrations.AddField(
            model_name='coach',
            name='contract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='barsa_app.contract'),
        ),
        migrations.AddField(
            model_name='employee',
            name='contract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='barsa_app.contract'),
        ),
        migrations.AddField(
            model_name='employee',
            name='post',
            field=models.ManyToManyField(to='barsa_app.posts'),
        ),
    ]