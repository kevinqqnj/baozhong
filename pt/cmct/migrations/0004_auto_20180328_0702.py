# Generated by Django 2.0.3 on 2018-03-28 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmct', '0003_auto_20180328_0534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accept',
            name='users',
        ),
        migrations.RemoveField(
            model_name='assign',
            name='users',
        ),
        migrations.RemoveField(
            model_name='secure',
            name='users',
        ),
        migrations.AddField(
            model_name='accept',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_ac', to='cmct.Seed'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assign',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_as', to='cmct.Seed'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='secure',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_se', to='cmct.Seed'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='seed',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]