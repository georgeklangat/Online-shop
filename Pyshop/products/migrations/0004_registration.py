# Generated by Django 4.2.5 on 2023-09-13 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_descriptions_offer_descripton'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('admission_no', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
    ]
