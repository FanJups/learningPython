# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:24:57 2019

@author: Admin
"""

class Point(object):
    """
    Classe pour représenter un point dans le plan
    """
    
    def __init__(self,x,y):
        """
        Création d'un nouveau point en position x,y
        """
        
        self.x=x
        self.y=y
        
    def translate(self,dx,dy):
        """
        Translate le point de dx and dy
        """
        
        self.x += dx
        self.y += dy
        
    def __str__(self):
        return "Point: [%f,%f] " % (self.x,self.y)
    
p = Point(x=0,y=0)
print(p.x)
print(p.y)
print("%s" % p)

p = Point(1,1)
p.translate(0.25,1.5)
print(p)

def ma_fonction(arg):
    if not isinstance (arg,list):
        raise Exception ("arg doit être de type list")
    print(arg)
    


try:
    ma_fonction("A")
    print("OK")
except:
    print("Exception interceptée")
    
try:
    #variable non définie
    print(var)
except Exception as e:
    print("Exception interceptée: %s" % e)
    






















        
        