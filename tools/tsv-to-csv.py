#!/usr/bin/python

import sys
import csv
from os.path import basename

if __name__ == "__main__":
    in_file = sys.argv[1]
    out_file = basename(('.').join(in_file.split('.')[:-1])) + ".csv"
    in_tsv = csv.reader(open(in_file, "rb"), delimiter = '\t')
    out_csv = csv.writer(open(out_file, 'wb'))

    out_csv.writerows(in_tsv)



