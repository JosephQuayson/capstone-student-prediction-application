# Generated by Django 3.1.7 on 2021-08-16 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_performancepredict_internet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performancepredict',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
