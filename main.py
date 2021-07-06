from __future__ import print_function
import sys

n=int(input())
for i in range(1,n+1):
    for j in range(n+1):
        sys.stdout.write(str(j))
    sys.stdout.flush()
