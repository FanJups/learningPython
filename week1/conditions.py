# -*- coding: utf-8 -*-
"""
Created on Sat May 11 00:57:35 2019

@author: Admin
"""

condition1=False
condition2=False

if condition1:
    print("condition1 est vraie")
elif condition2:
    print("condition2 est vraie")
else:
    print("condition 1 & 2 sont fausses")
    
condition1=condition2=True

if condition1:
    if condition2:
        print("condition 1 & 2 sont vraies")
        