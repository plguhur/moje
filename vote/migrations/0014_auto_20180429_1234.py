# Generated by Django 2.0.3 on 2018-04-29 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0013_candidate_program'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('email',)},
        ),
    ]
