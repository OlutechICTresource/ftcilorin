# Generated by Django 5.1.1 on 2024-10-04 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(upload_to='media/testimonials/'),
        ),
    ]
