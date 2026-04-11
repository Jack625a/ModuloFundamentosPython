import pandas as pd
import matplotlib.pyplot as plt

#data
data={
    "meses":["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
    "ventas":[700,850,900,600,680,720,698,780,795,800,850,890]
}
#Conversion de datos a DataFrame
dataFrame=pd.DataFrame(data)

print(dataFrame)

#Calcular el promedio
promedio=dataFrame["ventas"].mean()
print("Promedio de Ventas: ",promedio)

#Graficar
plt.plot(dataFrame["meses"],dataFrame["ventas"],marker="o",label="Ventas")

plt.axhline(y=promedio,linestyle="--")

#Muestra del valor de la grafica
plt.text(0,promedio, f"Prom:{promedio:.2f}")

plt.title("Ventas Mensuales con promedio")
plt.xlabel("Meses")
plt.ylabel("Ventas")
plt.legend()
plt.grid()

plt.show()