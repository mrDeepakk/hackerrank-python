import math
import os
import random
import re
import sys
from datetime import*

def time_delta(t1, t2):
    # Sun 10 May 2015 13:54:36 -0700
    # %a %d %b %Y %H:%M:%S %z
    first=datetime.strptime(t1,"%a  %d %b  %Y   %H:%M:%S %z")
    second=datetime.strptime(t2,"%a  %d %b  %Y   %H:%M:%S %z")
    
    return str(abs(int((first-second).total_seconds())))   
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
