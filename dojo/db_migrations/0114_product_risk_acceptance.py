# Generated by Django 3.1.12 on 2021-07-06 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0113_endpoint_protocol'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='risk_acceptance',
            field=models.ManyToManyField(blank=True, default=None, editable=False, to='dojo.Risk_Acceptance'),
        ),
    ]
