# Generated by Django 4.0.5 on 2022-06-30 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Уровень',
                'verbose_name_plural': 'Уровни',
            },
        ),
    ]
