# Generated by Django 4.0.5 on 2022-07-06 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('srno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=13)),
                ('author', models.CharField(max_length=500)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
