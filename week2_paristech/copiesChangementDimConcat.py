import numpy as np

import antigravity



A = np.array([[0,2],[3,4]])

print(A)

B = A # assignation sans copie

# B = A.copy() # assignation avec copie

B[0,0]=10 # changer B affecte A

print(B)

print(A)

C = np.array([[1,2],[3,4]])

print(C)

n,m = C.shape

print(n,m)

D = C.reshape((n*m,1))

print(D.shape)

print(D)

print(C)

print(np.tile(C,(1,2))) # répéter la matrice 2 fois

E = np.array([[5,6]])

print(E)

print(np.concatenate((C,E),axis=0))

print(np.vstack((C,E)))

print(np.concatenate((C,E.T),axis=1))

print(np.hstack((C,E.T)))




