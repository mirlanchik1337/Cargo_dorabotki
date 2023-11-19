# Generated by Django 4.2.6 on 2023-11-10 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cargo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupTrackCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargo_app.status')),
                ('trackcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargo_app.trackcode', verbose_name='')),
            ],
            options={
                'verbose_name': 'Группа Треккодов',
                'verbose_name_plural': 'Треккод',
            },
        ),
    ]