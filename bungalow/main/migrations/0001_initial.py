# Generated by Django 3.2.3 on 2021-05-23 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_unit', models.CharField(choices=[('SqFt', 'sqft')], max_length=10)),
                ('bathrooms', models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)),
                ('bedrooms', models.IntegerField()),
                ('home_size', models.IntegerField(null=True, blank=True)),
                ('home_type', models.CharField(choices=[('SingleFamily', 'Single Family'), ('VacantResidentialLand', 'Vacant Residential Land'), ('Miscellaneous', 'Miscellaneous'), ('MultiFamily2To4', 'Multi Family'), ('Condominium', 'Condominium'), ('Apartment', 'Apartment'), ('Duplex', 'Duplex')], max_length=30)),
                ('last_sold_date', models.DateField(blank=True, null=True)),
                ('last_sold_price', models.IntegerField(blank=True, null=True)),
                ('link', models.URLField()),
                ('price', models.CharField(max_length=10)),
                ('property_size', models.IntegerField(null=True)),
                ('rent_price', models.IntegerField(blank=True, null=True)),
                ('rentzestimate_amount', models.IntegerField(null=True, blank=True)),
                ('rentzestimate_last_updated', models.DateField(null=True, blank=True)),
                ('tax_value', models.IntegerField()),
                ('tax_year', models.IntegerField()),
                ('year_built', models.IntegerField(blank=True, null=True)),
                ('zestimate_amount', models.IntegerField(blank=True, null=True)),
                ('zestimate_last_updated', models.DateField()),
                ('zillow_id', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=5)),
            ],
        ),
    ]
