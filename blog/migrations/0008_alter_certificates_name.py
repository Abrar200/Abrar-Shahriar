# Generated by Django 5.0 on 2024-01-24 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_certificates_pdf_alter_certificates_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificates',
            name='name',
            field=models.CharField(max_length=1000, unique=True),
        ),
    ]