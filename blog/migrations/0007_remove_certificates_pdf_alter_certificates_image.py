# Generated by Django 5.0 on 2024-01-24 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_certificates_pdf_alter_certificates_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificates',
            name='pdf',
        ),
        migrations.AlterField(
            model_name='certificates',
            name='image',
            field=models.ImageField(upload_to='Images/'),
        ),
    ]
