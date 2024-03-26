# Generated by Django 5.0.3 on 2024-03-23 22:01

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resellerUid', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(max_length=100)),
                ('alias', models.CharField(max_length=100)),
                ('taxId', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('country', models.IntegerField()),
                ('state', models.IntegerField()),
                ('countryName', models.CharField(max_length=100)),
                ('regionName', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=255)),
                ('notes', models.TextField(blank=True, null=True)),
                ('zipCode', models.IntegerField()),
                ('website', models.URLField(default='www.alpha.com')),
                ('veeamTenantId', models.CharField(blank=True, max_length=100, null=True)),
                ('subscriptionPlanUid', models.CharField(blank=True, max_length=100, null=True)),
                ('isAlarmDetectEnabled', models.BooleanField(default=False)),
                ('isBackupAgentManagementEnabled', models.BooleanField(default=False)),
                ('isFileLevelRestoreEnabled', models.BooleanField(default=False)),
                ('isBackupServerManagementEnabled', models.BooleanField(default=False)),
                ('isVBPublicCloudManagementEnabled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='VSPCUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('storage_quota', models.BigIntegerField(default=1073741824)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]