# Generated by Django 5.0 on 2024-01-21 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_project_image6_project_image7'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]