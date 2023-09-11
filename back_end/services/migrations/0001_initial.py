# Generated by Django 4.2.5 on 2023-09-11 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SectorApprovedRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genocide_survivor_certificate', models.FileField(upload_to='documents/')),
                ('social_status_class', models.CharField(max_length=100)),
                ('deprived_certificate', models.FileField(upload_to='documents/')),
                ('message', models.TextField()),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.sector')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genocide_survivor_certificate', models.FileField(upload_to='documents/')),
                ('social_status_class', models.CharField(max_length=100)),
                ('deprived_certificate', models.FileField(upload_to='documents/')),
                ('message', models.TextField()),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.sector')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApprovedRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genocide_survivor_certificate', models.FileField(upload_to='documents/')),
                ('social_status_class', models.CharField(max_length=100)),
                ('deprived_certificate', models.FileField(upload_to='documents/')),
                ('message', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]