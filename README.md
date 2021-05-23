# django_csv_rest
A Django app that consumes a CSV file and supports RESTful APIs

# Assumptions
* To save time, I came up with only one Model so that loading the data is easy as one line: `home = Home(**csv_dict_row)`
* The following fields can be another Model with a `OneToOne` relationship to a `Home`:
```python
class ZillowInformation(Model):
    rentzestimate_amount = IntegerField(null=True, blank=True)
    rentzestimate_last_updated = DateField(null=True, blank=True)
    zestimate_amount = IntegerField(null=True, blank=True)
    zestimate_last_updated = DateField()
    zillow_id = IntegerField()
```
* `Home.id` is autoincrement because there is no candidate for a unique identifier
* Running the command again with the same CSV file will duplicate rows (see above). As such, the command wipes the previously
imported rows for quick debugging.
* An empty value in the cell is considered `NULL` instead of an empty string, for consistency

# References
* [Serializer](https://www.django-rest-framework.org/tutorial/1-serialization/)
* [API Views](https://www.django-rest-framework.org/tutorial/2-requests-and-responses/)

# Set up
```shell
cd path/to/django_csv_rest
python3 -m venv venv/django
source venv/django/bin/activate
pip install -r requirements.txt
```

# Run server
Given that the virtualenv had been set up and activated
```shell
cd path/to/django_csv_rest/bungalow
python manage.py runserver
```

# Load data
The app comes with a command to load in data from the path to a CSV file. An example usage with the test CSV file:
```shell
cd path/to/django_csv_rest/bungalow
python manage.py load_csv main/csv/test_data.csv
```

# REST APIs
With the server running, we can make the following requests
## Get all homes
```shell
curl --location --request GET 'http://127.0.0.1:8000/homes'
```
```json
[
    {
        "id": 2241,
        "area_unit": "SqFt",
        "bathrooms": "2.00",
        "bedrooms": 4,
        "home_size": 1372,
        "home_type": "SingleFamily",
        "last_sold_date": null,
        "last_sold_price": null,
        "link": "https://www.zillow.com/homedetails/7417-Quimby-Ave-West-Hills-CA-91307/19866015_zpid/",
        "price": "$739K",
        "property_size": 10611,
        "rent_price": null,
        "rentzestimate_amount": 2850,
        "rentzestimate_last_updated": "2018-08-07",
        "tax_value": 215083,
        "tax_year": 2017,
        "year_built": 1956,
        "zestimate_amount": 709630,
        "zestimate_last_updated": "2018-08-07",
        "zillow_id": 19866015,
        "address": "7417 Quimby Ave",
        "city": "West Hills",
        "state": "CA",
        "zipcode": "91307"
    },
    ...
]
```

## Get a home
```shell
curl --location --request GET 'http://127.0.0.1:8000/homes/2688'
```
```json
{
    "id": 2688,
    "area_unit": "SqFt",
    "bathrooms": "6.00",
    "bedrooms": 5,
    "home_size": 4830,
    "home_type": "SingleFamily",
    "last_sold_date": "2017-02-22",
    "last_sold_price": 2790000,
    "link": "https://www.zillow.com/homedetails/4146-Allott-Ave-Sherman-Oaks-CA-91423/20028524_zpid/",
    "price": "$2.79M",
    "property_size": 7974,
    "rent_price": null,
    "rentzestimate_amount": 10699,
    "rentzestimate_last_updated": "2018-08-07",
    "tax_value": 2411460,
    "tax_year": 2017,
    "year_built": 2016,
    "zestimate_amount": 3225008,
    "zestimate_last_updated": "2018-08-07",
    "zillow_id": 20028524,
    "address": "4146 Allott Ave",
    "city": "Sherman Oaks",
    "state": "CA",
    "zipcode": "91423"
}
```

## Create a new home
```shell
curl --location --request POST 'http://127.0.0.1:8000/homes/' --header 'Content-Type: application/json' --data-raw '{
    "area_unit": "SqFt",
    "bathrooms": 6.00,
    "bedrooms": 5,
    "home_size": 4830,
    "home_type": "SingleFamily",
    "last_sold_date": "2017-02-22",
    "last_sold_price": 2790000,
    "link": "https://www.zillow.com/homedetails/4146-Allott-Ave-Sherman-Oaks-CA-91423/20028524_zpid/",
    "price": "$2.79M",
    "property_size": 7974,
    "rent_price": null,
    "rentzestimate_amount": 10699,
    "rentzestimate_last_updated": "2018-08-07",
    "tax_value": 2411460,
    "tax_year": 2017,
    "year_built": 2016,
    "zestimate_amount": 3225008,
    "zestimate_last_updated": "2018-08-07",
    "zillow_id": 20028524,
    "address": "4444 Allott Ave",
    "city": "Sherman Oaks",
    "state": "CA",
    "zipcode": "91423"
}'
```
Optional fields:
* bathrooms
* home_size
* last_sold_date
* last_sold_price
* rent_price
* rentzestimate_amount
* rentzestimate_last_updated
* year_built
* zestimate_amount