# Generated by Django 4.2.3 on 2023-08-22 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0012_alter_article_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['title']},
        ),
    ]
