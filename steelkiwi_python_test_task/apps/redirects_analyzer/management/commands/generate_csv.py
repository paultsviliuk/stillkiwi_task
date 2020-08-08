import csv

from django.core.management.base import BaseCommand

from redirects_analyzer.models import RedirectData
from redirects_analyzer.serializers import RedirectDataListSerializer


class Command(BaseCommand):
    help = 'Generates csv file with all redirects.'

    def add_arguments(self, parser):
        parser.add_argument('-o', dest='filename', default='redirects_data.csv', help='Csv output file.')

    def handle(self, *args, **options):
        print('test')
        header = [f.name for f in RedirectData._meta.fields]
        data = RedirectData.objects.all()
        serializer = RedirectDataListSerializer(data, many=True)

        with open(options['filename'], 'w') as output:
            writer = csv.DictWriter(output, fieldnames=header)
            writer.writeheader()
            for row in serializer.data:
                writer.writerow(row)
