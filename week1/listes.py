# -*- coding: utf-8 -*-
"""
Created on Fri May 10 22:10:20 2019

@author: Admin
"""

l=[1,2,3,4,5,6,7,8]
print(l)
print(type(l))
print(l[0])
print(l[-2])
print(l[1:3])
print(l[::2])

start,stop,step=10,30,2
print(list(range(start,stop,step)))

print(list(range(-10,10)))

#itération de n-1 à 0

n=9

print(list(range(n-1,-1,-1)))

s="zaboda"
l =list(s)
print(l)

l_sorted = sorted(l)
print(l_sorted)

l.sort()

print(l)

# création d'une liste vide

l=[] # ou l=list()

# ajout d'éléments avec append

m=l.append("A")
l.append("d")
l.append("d")

print(m)
print(l)
print(l.count('d'))

l[1]='p'
l[2]='p'

print(l)

l[1:3]=["q","e"]
print(l)

l.insert(3,"w")
print(l)

l.remove("A")

print("y" in l)

print(l.index("w"))

del l[2]
print(l)

l1=[1,2,3]
l2=[4,5,6]
print(l1+l2)
l1.append(l2)
print(l1*2)

help(list)



