# Generated by Django 3.1.3 on 2020-12-15 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todoitem',
            options={'ordering': ['-started_time', 'is_completed'], 'verbose_name': 'Todo Item'},
        ),
    ]