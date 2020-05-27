import csv
import sys
from .models import Person, Record


class CsvDataSource:
    def __init__(self, path):
        self.path = path
        self.csv_file = None

        # start counting after header
        # could have arg to configure this?
        self.line = 1

    def __enter__(self):
        self.csv_file = open(self.path)
        self.reader = iter(csv.reader(self.csv_file))
        return self

    def __exit__(self, type, value, traceback):
        self.csv_file.close()

    def __iter__(self):
        err = sys.stderr

        next(self.reader)

        for row in self.reader:
            self.line += 1

            if len(row) != 4:
                print(f'invalid record on line {self.line}', file=err)
                continue

            yield Record(line_num=self.line, person=Person(*row))
