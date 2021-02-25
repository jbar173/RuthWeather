# Generated by Django 3.1.6 on 2021-02-24 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ruth_weather', '0002_auto_20210224_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, null=True)),
                ('temp', models.IntegerField(null=True)),
                ('prec', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='eve',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ruth_weather.eve'),
        ),
    ]