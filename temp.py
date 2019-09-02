# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 17:33:45 2019

@author: yuasa
"""

f = open('00.txt')
lines = f.readlines()[:2]
l1 = lines[0].split('\t')
l2 = lines[1].split('\t')
for a,b in zip(l1,l2):
    print(a,':',b)