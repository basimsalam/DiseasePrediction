# Generated by Django 3.2.23 on 2024-04-07 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ds_app', '0004_department_disease_symptoms'),
    ]

    operations = [
        migrations.CreateModel(
            name='chat_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('FROMID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ft', to='ds_app.login_table')),
                ('TOID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tt', to='ds_app.login_table')),
            ],
        ),
    ]
