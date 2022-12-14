# Generated by Django 4.1.3 on 2022-11-15 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("book_outlet", "0008_address_author_address"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="address",
            options={"verbose_name_plural": "Address Entriess"},
        ),
        migrations.AlterField(
            model_name="author",
            name="address",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="book_outlet.address",
            ),
        ),
    ]
