# Generated by Django 3.2 on 2021-06-20 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.album'),
        ),
    ]
