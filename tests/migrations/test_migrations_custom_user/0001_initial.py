# encoding: utf8
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [

        migrations.CreateModel(
            "Author",
            [
                ("id", models.AutoField(primary_key=True)),
                ("name", models.CharField(max_length=255)),
            ],
        ),

        migrations.CreateModel(
            "Tribble",
            [
                ("id", models.AutoField(primary_key=True)),
                ("author", models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field="id")),
            ],
        )

    ]
