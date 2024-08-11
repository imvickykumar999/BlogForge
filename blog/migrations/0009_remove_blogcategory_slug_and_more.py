# Generated by Django 5.0.4 on 2024-08-03 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blogcategory_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcategory',
            name='slug',
        ),
        migrations.AlterField(
            model_name='article',
            name='article_short_description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='image',
            field=models.ImageField(upload_to='team_images/'),
        ),
    ]