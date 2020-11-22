# Generated by Django 3.1.2 on 2020-11-22 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0025_remove_data_hits'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleHit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.data')),
                ('ip_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.ipaddress')),
            ],
        ),
        migrations.AddField(
            model_name='data',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', through='portfolio.ArticleHit', to='portfolio.IPAddress', verbose_name='بازدید ها'),
        ),
    ]
