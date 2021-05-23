import csv
import re
from datetime import datetime

from django.core.management.base import BaseCommand
from main.models import Home

date_regex = re.compile("\d\d/\d\d/\d\d\d\d")


def empty_string_to_none(row: dict):
    empty_strings = {key: None for key, value in row.items() if value == ''}

    return {**row, **empty_strings}


def load_date(row: dict):
    dates = {key: datetime.strptime(value, "%m/%d/%Y").date().strftime("%Y-%m-%d")
             for key, value in row.items() if date_regex.search(value)}

    return {**row, **dates}


class Command(BaseCommand):
    help = "Load content of a CSV file to create rows in the database"

    def add_arguments(self, parser):
        parser.add_argument("path", type=str)

    def handle(self, *args, **options):
        path = options["path"]
        # clear out the db first for now
        Home.objects.all().delete()
        with open(f"{path}", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                normalized = load_date(row)
                normalized = empty_string_to_none(normalized)
                home = Home(**normalized)
                home.save()

        self.stdout.write(self.style.SUCCESS(f"Successfully loaded file {path}"))
