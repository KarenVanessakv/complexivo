# Generated by Django 4.2.1 on 2023-07-19 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="imagen",
            field=models.ImageField(blank=True, null=True, upload_to="blog/"),
        ),
    ]
