# Generated by Django 4.2.1 on 2024-02-17 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_user_access_token_user_refresh_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='expires_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Expire of Access Token'),
        ),
    ]