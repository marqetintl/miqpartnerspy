# Generated by Django 4.0.2 on 2022-07-25 00:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import miq.core.models.user
import miqpartners.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0003_sitesetting_whatsapp_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.user',),
            managers=[
                ('objects', miq.core.models.user.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.uuid4, editable=False, max_length=100, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creation date and time')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='update date and time')),
                ('first_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2, message='Enter your first name.')], verbose_name='First name')),
                ('last_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2, message='Enter your last name.')], verbose_name='Last name')),
                ('phone', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(4, message='Veuillez entrer votre numéro de téléphone.')], verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('tt', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tiktok')),
                ('ig', models.CharField(blank=True, max_length=100, null=True, verbose_name='Instagram')),
                ('extra', models.JSONField(default=miqpartners.models.jsondef, verbose_name='Additional Information')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='partner', to='miqpartners.partneruser')),
            ],
            options={
                'verbose_name': 'Partner',
                'verbose_name_plural': 'Partners',
                'ordering': ('-created',),
            },
        ),
    ]
