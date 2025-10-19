import csv
from django.core.management.base import BaseCommand
from quiz.models import Quiz

class Command(BaseCommand):
    help = 'Imports data from a specified CSV file using DictReader.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to import.')

    def handle(self, *args, **options):
        file_path = options['csv_file']
        
        try:
            # encoding='utf-8-sig' … BOMありCSVを読む場合に必要
            with open(file_path, 'r', encoding='utf-8-sig') as f:
              
                # セル内改行のあるエクセルデータを読み込む場合は、
                # データにダブルクォーテーションが必要
                reader = csv.DictReader(f)
                
                for row in reader:
                    Quiz.objects.create(
                        chapter = row['chapter'],
                        number = row['number'],
                        about = row['about'],
                        question = row['question'],
                        optionA = row['optionA'],
                        optionB = row['optionB'],
                        optionC = row['optionC'],
                        optionD = row['optionD'],
                        correctanswer = row['correctanswer'],
                        explanation = row['explanation']
                    )
                self.stdout.write(self.style.SUCCESS('Successfully imported data from "%s"' % file_path))
                
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File "%s" not found.' % file_path))
        except KeyError as e:
            self.stdout.write(self.style.ERROR(f'Missing column in CSV: {e}'))