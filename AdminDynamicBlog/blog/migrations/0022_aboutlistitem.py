# Generated by Django 5.0.4 on 2024-08-08 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_whychoosemeslider_remove_staticcontentabout_slider1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
            ],
        ),
    ]