# Generated by Django 4.2.11 on 2024-05-29 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageupload',
            name='images',
        ),
        migrations.AddField(
            model_name='imageupload',
            name='img',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='이미지'),
        ),
        migrations.AddField(
            model_name='imageupload',
            name='img_caption',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='imageupload',
            name='filename',
            field=models.CharField(blank=True, max_length=100, verbose_name='파일 이름'),
        ),
    ]