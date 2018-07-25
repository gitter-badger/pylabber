# Generated by Django 2.0.7 on 2018-07-24 13:51

from django.db import migrations, models
import research.models.choices


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0003_auto_20180724_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='dominant_hand',
            field=models.CharField(choices=[('RIGHT', 'Right'), ('LEFT', 'Left'), ('AMBI', 'Ambidextrous')], default=research.models.choices.DominantHand('Right'), max_length=5),
        ),
    ]