# Generated by Django 3.2.16 on 2022-11-15 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_rename_user_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='release_date',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(model_name='movies', name="imdb_id", field=models.CharField(max_length=20, null=True)),
    ]   
