# Generated by Django 2.0.2 on 2018-09-15 21:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('weight', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weight',
            options={'ordering': ['user', '-date']},
        ),
        migrations.RenameField(
            model_name='weight',
            old_name='bodyfat',
            new_name='body_fat',
        ),
        migrations.AlterField(
            model_name='weight',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]