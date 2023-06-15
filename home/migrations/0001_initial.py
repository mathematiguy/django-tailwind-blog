# Generated by Django 4.1.4 on 2023-01-22 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                ("sno", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=200)),
                ("meta", models.CharField(max_length=300)),
                ("content", models.TextField()),
                (
                    "thumbnail_img",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                ("slug", models.CharField(max_length=100)),
                ("time", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
