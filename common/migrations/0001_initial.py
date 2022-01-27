# Generated by Django 3.1.3 on 2022-01-26 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('userid', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='사용자 아이디')),
                ('username', models.CharField(max_length=50, verbose_name='사용자 이름')),
                ('phone_num', models.CharField(max_length=13, verbose_name='휴대전화')),
                ('company_name', models.CharField(max_length=30, verbose_name='회사명')),
                ('company_address', models.CharField(max_length=100, verbose_name='회사 주소')),
                ('company_tel', models.CharField(max_length=13, verbose_name='회사 전화')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='이메일')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
