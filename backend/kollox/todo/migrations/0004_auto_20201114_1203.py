# Generated by Django 3.1.3 on 2020-11-14 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20201113_2335'),
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
        migrations.RemoveField(
            model_name='todoitem',
            name='is_repited',
        ),
        migrations.RemoveField(
            model_name='todoitem',
            name='remind_time',
        ),
        migrations.RemoveField(
            model_name='todoitem',
            name='repeat_frequency',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='reminder',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reminder_task', to='todo.reminder'),
        ),
    ]
