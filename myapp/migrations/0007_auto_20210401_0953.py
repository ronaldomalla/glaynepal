# Generated by Django 3.1.6 on 2021-04-01 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20210401_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('......', '......'), ('Bikes', 'Bikes'), ('Cars', 'Cars'), ('Heavy-Motors', 'Heavy-Motors')], default='', max_length=100),
        ),
    ]
