#Ejercicio Regresiones
#Crear un modelo que prediga el salario de un empelado segun los años de experiencia

#PASO 1. IMPORTAR LAS LIBRERIAS
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#PASO 2. CARGADO DE DATOS
añosX=np.array([1,2,3,4,5,6,7,8,9],dtype=float)
salarioY=np.array([1000,1500,2000,2500,3000,3500,4000,4500,5000],dtype=float)

#PASO 3 APLICAR UNA NORMALIZACION
añosX=añosX.reshape(-1,1)

#PASO 4. CREACION DEL MODELO
modelo=tf.keras.Sequential([
    tf.keras.layers.Dense(10,activation="relu"),
    tf.keras.layers.Dense(1)
])

#PASO 5. COMPILAR EL MODELO
modelo.compile(
    optimizer="adam",
    loss="mean_squared_error"
)

#PASO 6. ENTRENAR EL MODELO
modelo.fit(añosX,salarioY,epochs=300, verbose=0)

#PASO 7. REALIZAR UNA PREDICCION
resultado=modelo.predict(np.array([[20]],dtype=float))
print(resultado)
print("SALARIO ESTIMADO: ",resultado[0][0]*1000)

#PASO 8. GRAFICAR EL RESULTADO
xLinea=np.linspace(1,10,100).reshape(-1,1)
yPrediccion=modelo.predict(xLinea)

plt.scatter(añosX,salarioY)
plt.plot(xLinea,yPrediccion)
plt.show()