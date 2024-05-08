# Generated by Django 4.2.11 on 2024-05-08 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=40, unique=True, verbose_name='아이디')),
                ('pwd', models.CharField(max_length=300, verbose_name='비밀번호')),
                ('username', models.CharField(max_length=40, verbose_name='이름')),
                ('birth', models.DateField(verbose_name='생일')),
                ('gender', models.CharField(max_length=20, verbose_name='성별')),
                ('email', models.EmailField(max_length=300, verbose_name='이메일')),
            ],
        ),
    ]
