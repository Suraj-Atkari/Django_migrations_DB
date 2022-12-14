# Generated by Django 4.1.3 on 2022-11-15 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_outlet", "0009_alter_address_options_alter_author_address"),
    ]

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("code", models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name="book",
            name="published_country",
            field=models.ManyToManyField(to="book_outlet.country"),
        ),
    ]
