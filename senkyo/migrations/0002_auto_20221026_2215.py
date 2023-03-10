# Generated by Django 3.2.15 on 2022-10-26 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senkyo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_name', models.CharField(max_length=20, verbose_name='名前')),
                ('chat_content', models.TextField(verbose_name='経歴')),
            ],
        ),
        migrations.RemoveField(
            model_name='kouho',
            name='fl1',
        ),
        migrations.RemoveField(
            model_name='kouho',
            name='fl10',
        ),
        migrations.RemoveField(
            model_name='kouho',
            name='fl2',
        ),
        migrations.RemoveField(
            model_name='kouho',
            name='fl3',
        ),
        migrations.RemoveField(
            model_name='kouho',
            name='fl4',
        ),
        migrations.RemoveField(
            model_name='kouho',
            name='fl5',
        ),
        migrations.RemoveField(
            model_name='kouho',
            name='fl6',
        ),
        migrations.RemoveField(
            model_name='kouho',
            name='fl7',
        ),
        migrations.RemoveField(
            model_name='kouho',
            name='fl8',
        ),
        migrations.RemoveField(
            model_name='kouho',
            name='fl9',
        ),
        migrations.AddField(
            model_name='kouho',
            name='flag',
            field=models.CharField(default='unchecked', max_length=20, verbose_name='フラグ'),
        ),
    ]
