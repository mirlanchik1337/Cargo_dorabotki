# Generated by Django 4.2.6 on 2023-11-25 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cargo_app', '0006_remove_group_track_codes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackcode',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='track_codes', to='cargo_app.group'),
        ),
    ]
