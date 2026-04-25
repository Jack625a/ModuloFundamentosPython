#CREAR UN MODELO DEEP LEARNING PARA 
#PREDECIR EL RENDIMIENTO DE UN ESTUDIANTE
#DATOS 5:
#horas de estudio
#asistenciaClases
#nivelesSueño
#usoCelular

import tensorflow as tf
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

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

#Crear el modelo
modelo=tf.keras.Sequential([
    tf.keras.layers.Dense(32,activation="relu", input_shape=(4,)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(16,activation="relu"),
    tf.keras.layers.Dense(8,activation="relu"),
    tf.keras.layers.Dense(1,activation="tanh")
])

#Compilar el modelo
modelo.compile(
    optimizer="adam",
    loss="mean_squared_error"
)

entrenar=modelo.fit(
    x,y,
    epochs=300,
    validation_split=0.2,
    verbose=1
)

#Visualizacion de los datos 
plt.plot(entrenar.history["loss"])
plt.plot(entrenar.history["val_loss"])
plt.legend("Entrenamiento","Validacion")
plt.xlabel("Epocas")
plt.ylabel("Error")
plt.show()