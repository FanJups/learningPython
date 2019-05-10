# -*- coding: utf-8 -*-
"""
Created on Fri May 10 21:22:09 2019

@author: Admin
"""

s='Bonjour Telecom ParisTech'
# ou avec " "
s="Bonjour Telecom ParisTech"
print(s)
print(type(s))
print(s[0])
print(s[-1])

start,stop =1,7
print(s[stop])
print(s[start:stop])
print(len( s[start:stop]))
print(stop-start)

test ="abcdefghijlopmn"
print(test[0:3])

print(test[:7])

print(s[:7])

print(s[8:])

print(len( s[8:]))

print(s[-10:])

s="ababababab"

#slicing

print(s[0::2])

print(s[1::2])

print("str1",1.0,False,-6j)

print("str1"+"str2"+"str3")

a=1.0

print("val = %e" % a)
print("val = %f" % a)
print("val = %s" % a)

s="val1 = %.2f, val2 = %d" % (3.1415,1.5)

print(s)


