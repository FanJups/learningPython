import numpy as np

y = np.ones((8,1), dtype=int)



I = np.eye(8, dtype=int)

E = np.array([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]])



X = I+E




b, residues, rank, s = np.linalg.lstsq(X, y,rcond=None)



D= np.dot(X,X.T)

F = D - I

r = np.linalg.matrix_rank(F)

print(r)

