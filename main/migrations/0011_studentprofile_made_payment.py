# Generated by Django 5.0.1 on 2024-10-05 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_studentprofile_course_alter_studentprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='made_payment',
            field=models.BooleanField(default=False),
        ),
    ]