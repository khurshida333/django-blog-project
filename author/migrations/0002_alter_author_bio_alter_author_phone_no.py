# Generated by Django 5.0.6 on 2024-06-23 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='author',
            name='phone_no',
            field=models.CharField(max_length=11),
        ),
    ]
