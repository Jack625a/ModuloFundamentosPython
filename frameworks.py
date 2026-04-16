import tensorflow as tf
import numpy as np

#entradas
x=np.array([1,2,3,4],dtype=float)
y=np.array([3,5,7,9], dtype=float)

#Modelo 
modelo=tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

#Compilado del modelo
modelo.compile(
    optimizer='sgd',
    loss="mean_squared_error"
)

#Entrenar el modelo
modelo.fit(x,y,epochs=10)

print(modelo.predict([7]))