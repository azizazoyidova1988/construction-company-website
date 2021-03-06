# Generated by Django 3.2.9 on 2021-11-17 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0002_oficce_contact_icons'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('author', models.CharField(blank=True, max_length=450, null=True)),
                ('description', models.CharField(blank=True, max_length=450, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'blog',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('video', models.ImageField(null=True, upload_to='video/', verbose_name='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'video',
            },
        ),
    ]
