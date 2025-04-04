# Generated by Django 5.1.6 on 2025-03-28 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='cores',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='cpu',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='server',
            name='ghz',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='port',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='region',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='server',
            name='storage',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='server',
            name='title',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='server',
            name='traffic',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
