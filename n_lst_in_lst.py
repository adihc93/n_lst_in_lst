# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 17:32:07 2018
Accessing items list within list n nesting
@author: HP
"""


def accessor(lst):
    for i in range(0, len(lst)):
        if type(lst[i])==int or type(lst[i])==float or type(lst[i])==str:
            print(lst[i])
        else:
            accessor(lst[i])
            
lst=[4, (2,3,[2,3,4],6), 7,5, 4.5, [6,2,4,['lk',4,5,(75,'ll')]], 'aditya', 7] #list contains a combination of int, float, str, list and tuple

accessor(lst)