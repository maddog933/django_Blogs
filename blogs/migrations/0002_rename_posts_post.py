# Generated by Django 4.1.7 on 2023-02-16 06:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blogs", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Posts",
            new_name="Post",
        ),
    ]
