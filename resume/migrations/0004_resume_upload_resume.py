# Generated by Django 5.0.1 on 2024-02-15 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_alter_resume_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='upload_resume',
            field=models.FileField(blank=True, null=True, upload_to='resume'),
        ),
    ]
