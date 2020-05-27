# Datashedder

A tool to pass a technical test

## Approach

It's a python package with a single dependency on "python-Levenshtein"

python-Levenshtein is a wrapper around a C library which provides functions to calculate the  
Levenshtein distance between two strings.

That difference is the number of single character inplace edits, removals or additions required to 
get from __string a__ -> __string b__

The Levenshtein between "Wilyam Premadasta" and "William Premadasa" is 3 which is the default
tolerance setting when running the application.

## Performance

Perfmance is pretty bad, it's a trixy problem, I'd consider replacing python-Levenshtein with Lucene.

Or buying a copy of https://www.amazon.co.uk/Data-Matching-Techniques-Data-Centric-Applications/dp/3642430015 
to look for tips and tricks to squeeze performance out

```bash
time datashedder ./samples/complex.csv
total records: 11122
unique records: 10993
different people: 8047

real    0m27.826s
user    0m27.767s
sys     0m0.052s
```


## Install steps

Assuming you don't want to install globally as this is a tech test let's make a venv

```bash
# Maybe python3 is just python on your system, alter as necessary
$ python3 -m venv venv
# And activate it
$ source venv/bin/activate
$ pip install wheel
# If you want to run tests and tox is missing globally
$ pip install tox
# And finally install this project
$ pip install .
```

## Usage (assumes install steps followed)

The tech test source file is provided as a convenience in the samples directory

```bash
$ datashedder ./samples/complex.csv
```

This will report csv errors on stderr, and stats on stdout along with producing a 
csv at ./relateddata.csv

You can alter the output filename, and fuzzyness tolerance (integer representing edit distance considered duplicate)

```bash
usage: datashedder [-h] [-o OUTPUT] [-t TOLERANCE] input_csv

positional arguments:
  input_csv             Path to csv file to process

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Duplicates file path
  -t TOLERANCE, --tolerance TOLERANCE
                        Edit distance tolerance when considering fuzzy matches
```

## Running the tests (assumes install steps followed)

run tests with

```bash
$ tox
```
