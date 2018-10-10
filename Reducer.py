#!/usr/bin/python
#Reducer.py
import sys

date_score = {}

#Partitoner
for line in sys.stdin:
    line = line.strip()
    date, score = line.split('\t')

    if date in date_score:
        date_score[date].append(float(score))
    else:
        date_score[date] = []
        date_score[date].append(float(score))

#Reducer
for date in date_score.keys():
    ave_score = sum(date_score[date])*1.0 / len(date_score[date])
    print '%s\t%s'% (date, ave_score)