# Generated by Django 3.2.4 on 2021-06-30 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dndWiki', '0006_alter_monster_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]
