# Generated by Django 4.0 on 2024-04-03 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIapp', '0002_imageai_imageai_ai'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('content', models.TextField(blank=True, max_length=255)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='mediaphoto')),
            ],
        ),
        migrations.DeleteModel(
            name='Imageai',
        ),
    ]
