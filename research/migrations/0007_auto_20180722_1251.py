# Generated by Django 2.0.7 on 2018-07-22 12:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0006_study_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='collaborators',
            field=models.ManyToManyField(related_name='studies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='study',
            name='subjects',
            field=models.ManyToManyField(related_name='studies', to='research.Subject'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1),
        ),
    ]