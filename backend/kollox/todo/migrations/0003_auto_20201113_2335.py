# Generated by Django 3.1.3 on 2020-11-13 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20201113_2024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todoitem',
            options={'ordering': ['started_time', 'expired_time', 'is_important', 'is_favorite'], 'verbose_name': 'ToDo Item'},
        ),
        migrations.RemoveField(
            model_name='todoitem',
            name='completed',
        ),
        migrations.AddField(
            model_name='project',
            name='favorite',
            field=models.BooleanField(default=False, verbose_name='is Favorite'),
        ),
        migrations.AddField(
            model_name='simpletodolist',
            name='favorite',
            field=models.BooleanField(default=False, verbose_name='is Favorite'),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='attached_file',
            field=models.FileField(blank=True, upload_to='files/'),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='attached_photo',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='expired_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Expired Time'),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='is_completed',
            field=models.BooleanField(default=False, verbose_name='Is Completed'),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='is_favorite',
            field=models.BooleanField(default=False, verbose_name='Is favorite'),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='is_important',
            field=models.BooleanField(default=False, verbose_name='Is Important'),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='is_repited',
            field=models.BooleanField(default=False, verbose_name='Repeat?'),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='remind_me',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='remind_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Remind Time'),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='repeat_frequency',
            field=models.CharField(blank=True, choices=[('none', 'None'), ('every_day', 'Everyday'), ('every_hour', 'Every hour'), ('custom', 'Custom')], default='none', max_length=256),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='started_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Started time'),
        ),
    ]
