# Generated by Django 5.1 on 2024-08-20 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_course_slug_alter_course_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-rating']},
        ),
    ]
