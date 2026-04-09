#Eje1. Grafico de lineas (TENDENCIAS)
#Paso 1. IMPORTACION
import matplotlib.pyplot as plt

#Paso 2. Creacion u obtencion de datos
meses=[1,2,3,4,5,6,7,8,9,10]
ventas=[600,650,700,750,800,820,850,900,980,1000]

#Paso 3. Crear la grafica de tendencias
plt.plot(meses,ventas,marker='o')

#Paso 4. Personalizacion del grafico
plt.title("Evolución de ventas")
plt.xlabel("Meses")
plt.ylabel("Ventas")

plt.show()