# Generated by Django 2.2.2 on 2019-06-30 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p2papp', '0008_featuredprojects'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='projects'),
        ),
    ]