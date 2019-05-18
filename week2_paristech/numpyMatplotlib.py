

import numpy as np
import matplotlib.pyplot as plt

# un vecteur à partir d'une liste python

v = np.array([1,2,3,4])
print(v)
print(type(v))

#plt.figure()
#plt.plot(v)
#plt.show()

x = np.array([0,2,4,6])
plt.figure()
plt.plot(x,v,'r--',label='vecteur')
plt.xlabel('x')
plt.ylabel('v')
plt.title('Exemple titre')
plt.legend(loc='lower right')
plt.show()

# une matrice : l'argument est une liste emboîtée

M=np.array([[1,3],[2,4]])

print(M)

# accéder à un élément

print(M[0,0])

print(M[1,1])

# type

print(type(M))

# taille

print(v.shape)

print(M.shape)

# type de la taille

print(type(M.shape))

print(type(v.shape))

# dimensions

print(v.ndim)

print(M.ndim)

# nombre d'éléments ( différent de shape qui est la taille)

print(v.size)

print(M.size)

T = np.array([[[1,2,3,4]]])

print(T)

print(T.shape)

print(T.ndim)

print(T.size)



print(np.size(T))