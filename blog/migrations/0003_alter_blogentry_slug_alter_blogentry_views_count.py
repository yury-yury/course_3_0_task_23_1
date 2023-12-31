# Generated by Django 4.2.3 on 2023-07-29 00:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_blogentry_content_alter_blogentry_preview_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogentry",
            name="slug",
            field=models.CharField(max_length=100, verbose_name="Slug"),
        ),
        migrations.AlterField(
            model_name="blogentry",
            name="views_count",
            field=models.IntegerField(default=0, verbose_name="Просмотры"),
        ),
    ]
