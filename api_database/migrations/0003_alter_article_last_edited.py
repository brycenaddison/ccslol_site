# Generated by Django 3.2.5 on 2021-08-23 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_database', '0002_alter_article_last_edited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='last_edited',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
