# Generated by Django 5.2 on 2025-07-17 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_profile_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='box',
            field=models.CharField(choices=[('CF4TIME ', 'CAMPINA'), ('CF4TIME', 'JOCKEY')], default='DEFAULT'),
        ),
    ]
