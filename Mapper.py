#!/usr/bin/python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")

    if len(line) >=2:
        date = line[0]
        score = line[-1]

        print '%s\t%s' % (date, score)