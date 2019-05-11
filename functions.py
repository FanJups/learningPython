# -*- coding: utf-8 -*-
"""
Created on Sat May 11 01:49:02 2019

@author: Admin
"""

def fonction0():
    print("test")
    
fonction0()

def fonction1(s):
    """
    Affichage d'une chaîne et de sa longueur
    """
    print("%s est de longueur %d" % (s,len(s)))
    
help(fonction1)

fonction1([1,2,3])

fonction1("test")

print(fonction1("test"))


def square(x):
    return x**2

print(square(4))

def powers(x):
    """
    Retourne les premières puissances de x
    """
    
    return x**2,x**3,x**4

out = powers(3)

print(type(out))
print(len(out))
print(out[1])

x2,x3,x4 = out
print(x2,x3)

def ma_fonction(x,p=2,debug=False):
    if debug:
        print("evalue ma_fonction avec x = %s"
              "et l'exposant p =%s " % (x,p))
    return x**p

ma_fonction(5)

print(ma_fonction(5,3,True))


def fonctionl(l):
    l +=l
    return None
a=[1,2]
fonctionl(a)
print (a)


def fonctionl_modifie(l):
    l =list(l)
    l+=l
    return None

a=[1,2]
fonctionl_modifie(a)
print (a)



















