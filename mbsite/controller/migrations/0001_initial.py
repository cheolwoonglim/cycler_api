# Generated by Django 2.1.3 on 2018-11-15 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CyclerInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=5)),
                ('wafer', models.CharField(max_length=10)),
                ('array', models.CharField(max_length=10)),
                ('Tstart', models.DateTimeField(default='2018-11-15')),
                ('Icharge', models.FloatField(default=0.1)),
                ('Idischarge', models.FloatField(default=-0.1)),
                ('Vmax', models.FloatField(default=4.2)),
                ('Vmin', models.FloatField(default=3.0)),
                ('Tstep', models.IntegerField(default=30)),
                ('schedule', models.CharField(default='ocodocodocodo', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cyclers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=7, unique=True)),
                ('url', models.CharField(max_length=30)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='cyclerinput',
            name='node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controller.Cyclers'),
        ),
    ]
