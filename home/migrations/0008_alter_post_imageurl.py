# Generated by Django 4.2.4 on 2023-09-09 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_post_imageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imageurl',
            field=models.CharField(max_length=255),
        ),
    ]
