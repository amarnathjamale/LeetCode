#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the 'calen' function below.
#
# The function accepts TUPLE datetuple as parameter.
#
import calendar
def usingcalendar(datetuple):
    # Write your code here
    lst = []
    year = datetuple[0]
    month = datetuple[1]
    date = datetuple[2]
    if (year % 4) == 0: 
        month = 2 
        
    print(calendar.month(year, month))
    
    cal= calendar.Calendar()

    a = cal.itermonthdates(year, month)
    print(type(a))

if __name__ == '__main__':
    qw1 = []

    for _ in range(3):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)
        
    tup=tuple(qw1)

    usingcalendar(tup)

