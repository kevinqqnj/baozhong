# Generated by Django 2.0.3 on 2018-03-28 07:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmct', '0004_auto_20180328_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accept',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ac', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='assign',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_as', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='secure',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_se', to=settings.AUTH_USER_MODEL),
        ),
    ]
