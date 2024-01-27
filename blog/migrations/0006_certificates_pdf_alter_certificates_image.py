# Generated by Django 5.0 on 2024-01-24 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_certificates'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificates',
            name='pdf',
            field=models.FileField(null=True, upload_to='Images/'),
        ),
        migrations.AlterField(
            model_name='certificates',
            name='image',
            field=models.ImageField(null=True, upload_to='Images/'),
        ),
    ]
