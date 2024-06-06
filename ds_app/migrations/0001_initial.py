# Generated by Django 3.2.23 on 2024-02-02 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='doctor_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('phoneno', models.BigIntegerField()),
                ('email', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('pin', models.IntegerField()),
                ('dob', models.DateField()),
                ('image', models.FileField(upload_to='')),
                ('gender', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('consultfee', models.IntegerField()),
                ('certificate', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='expert_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('phoneno', models.BigIntegerField()),
                ('email', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('pin', models.IntegerField()),
                ('dob', models.DateField()),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='login_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='user_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('phoneno', models.BigIntegerField()),
                ('email', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('pin', models.IntegerField()),
                ('dob', models.DateField()),
                ('image', models.FileField(upload_to='')),
                ('gender', models.CharField(max_length=100)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ds_app.login_table')),
            ],
        ),
        migrations.CreateModel(
            name='tip_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip', models.CharField(max_length=500)),
                ('EXPERT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ds_app.expert_table')),
            ],
        ),
        migrations.CreateModel(
            name='schedule_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('fromtime', models.TimeField()),
                ('totime', models.TimeField()),
                ('DOCTOR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ds_app.doctor_table')),
            ],
        ),
        migrations.CreateModel(
            name='prescription_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription', models.CharField(max_length=500)),
                ('report', models.FileField(upload_to='')),
                ('date', models.DateField()),
                ('BOOKING', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ds_app.booking_table')),
            ],
        ),
        migrations.CreateModel(
            name='feedback_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('feedback', models.CharField(max_length=500)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ds_app.user_table')),
            ],
        ),
        migrations.AddField(
            model_name='expert_table',
            name='LOGIN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ds_app.login_table'),
        ),
        migrations.CreateModel(
            name='doubt_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doubt', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('reply', models.CharField(max_length=500)),
                ('EXPERT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ds_app.expert_table')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ds_app.user_table')),
            ],
        ),
        migrations.AddField(
            model_name='doctor_table',
            name='LOGIN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ds_app.login_table'),
        ),
        migrations.CreateModel(
            name='complaint_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=500)),
                ('reply', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ds_app.user_table')),
            ],
        ),
        migrations.AddField(
            model_name='booking_table',
            name='SCHEDULE',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ds_app.schedule_table'),
        ),
        migrations.AddField(
            model_name='booking_table',
            name='USER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ds_app.user_table'),
        ),
    ]
