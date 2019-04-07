# Generated by Django 2.2 on 2019-04-06 13:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import pylabber.utils
import research.models.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', pylabber.utils.CharNullField(blank=True, max_length=64, null=True, unique=True, validators=[django.core.validators.RegexValidator('^\\d+$', code='invalid_number', message='Digits only!')])),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('date_of_birth', models.DateField(blank=True, null=True, validators=[research.models.validators.not_future], verbose_name='Date of Birth')),
                ('dominant_hand', models.CharField(blank=True, choices=[('RIGHT', 'Right'), ('LEFT', 'Left'), ('AMBI', 'Ambidextrous')], max_length=5)),
                ('sex', models.CharField(blank=True, choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], max_length=6)),
                ('gender', models.CharField(blank=True, choices=[('CIS', 'Cisgender'), ('TRANS', 'Transgender'), ('OTHER', 'Other')], max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='images/studies')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('collaborators', models.ManyToManyField(related_name='studies', to=settings.AUTH_USER_MODEL)),
                ('subjects', models.ManyToManyField(related_name='studies', to='research.Subject')),
            ],
            options={
                'verbose_name_plural': 'Studies',
            },
        ),
    ]
