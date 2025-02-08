# Generated by Django 5.1.5 on 2025-02-05 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='abc@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default='username', max_length=200),
        ),
    ]
