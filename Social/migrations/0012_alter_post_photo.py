# Generated by Django 5.2 on 2025-05-07 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Social', '0011_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media_post'),
        ),
    ]
