# Generated by Django 2.2.2 on 2019-07-06 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p2papp', '0012_remove_project_funds_collected'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]