# Generated by Django 5.1 on 2024-08-29 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_enquiry_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='media')),
                ('date', models.IntegerField()),
                ('description', models.CharField(max_length=50)),
            ],
        ),
    ]
