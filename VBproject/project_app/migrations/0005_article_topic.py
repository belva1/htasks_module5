# Generated by Django 4.2.3 on 2023-08-03 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0004_remove_article_article_topic_delete_articletopic'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='topic',
            field=models.ManyToManyField(to='project_app.topic'),
        ),
    ]
