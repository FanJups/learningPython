
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler

from sklearn.preprocessing import StandardScaler



Z = np.genfromtxt('winequality-white.csv',dtype=float,delimiter = ';',skip_header=1,usecols = (0,1,2,3,4,5,6,7,8,9,10))

y = np.genfromtxt('winequality-white.csv',dtype=float,delimiter = ';',skip_header=1,usecols = (11))

b, residues, rank, s = np.linalg.lstsq(Z, y,rcond=None)



#print(residues)

print(Z)

print("----------------------------------")



std_scaler = StandardScaler().fit(Z)
X = std_scaler.transform(Z)

b2, residues2, rank2, s2 = np.linalg.lstsq(X, y,rcond=None)



print(residues2)


