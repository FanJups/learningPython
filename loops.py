# -*- coding: utf-8 -*-
"""
Created on Sat May 11 01:05:33 2019

@author: Admin
"""

for x in [1,2,3]:
    print(x)


for x in range(4):
    print(x)
    
s="calcul"

for idx,c in enumerate(s):
    print(idx,c)
    
for idx in range(len(s)):
    print(idx,s[idx])
    
cnt=0
for c in s:
    print(cnt,s[cnt])
    cnt+=1
    
params= {"param1":1.0,
         "param2":2.0,
         "param3":3.0}

for key,value in params.items():
    print("%s = %s"% (key,value))
    
for key in params:
    print(key)
    
l=[x**2 for x in range(0,5)]

print(l)

# est la version courte de 

l=[]
for x in range(0,5):
    l.append(x**2)
    
print(l)

i=0

while i<5:
    print(i)
    i+=1
print("OK")
