# Generated by Django 5.1.1 on 2024-10-01 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_course_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_unit',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]