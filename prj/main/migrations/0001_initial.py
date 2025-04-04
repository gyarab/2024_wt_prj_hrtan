# Generated by Django 5.1.6 on 2025-03-28 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('region', models.CharField(max_length=20)),
                ('cpu', models.CharField(max_length=20)),
                ('cores', models.IntegerField(blank=True, null=True)),
                ('ghz', models.IntegerField(blank=True, null=True)),
                ('storage', models.CharField(max_length=30)),
                ('port', models.IntegerField(blank=True, null=True)),
                ('traffic', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
