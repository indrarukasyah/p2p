# Generated by Django 2.2.2 on 2019-06-30 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p2papp', '0010_auto_20190630_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredprojects',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='p2papp.Project'),
        ),
    ]
