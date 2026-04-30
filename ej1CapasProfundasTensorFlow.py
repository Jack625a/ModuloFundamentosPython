#Paso 1. Importacion librerias
import tensorflow as tf
import numpy as np

#Crear un modelo para predecir el rendimiento de estudiantes
#segun la cantidad de horas de estudio
#hora  rendimiento
# -1     bajo
#  0    medio
#  1    Alto
#Paso 2. Datos
horasEstudioX=np.array([1,2,3,4,5,6,7,8,9,10,11], dtype=float)
rendimientoY=np.array([-1,-1,-1,-1,0,0,0,1,1,1,1], dtype=float)

#Paso 3. Normalizacion
horasEstudioX=horasEstudioX.reshape(-1,1)
horasEstudioX=(horasEstudioX-6)/2

#Paso 4. Creacion del modelo profundo
modelo=tf.keras.Sequential([
    tf.keras.layers.Dense(32, activation="relu", input_shape=(1,)),
    tf.keras.layers.Dropout(0.20),
    tf.keras.layers.Dense(16,activation="relu"),
    tf.keras.layers.Dense(8,activation="relu"), #CAPA PROFUNDA
    tf.keras.layers.Dense(4,activation="relu"),
    tf.keras.layers.Dense(1,activation="tanh")
])

#Paso 5. Compilar el modelo
modelo.compile(
    optimizer="adam",
    loss="mean_squared_error",
    metrics=["accuracy"]
)

modelo.fit(horasEstudioX,rendimientoY, epochs=300)

#Paso 6. Probar
nuevasHoras=np.array([7.5], dtype=float)
nuevasHoras=nuevasHoras.reshape(-1,1)
nuevasHoras=(nuevasHoras-6)/2

prediccion=modelo.predict(nuevasHoras)
print("Resultado es ", prediccion[0][0])


modelo.save("CapasProfundasMachineLearning.h5")