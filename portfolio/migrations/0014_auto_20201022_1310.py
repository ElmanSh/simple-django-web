# Generated by Django 3.1.1 on 2020-10-22 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_slide_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='slide_image',
            new_name='SlideImage',
        ),
    ]