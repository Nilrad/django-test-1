# Generated by Django 3.2.4 on 2021-06-21 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vigilancia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(max_length=5)),
                ('link', models.CharField(max_length=100)),
                ('bytes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=150)),
                ('last_detected_movement_date', models.DateField()),
                ('last_photo_taken_link', models.CharField(max_length=200)),
                ('last_video_taken_link', models.CharField(max_length=200)),
                ('door_state', models.CharField(max_length=5)),
            ],
        ),
        migrations.AlterModelOptions(
            name='camera',
            options={'ordering': ['code']},
        ),
        migrations.AddField(
            model_name='camera',
            name='state',
            field=models.CharField(default='OFF', max_length=3),
        ),
        migrations.CreateModel(
            name='VideoDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seconds_length', models.SmallIntegerField()),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vigilancia.media')),
            ],
        ),
        migrations.AddField(
            model_name='media',
            name='trap',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vigilancia.trap'),
        ),
    ]
