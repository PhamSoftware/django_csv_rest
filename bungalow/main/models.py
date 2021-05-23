from django.db.models import (
    Model,
    CharField,
    IntegerField,
    DecimalField,
    DateField,
    URLField,
)


class Home(Model):
    UNITS = [("SqFt", "sqft")]

    TYPES = [
        ("SingleFamily", "Single Family"),
        ("VacantResidentialLand", "Vacant Residential Land"),
        ("Miscellaneous", "Miscellaneous"),
        ("MultiFamily2To4", "Multi Family"),
        ("Condominium", "Condominium"),
        ("Apartment", "Apartment"),
        ("Duplex", "Duplex"),
    ]

    area_unit = CharField(max_length=10, choices=UNITS)
    bathrooms = DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    bedrooms = IntegerField()
    home_size = IntegerField(null=True, blank=True)
    home_type = CharField(max_length=30, choices=TYPES)
    last_sold_date = DateField(null=True, blank=True)
    last_sold_price = IntegerField(null=True, blank=True)
    link = URLField()
    price = CharField(max_length=10)
    property_size = IntegerField(null=True)
    rent_price = IntegerField(null=True, blank=True)
    rentzestimate_amount = IntegerField(null=True, blank=True)
    rentzestimate_last_updated = DateField(null=True, blank=True)
    tax_value = IntegerField()
    tax_year = IntegerField()
    year_built = IntegerField(null=True, blank=True)
    zestimate_amount = IntegerField(null=True, blank=True)
    zestimate_last_updated = DateField()
    zillow_id = IntegerField()
    address = CharField(max_length=100)
    city = CharField(max_length=50)
    state = CharField(max_length=2)
    zipcode = CharField(max_length=5)
