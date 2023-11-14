# Generated by Django 4.1.13 on 2023-11-14 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teaser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locked', models.BooleanField(default=False, editable=False, verbose_name='locked')),
                ('locked_at', models.DateTimeField(editable=False, null=True, verbose_name='locked at')),
                ('body', models.CharField(max_length=255)),
                ('locked_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='locked_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='locked by')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
