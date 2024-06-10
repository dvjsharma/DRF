# Generated by Django 5.0.6 on 2024-06-09 19:02

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("salary", models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]