# Generated by Django 4.2.4 on 2023-09-14 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_experience_e_to_alter_experience_e_from'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=100)),
                ('s_percentage', models.IntegerField()),
            ],
        ),
    ]
