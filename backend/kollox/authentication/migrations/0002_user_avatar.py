# Generated by Django 3.1.3 on 2020-12-11 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='noimage.jpg', upload_to='d:/repos/kollox/frontend/src/assets/'),
        ),
    ]
