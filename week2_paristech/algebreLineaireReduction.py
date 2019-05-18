import numpy as np

B = np.array([[n + m*10 for n in range(4)] for m in range(4)])

print(B)

print(B.T) # transposition

C = (B + B.T) / 2 # addition terme à terme

print(C)


print(np.trace(B)) # trace de B

print(B.shape)

print(B*B) # multiplication élément par élément

print(np.dot(B,B)) # multiplication de matrices

print("---------------------------------------------------------------")

# inversion de matrice

D = np.random.standard_normal((3,3))

print(D)

Dinv = np.linalg.inv(D)

print(Dinv)

print("---------------------------------------------------------------")

print(np.dot(D,Dinv))

print("--------------------------REDUCTION-------------------------------------")

print(np.sum(B)) # somme de tous les éléments

 # somme de la 2ème ligne

print(np.sum(B[1,:]))

# somme de toutes les lignes


print(np.sum(B,axis=1))

# somme de toutes les colonnes


print(np.sum(B,axis=0))

print("--------------------------REDUCTION - moyenne-------------------------------------")

print(np.mean(B)) # moyenne de tous les éléments

 # moyenne de la 2ème ligne

print(np.mean(B[1,:]))

# moyenne de toutes les lignes


print(np.mean(B,axis=1))

# moyenne de toutes les colonnes


print(np.mean(B,axis=0))

# maximum de toutes les colonnes

print(np.max(B,axis=0))









