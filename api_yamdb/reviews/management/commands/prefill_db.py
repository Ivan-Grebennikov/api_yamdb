import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from reviews import models


class Command(BaseCommand):

    def handle(self, *args, **options):
        csv_data_files = (
            (models.User, 'users.csv'),
            (models.Category, 'category.csv'),
            (models.Genre, 'genre.csv'),
            (models.Title, 'titles.csv'),
            (models.GenreTitle, 'genre_title.csv'),
            (models.Review, 'review.csv'),
            (models.Comment, 'comments.csv'),
        )

        self.stdout.write(
            self.style.NOTICE(
                'Clearing Database...\n'
            )
        )

        for model, _ in reversed(csv_data_files):
            model.objects.all().delete()

        self.stdout.write(
            self.style.NOTICE(
                'Starting to add prepared data...\n'
            )
        )

        for model, filename in csv_data_files:
            filepath = os.path.join(
                settings.BASE_DIR, 'static', 'data', filename
            )

            self.stdout.write(
                self.style.NOTICE(
                    f'Processing file {filepath}\n'
                )
            )

            with open(filepath, newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                for row in csv_reader:
                    object_data = self.prepare_model_object_data(row)
                    model.objects.get_or_create(**object_data)

        self.stdout.write(
            self.style.SUCCESS(
                'Database has been filled successfully!'
            )
        )

    def prepare_model_object_data(self, csv_row_dict):
        foreign_keys = {
            'category': (models.Category, 'category'),
            'title_id': (models.Title, 'title'),
            'genre_id': (models.Genre, 'genre'),
            'author': (models.User, 'author'),
            'review_id': (models.Review, 'review')
        }

        object_data = {}

        for column, value in csv_row_dict.items():
            if column in foreign_keys:
                (model, field_name) = foreign_keys[column]
                obj = model.objects.get(pk=csv_row_dict[column])
                object_data[field_name] = obj
            else:
                object_data[column] = value

        return object_data
