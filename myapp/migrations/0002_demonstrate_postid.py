# Generated by Django 4.2.7 on 2024-01-03 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='demonstrate',
            name='postId',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
