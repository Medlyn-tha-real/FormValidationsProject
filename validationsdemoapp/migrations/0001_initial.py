# Generated by Django 5.0 on 2024-06-21 12:18

from django.db import migrations, models # type: ignore


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, verbose_name='User Name')),
                ('password', models.CharField(max_length=15, verbose_name='Password')),
                ('confirm_password', models.CharField(max_length=15, verbose_name='Confirm Password')),
                ('gender', models.CharField(max_length=10, verbose_name='Gender')),
                ('country', models.CharField(max_length=20, verbose_name='Country')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('postal_code', models.IntegerField(verbose_name='Postal Code')),
                ('phone_number', models.CharField(max_length=13, verbose_name='Phone Number')),
                ('profile', models.TextField(blank=True, verbose_name='Profile of User')),
                ('website_url', models.URLField(verbose_name='website URL')),
                ('terms_condition', models.BooleanField(verbose_name='Terms & Conditions')),
                ('favwebsite_url', models.CharField(max_length=256)),
            ],
        ),
    ]
