import argparse
from .datasource import CsvDataSource
from .fuzzysearcher import FuzzySearcher
from .datacleansing import DataCleanser
from .reporting import DuplicateWriter

parser = argparse.ArgumentParser(prog='datashedder')

parser.add_argument(
    'input_csv',
    help='Path to csv file to process'
)

parser.add_argument(
    '-o',
    '--output',
    type=str,
    default='relateddata.csv',
    help='Duplicates file path'
)

parser.add_argument(
    '-t',
    '--tolerance',
    type=int,
    default=3,
    help='Edit distance tolerance when considering fuzzy matches'
)


def run():
    """Entry point to application"""
    args = parser.parse_args()

    fuzzy = FuzzySearcher(args.tolerance)

    with CsvDataSource(args.input_csv) as datasource:
        with DuplicateWriter(args.output) as output:
            results = DataCleanser(datasource, fuzzy, output).process()

            print(f"total records: {results.total}")
            print(f"unique records: {results.unique}")
            print(f"different people: {results.different}")
