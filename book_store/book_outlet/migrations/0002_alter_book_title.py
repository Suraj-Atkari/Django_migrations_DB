# Generated by Django 4.1.3 on 2022-11-11 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_outlet", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="title",
            field=models.CharField(max_length=55),
        ),
    ]
