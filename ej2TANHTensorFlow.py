#Modelo de tipo clasificatorio
#CLASIFICADOR DEL ESTADO DE LA TEMPERATURA
#5 = FRIO = -1
#10 =FRIO = -1
#15 = TEMPLADO = 0
#20 = CALIENTE = 1
#25 = CALIENTE= 1
import tensorflow as tf
import numpy as np

temperaturaX=np.array([5,10,15,20,25],dtype=float)
escalaY=np.array([-1,-1,0,1,1],dtype=float)

#normalizando los datos
temperaturaX=temperaturaX.reshape(-1,1)
temperaturaX=(temperaturaX-15)/10

modelo=tf.keras.Sequential([
    tf.keras.layers.Dense(10,activation="tanh",input_shape=(1,)),
    tf.keras.layers.Dense(1,activation="tanh")
])

modelo.compile(
    optimizer="adam",
    loss="mean_squared_error"
)

modelo.fit(temperaturaX,escalaY,epochs=300)

nuevaTemperatura=np.array([18],dtype=float)
nuevaTemperatura=nuevaTemperatura.reshape(-1,1)
nuevaTemperatura=(nuevaTemperatura-15)/10

prediccion=modelo.predict(nuevaTemperatura)
print("Resultado ",prediccion[0][0])





#Modelo de tipo regresion