# Generated by Django 4.1.7 on 2023-03-11 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customuser_file_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),

    ]
