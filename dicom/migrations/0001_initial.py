# Generated by Django 2.0.7 on 2018-07-22 12:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('research', '0007_auto_20180722_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=500)),
                ('number', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('date_of_birth', models.DateField()),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('subject', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='research.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('description', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=64)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'verbose_name_plural': 'Studies',
            },
        ),
        migrations.AddField(
            model_name='instance',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dicom.Patient'),
        ),
        migrations.AddField(
            model_name='instance',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dicom.Series'),
        ),
        migrations.AddField(
            model_name='instance',
            name='study',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dicom.Study'),
        ),
    ]