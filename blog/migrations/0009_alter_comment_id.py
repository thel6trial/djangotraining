# Generated by Django 4.2.1 on 2024-02-14 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_comment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
