# Generated by Django 5.1.4 on 2025-01-21 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_rename_choice_id_answers_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.question'),
        ),
    ]
