# Generated by Django 4.1.7 on 2023-03-11 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_delete_user_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True, verbose_name='email address'),
        ),
    ]
