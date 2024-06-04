# Generated by Django 5.0.6 on 2024-06-03 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('plan_name', models.CharField(max_length=30)),
                ('plan_id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'plans',
            },
        ),
    ]