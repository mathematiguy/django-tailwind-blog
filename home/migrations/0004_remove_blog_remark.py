# Generated by Django 4.1.4 on 2023-01-26 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_blog_remark"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="remark",
        ),
    ]
