# Generated by Django 3.2.7 on 2021-11-24 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_tracker_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='desc',
            field=models.CharField(default='Order has been placed', max_length=300),
        ),
    ]