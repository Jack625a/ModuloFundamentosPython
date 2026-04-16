#Modelo de clasificacion para notas de estudiantes
#APROBAR O REPORBAR

#PASO 1. IMPORTAR LAS LIBRERIAS
import tensorflow as tf
import numpy as np

#Paso 2. CREAR LOS DATOS
notas=np.array([30,35,45,50,60,70,80,90,95], dtype=float)
#etiquetas
#1 APROBAR 0 REPROBAR
etiquetas=np.array([0,0,0,0,1,1,1,1,1], dtype=float)

#Paso3. Normalizar las notas
notas=(notas-50)/10

#Paso 4.Crear el modelo
modelo=tf.keras.Sequential([
    tf.keras.layers.Dense(1,activation="sigmoid",input_shape=(1,))
])

#Paso 5. Compilar el modelo
modelo.compile(
    optimizer="adam",
    loss="binary_crossentropy"
)

#Paso 6. Entrenar Modelo
modelo.fit(
    notas,
    etiquetas,
    epochs=90
        )

#Paso 7. Probar el modelo
nuevosNotas=np.array([45,55,90],dtype=float)
nuevosNotas=(nuevosNotas-50)/10

prediccion=modelo.predict(nuevosNotas)

print("RESULTADOS")
for nt, pred in zip([45,55,90],prediccion):
    print(f"Nota {nt} => Probabilidad {pred[0]:.3f}")