# Generated by Django 2.2.6 on 2020-02-07 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0005_auto_20200131_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='photo',
            field=models.ImageField(blank=True, upload_to='books_photo'),
        ),
    ]
