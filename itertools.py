#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'usingiter' function below.
#
# The function is expected to return a TUPLE.
# The function accepts following parameters:
#  1. TUPLE tupb
#
import itertools
import operator
def performIterator(tuplevalues):
    # Write your code here
    mylistx = []
    mylisty = []
    list1 = []
    count = 0
    
    for i in tuplevalues:
        count+=1
        if count==1:
            y = itertools.cycle(i)
            for b in range(4):
                list1.append(next(y))
            g=tuple(list1)
            mylistx.append(g)
        if count==2:
          z=tuple(itertools.repeat(i[0],len(i)))
          mylistx.append(z)
        if count==3:
          y=itertools.accumulate(i,operator.add)
          mylistx.append(tuple(y))
        if count==4:
            list1=[]
            list2=[]
            for j in tuplevalues:
                for k in j:
                    list1.append(k)
            w=tuple(list1)
            mylistx.append(w)
            for z in w:
                if z%2!=0:
                    list2.append(z)
            t=tuple(list2)
            mylistx.append(t)
    return tuple(mylistx)

    

if __name__ == '__main__':

    length = int(input().strip())

    qw1 = []
    for i in range(4):
        qw2 = []
        for _ in range(length):
            qw2_item = int(input().strip())
            qw2.append(qw2_item)
        qw1.append(tuple(qw2))
    tupb = tuple(qw1)

    q = performIterator(tupb)
    print(q)
