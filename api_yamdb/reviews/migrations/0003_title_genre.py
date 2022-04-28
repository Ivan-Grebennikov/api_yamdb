# Generated by Django 2.2.16 on 2022-04-28 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220427_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(through='reviews.GenreTitle', to='reviews.Genre', verbose_name='Жанр'),
        ),
    ]