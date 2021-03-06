# Generated by Django 3.1.3 on 2021-01-14 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual_name', models.CharField(max_length=10, verbose_name='姓名')),
                ('authority', models.CharField(choices=[('admin', '管理者'), ('employee', '照服員'), ('resident', '住民'), ('family', '家屬'), ('vendor', '廠商')], default='resident', max_length=20, verbose_name='身分')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d/', verbose_name='照片')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
