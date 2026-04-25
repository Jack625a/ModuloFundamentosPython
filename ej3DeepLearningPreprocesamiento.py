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
from tensorflow.keras.callbacks import EarlyStopping

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
    tf.keras.layers.Dense(16,activation="relu", input_shape=(4,)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(8,activation="relu"),
    #tf.keras.layers.Dense(8,activation="relu"),
    tf.keras.layers.Dense(1,activation="tanh")
])

#Compilar el modelo
#Tasa de aprendizaje
#0.01 (rapido ) - 0.001( mas estable)
modelo.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss="mean_squared_error"
)
pausaAutomatica=EarlyStopping(
    monitor="val_loss",
    patience=20,
    restore_best_weights=True
)

entrenar=modelo.fit(
    x,y,
    epochs=400,
    validation_split=0.2,
    callbacks=[pausaAutomatica]
)

#Visualizacion de los datos 
plt.plot(entrenar.history["loss"])
plt.plot(entrenar.history["val_loss"])
plt.legend("Entrenamiento","Validacion")
plt.xlabel("Epocas")
plt.ylabel("Error")
plt.show()


#NUEVOS DATOS
nuevoDatos=np.array([
    [7,80,7,3],
    [3,60,5,7],
    [9,70,8,2],
    [11,85,9,1],
    [2,90,1,10],
    [18,90,10,10]
],dtype=float)

#Normalizar los nuevos datos
nuevaNormalizacion=normalizar.transform(nuevoDatos)

#Prediccion 
prediccion=modelo.predict(nuevaNormalizacion)

#Interpretacion de los resultados
for datos, p in enumerate(prediccion):
    print(f"Estudiante {datos+1}: {p[0]:.3f}")
    if p[0]<-0.3:
        print("Rendimiento Bajo")
    elif -0.3<=p[0]<=0.3:
        print("Rendimiento Medio")
    else:
        print("Rendimiento Alto")

modelo.save("modeloRendimiento_Estudiante.h5")