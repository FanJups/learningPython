import numpy as np
from numpy import  random
import matplotlib.pyplot as plt



a=np.array([1 , 2], dtype=int)

b=np.array([2 , 2], dtype=int)

print(a/b)

a=np.array([1,2],dtype=float)

b=np.array([2,2],dtype=float)

print(a/b)
print(a//b)

# tirage uniforme dans [0,1]


print(random.random_sample((3,3))) # ou random.rand

# tirage suivant une loi normale

print(random.standard_normal((3,3)))  # ou random.randn

a= random.standard_normal(10000)

plt.hist(a,40)

plt.show()

# affichage des tirages comme une image

C = random.standard_normal((32,32))

print(C.shape)

plt.imshow(C,interpolation='nearest')
plt.colorbar()
plt.show()

# création d'un tableau 2D de zeros
A = np.zeros((2,3))
print(A)
print(A.dtype)



print(np.zeros((1,3),dtype=int)) # ligne

print(np.zeros((3,1),dtype=int)) # colonne

print(np.ones((3,3))) # tableau 3*3 de 1

# matrice diagonale

D = np.diag([1,2,3])

print(D)

# extraction de la diagonale

print(np.diag(D))



