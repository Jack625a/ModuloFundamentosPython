#CREAR UN MODELO DEEP LEARNING PARA 
#PREDECIR EL RENDIMIENTO DE UN ESTUDIANTE
#DATOS 5:
#horas de estudio
#asistenciaClases
#nivelesSueño
#usoCelular

import tensorflow as tf
import numpy as np
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
    [8,54,8,7]
], dtype=float)

y=np.array([-1,-1,-1,0,0,1,1,1])

#Normalizacion

#Horas Estudio
x[:,0]=(x[:,0]-4.5)/2

#Asistencia
x[:,1]=(x[:,1]-58.5)/100

#niveles Sueño
x[:,2]=(x[:,2]-6.5)/10

#usoCelular

x[:,3]=(x[:,3]-6)/10

#Creacion del modelo
modelo=tf.keras.Sequential([
    tf.keras.layers.Dense(32,activation="relu",input_shape=(4,)),
    tf.keras.layers.Dense(16,activation="relu"),
    tf.keras.layers.Dense(8,activation="relu"),
    tf.keras.layers.Dense(1,activation="tanh")
])

modelo.compile(
    optimizer="adam",
    loss="mean_squared_error"
)

analisis=modelo.fit(x,y,epochs=300,verbose=0, validation_split=0.2)

#PROBAR EL MODELO

#NUEVOS DATOS
nuevoDatos=np.array([
    [7,80,7,3],
    [3,60,5,7],
    [9,70,8,2],
    [11,85,9,1],
    [2,90,1,10],
    [18,90,10,10]
],dtype=float)

#normalizar
nuevoDatos[:,0]=(nuevoDatos[:,0]-4.5)/2
nuevoDatos[:,1]=(nuevoDatos[:,1]-58.5)/100
nuevoDatos[:,2]=(nuevoDatos[:,2]-6.5)/10
nuevoDatos[:,3]=(nuevoDatos[:,3]-6)/10

prediccion=modelo.predict(nuevoDatos)

print(prediccion)


plt.plot(analisis.history["loss"])
plt.plot(analisis.history["val_loss"])
plt.legend(["Entrenamiento/Validacion"])
plt.show()

