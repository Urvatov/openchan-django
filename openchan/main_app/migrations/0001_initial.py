# Generated by Django 5.0.2 on 2024-02-14 19:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=64, unique=True)),
                ('title', models.CharField(max_length=24)),
                ('description', models.TextField(blank=True)),
                ('all_posts', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('text', models.TextField(blank=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('all_posts', models.IntegerField()),
                ('board', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main_app.board')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='Аноним', max_length=64)),
                ('text', models.TextField(blank=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('board', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main_app.board')),
                ('thread', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main_app.thread')),
            ],
        ),
    ]
