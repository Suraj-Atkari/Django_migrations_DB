# Generated by Django 4.1.3 on 2022-11-15 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("book_outlet", "0007_alter_book_author"),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("street", models.CharField(max_length=100)),
                ("postal_code", models.CharField(max_length=80)),
                ("city", models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name="author",
            name="address",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="address",
                to="book_outlet.address",
            ),
        ),
    ]
