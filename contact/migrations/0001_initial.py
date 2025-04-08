# Generated by Django 5.1.6 on 2025-02-21 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('is_read', models.BooleanField(default=False)),
                ('response', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-sent_at'],
            },
        ),
    ]
