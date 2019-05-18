import numpy as np

"""

data = np.genfromtxt('data.csv',delimiter = ',')
print(data)

print(data.shape)

M = np.random.standard_normal((3,3))

print(M)

np.savetxt("random-data.csv",M,fmt='%2.3f',delimiter=',')

randomData = np.genfromtxt('random-data.csv',delimiter = ',')


#print(randomData)

np.save("random-matrix.npy",M)

x=np.load("random-matrix.npy")

print(x)

"""

v = np.array([1,2,3,4])

M = np.array([[1,3],[2,4]])

# v ndarray à 1 dimension -> un indice
print(v[0])

# M ndarray à 2 dimensions -> 2 indices
print(M[0,1])

print(M[0]) # la 1ère ligne

print(M[1,:]) # 2ème ligne indice 1

print(M[:,1]) # 2ème colonne indice 1

M[1,:] = -1 # assigne un élément à toute une ligne

print(M)

M[:,1] = [5,6] # assignement de plusieurs éléments
print(M)

# slicing

# start:stop:step

A = np.array([1,2,3,4,5])
print(A)

print(A[1:3])

print(A[::])

print(A[::2]) # step = 2

print(A[:3]) # les 3 premiers éléments

print(A[3:]) # à partir de l'indice 3

print(A[-1])  # le dernier élément

print(A[-3:]) # les 3 derniers éléments

# slicing sur les tableaux multidimensionnels

B = np.array([[n + m*10 for n in range(4)] for m in range(4)])

print(B)

# un bloc du tableau

print(B[1:3,1:3])

print(B[::2,::2]) # une ligne sur 2 et une colonne sur 2

print(B)

indices =[1,3]

print(B[indices]) # lignes d'indice 1 et 3

print(B[:,indices]) # colonnes d'indice 1 et 3

# éléments d'indices [0,1] et [2,3]

print(B[[0,2],[1,3]])

# sous tableaux lignes [0,1]  et colonnes [2,3]

print(B[np.ix_([0,2],[1,3])])

tab = np.arange(5)

print(tab)

mask = np.array([True,False,True,False,False])

print(tab[mask])

print(tab[[0,2]])

print(tab>2)

print(tab[tab>2])



























