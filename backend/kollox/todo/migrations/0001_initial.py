# Generated by Django 3.1.3 on 2020-12-10 18:37

import authentication.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remind_time', models.DateTimeField(blank=True, null=True, verbose_name='Remind Time')),
                ('is_repited', models.BooleanField(default=False, verbose_name='Repeat?')),
                ('repeat_frequency', models.CharField(blank=True, choices=[('none', 'None'), ('every_day', 'Everyday'), ('every_hour', 'Every hour'), ('custom', 'Custom')], default='none', max_length=256)),
            ],
            options={
                'verbose_name': 'Reminder',
                'ordering': ['remind_time'],
            },
        ),
        migrations.CreateModel(
            name='ToDoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512, verbose_name='Task Title')),
                ('description', models.TextField(blank=True, verbose_name='Desctiption')),
                ('todo_list_id', models.PositiveIntegerField()),
                ('attached_file', models.FileField(blank=True, upload_to='files/')),
                ('attached_photo', models.ImageField(blank=True, upload_to='images/')),
                ('remind_me', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(default=False, verbose_name='Is Completed')),
                ('started_time', models.DateTimeField(auto_now=True, verbose_name='Started time')),
                ('expired_time', models.DateTimeField(blank=True, null=True, verbose_name='Expired Time')),
                ('is_favorite', models.BooleanField(default=False, verbose_name='Is favorite')),
                ('is_important', models.BooleanField(default=False, verbose_name='Is Important')),
                ('reminder', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reminder_task', to='todo.reminder')),
                ('subtask', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.todoitem')),
                ('todo_list_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'ToDo Item',
                'ordering': ['started_time', 'expired_time', 'is_important', 'is_favorite'],
            },
        ),
        migrations.CreateModel(
            name='SimpleToDoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=512, verbose_name='ToDo-List Name')),
                ('favorite', models.BooleanField(default=False, verbose_name='is Favorite')),
                ('status', models.CharField(choices=[('in_archive', 'In Archive'), ('started', 'Started'), ('completed', 'Completed'), ('not_complted', 'Not Completed'), ('not_started', 'Not Started')], default='not_started', max_length=255, verbose_name='Status')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_simple_todo_lists', to=settings.AUTH_USER_MODEL, verbose_name='ToDo-List Owner')),
            ],
            options={
                'verbose_name': 'Simple ToDo List',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=512, verbose_name='ToDo-List Name')),
                ('favorite', models.BooleanField(default=False, verbose_name='is Favorite')),
                ('percentage_completed', models.DecimalField(decimal_places=2, default=0, max_digits=5, validators=[authentication.validators.percent_validation], verbose_name='Completed Status')),
                ('status', models.CharField(choices=[('in_archive', 'In Archive'), ('started', 'Started'), ('completed', 'Completed'), ('not_complted', 'Not Completed'), ('not_started', 'Not Started')], default='not_started', max_length=256, verbose_name='Status')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_projects', to=settings.AUTH_USER_MODEL, verbose_name='ToDo-List Owner')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
