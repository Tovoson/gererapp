# Generated by Django 5.1.7 on 2025-04-01 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailsappart',
            name='loyer',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='detailsappart',
            name='numapp',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
