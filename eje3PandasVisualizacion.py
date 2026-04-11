import pandas as pd
import matplotlib.pyplot as plt

#Cargar los datos
dataFrame=pd.read_csv("estudiantes.csv")

print(dataFrame)
promedioNotas=dataFrame["Nota"].mean()
print(promedioNotas)


dataFrame.plot(x="Carrera",y="Nota", kind="bar",title="Notas estudiantes")
plt.axhline(promedioNotas, linestyle="--",label="Promedio Notas")

plt.legend()
plt.show()