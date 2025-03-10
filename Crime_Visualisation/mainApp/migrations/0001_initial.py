# Generated by Django 2.2.5 on 2019-11-18 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='incidents',
            fields=[
                ('incident_id', models.IntegerField(primary_key=True, serialize=False)),
                ('incident_date', models.DateField()),
                ('incident_time', models.TimeField()),
                ('incident_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='policeDepartment',
            fields=[
                ('dept_id', models.IntegerField(primary_key=True, serialize=False)),
                ('district', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('cnn', models.IntegerField()),
                ('telephone', models.IntegerField()),
                ('supervisor', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='portalUser',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255)),
                ('phone_number', models.IntegerField()),
                ('password', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='report',
            fields=[
                ('report_id', models.IntegerField(primary_key=True, serialize=False)),
                ('incident_category', models.CharField(max_length=255)),
                ('incident_subcategory', models.CharField(max_length=255)),
                ('resolution', models.CharField(max_length=255)),
                ('report_type', models.CharField(max_length=255)),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.policeDepartment')),
                ('incident_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.incidents')),
            ],
        ),
        migrations.CreateModel(
            name='policeOfficial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('official_rank', models.CharField(max_length=255)),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.policeDepartment')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.portalUser')),
            ],
        ),
        migrations.AddField(
            model_name='incidents',
            name='dept_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.policeDepartment'),
        ),
        migrations.CreateModel(
            name='complainant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.portalUser')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.incidents')),
            ],
        ),
    ]
