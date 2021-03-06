# Generated by Django 2.2.17 on 2021-02-27 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0080_jira_issue_templates'),
    ]

    operations = [
        migrations.AddField(
            model_name='finding',
            name='last_status_update',
            field=models.DateTimeField(auto_now_add=True, null=True, blank=True, help_text='Timestamp of latest status update (change in status related fields).', verbose_name='Last Status Update'),
        ),
    ]
