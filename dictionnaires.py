# -*- coding: utf-8 -*-
"""
Created on Sat May 11 00:26:29 2019

@author: Admin
"""

params= {"param1":1.0,
         "param2":2.0,
         "param3":3.0}

print(type(params))
print(params)

print("param2 = %s" % params["param2"])

params["param1"]="A"
params["param2"]="B"

#ajout d'une entrée 

params["param4"]="D"

print("param1 = %s" % params["param1"])
print("param2 = %s" % params["param2"])
print("param3 = %s" % params["param3"])
print("param4 = %s" % params["param4"])

del params["param4"]
print(params)


print("param1" in params)
print("param6" in params)
