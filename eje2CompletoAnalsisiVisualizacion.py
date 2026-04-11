import pandas as pd
import matplotlib.pyplot as plt

#data
data={
    "meses":["2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2021","2022","2023","2024"],
    "ventas":[700,850,900,600,680,720,698,780,795,500,850,890,680,785,900,685,750,860,865,900,990,752,690,800]
}
#Conversion de datos a DataFrame
dataFrame=pd.DataFrame(data)

print(dataFrame)

#Calcular el promedio
promedio=dataFrame["ventas"].mean()

#Desviacion estandar
desviacion=dataFrame["ventas"].std()
ventaMinima=dataFrame["ventas"].min()
ventaMayor=dataFrame["ventas"].max()

print("Promedio de Ventas: ",promedio)
print("Desviacion Estandar: ",desviacion)

#Graficar
plt.plot(dataFrame["meses"],dataFrame["ventas"],marker="o",label="Ventas",color="green")

plt.axhline(y=promedio,linestyle="--",label=f"Prom:{promedio:.2f}",color="orange")
plt.axhline(y=promedio+desviacion,linestyle=":",label="Desviacion +")
plt.axhline(y=promedio-desviacion,linestyle=":", label="Desviacion -",color="red")
plt.fill_between(dataFrame["meses"],promedio,promedio+desviacion,alpha=0.3,label="Zona Optima")
plt.fill_between(dataFrame["meses"],promedio,promedio-desviacion,alpha=0.3,label="Zona Normal",color="yellow")
plt.fill_between(dataFrame["meses"],promedio-desviacion,ventaMinima,alpha=0.3,color="red",label="Zona Perdida")
plt.fill_between(dataFrame["meses"],promedio+desviacion,ventaMayor,alpha=0.3,color="green",label="Zona Ganancia")


#Muestra del valor de la grafica
plt.text(0,promedio, f"Prom:{promedio:.2f}")

plt.title("Ventas Mensuales con promedio")
plt.xlabel("Meses")
plt.ylabel("Ventas")
plt.legend()
plt.grid()

plt.show()