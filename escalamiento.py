from sklearn.preprocessing import StandardScaler
import joblib
import numpy as np

#Datos
x=np.array([
    [1,56,5,5],
    [2,67,6,5],
    [3,85,6,6],
    [4,58,7,6],
    [5,59,6,3],
    [6,58,5,5],
    [7,53,7,2],
    [8,54,8,7],
    [4,88,7,2],
    [9,90,7,1]
], dtype=float)

y=np.array([-1,-1,-1,0,0,1,1,1,-1,1])

#Aplicar la normalizacion
normalizar=StandardScaler()
x=normalizar.fit_transform(x)

joblib.dump(normalizar,"escala.pkl")