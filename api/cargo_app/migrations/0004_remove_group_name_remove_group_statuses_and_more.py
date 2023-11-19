# Generated by Django 4.2.6 on 2023-11-12 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cargo_app', '0003_group_delete_grouptrackcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='name',
        ),
        migrations.RemoveField(
            model_name='group',
            name='statuses',
        ),
        migrations.AddField(
            model_name='group',
            name='statuses',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='cargo_app.status'),
            preserve_default=False,
        ),
    ]