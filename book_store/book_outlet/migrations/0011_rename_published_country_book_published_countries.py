# Generated by Django 4.1.3 on 2022-11-15 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("book_outlet", "0010_country_book_published_country"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="published_country",
            new_name="published_countries",
        ),
    ]
