# Generated by Django 3.1.6 on 2021-03-31 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210325_0945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('Bikes', 'Bikes'), ('Car', 'Car'), ('Heavy_Motor', 'Heavy_Motor')], default='', max_length=100)),
                ('timeslap', models.TimeField(blank=True)),
                ('author', models.CharField(max_length=100)),
                ('Image', models.ImageField(default='', upload_to='mysite/images')),
            ],
        ),
        migrations.RenameModel(
            old_name='Apply',
            new_name='Dealership',
        ),
        migrations.DeleteModel(
            name='post',
        ),
    ]
