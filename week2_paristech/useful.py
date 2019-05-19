import numpy as np

u = np.array([2,2,1])
v = np.array([2,1,1])

# produit scalaire

print("produit scalaire")
print(np.vdot(u,v))

# produit vectoriel

print("produit vectoriel")
print(np.cross(u,v))

print("Décomposition en valeurs singulières")
M = np.array([[1,2,3],[4,5,6]])

print(M)

U,s,W = np.linalg.svd(M)

print(U)
print(s)
print(W)

print("Reconstruire M")

S = np.zeros((2,3),dtype=float)
S[:2,:2] = np.diag(s)



M_recons = np.dot(np.dot(U,S),W)

print(M_recons)



