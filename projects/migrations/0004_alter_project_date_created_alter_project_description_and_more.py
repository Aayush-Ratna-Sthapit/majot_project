# Generated by Django 4.2.1 on 2023-07-18 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default='2023-07-18 15:30:00.000000'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
