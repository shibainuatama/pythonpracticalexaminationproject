import csv
from django.core.management.base import BaseCommand
from quiz.models import Book

class Command(BaseCommand):
    help = 'Imports data from a specified CSV file using DictReader.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to import.')

    def handle(self, *args, **options):
        file_path = options['csv_file']
        
        try:
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                
                for row in reader:
                    Book.objects.create(
                        chapter = row['chapter'],
                        title = row['title'],
                        link = row['link']
                    )
                self.stdout.write(self.style.SUCCESS('Successfully imported data from "%s"' % file_path))
                
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File "%s" not found.' % file_path))
        except KeyError as e:
            self.stdout.write(self.style.ERROR(f'Missing column in CSV: {e}'))