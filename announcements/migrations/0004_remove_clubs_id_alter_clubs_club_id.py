# Generated by Django 4.0.3 on 2023-02-26 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0003_alter_club_members_club_id_alter_clubs_club_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clubs',
            name='id',
        ),
        migrations.AlterField(
            model_name='clubs',
            name='club_id',
            field=models.CharField(max_length=6, primary_key=True, serialize=False),
        ),
    ]
