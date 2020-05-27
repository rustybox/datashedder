import csv
import sys
from .models import Person, Record

class DuplicateWriter:
    def __init__(self, path):
        self.path = path
        self.csv_file = None
        self.writer = None

    def __enter__(self):
        self.csv_file = open(self.path, 'w')
        self.writer = csv.writer(self.csv_file)
        self.writer.writerow(['line', 'full_name', 'fuzzy'])
        return self

    def __exit__(self, type, value, traceback):
        self.csv_file.close()

    def log_duplicate(self, record, fuzzy):
        self.writer.writerow([record.line_num, record.person.full_name, fuzzy])
