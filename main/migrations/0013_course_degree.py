# Generated by Django 5.0.1 on 2024-10-05 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_studentprofile_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='degree',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]