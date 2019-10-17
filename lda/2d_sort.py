#!/usr/bin/env python3

from operator import itemgetter

a = [ [1, 6, 3], 
      [7, 9, 0],
      [4, 8, 5],
    ]


a.sort(key=itemgetter(2), reverse=True)

print(a)

