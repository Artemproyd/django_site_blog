# Generated by Django 3.2.16 on 2024-02-28 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pub_date'], 'verbose_name': 'публикация', 'verbose_name_plural': 'Публикации'},
        ),
    ]
