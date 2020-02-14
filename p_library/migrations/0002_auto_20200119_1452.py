# Generated by Django 2.2.6 on 2020-01-19 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publishes',
            field=models.ManyToManyField(blank=True, help_text='Select a publishes for this book', null=True, related_name='books', to='p_library.Publish'),
        ),
    ]
