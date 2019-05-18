import numpy as np
import matplotlib.pyplot as plt

v = np.array([1,2,3,4])
print(v)

M = np.array([[1,3],[2,4]])

print(M)

print(M.dtype)

# nombre d'octets par élément

print(M.itemsize)

# nombre d'octets

print(M.nbytes)

# nombre d'octets

print(M.nbytes / M.size)

M[0,0]=-1

print(M)

#M[0,0]= "hello"

a = np.array([0,0,0])
print(a.dtype)
a[0]=3.2 # perte de précision
print(a)

b = np.array([0,0,0],dtype=np.complex64)
b[0]=3.2
print(b)

M = np.array([[-1,2],[0,4]])
print(M.dtype)

M2 = M.astype(float)
print(M2)
print(M2.dtype)

M3 = M.astype(bool)
print(M3)
print(M3.dtype)

# utilisation de fonction de génération d'arrays

x = np.array(range(0,10,2))  # à partir d'une liste
print(x)

x = np.arange(0,10,2) # ok : plus efficace

print(x)

x = np.arange(-1,1,0.5) # avec flottants
print(x)

# fonction linspace : le début et la fin sont inclus

d = np.linspace(0,10,6)

print(d)

x = np.linspace(-10,10,100)
y = np.sin(x)
plt.plot(x,y, label = '$y = \sin(x)$')
plt.legend()
plt.show()











