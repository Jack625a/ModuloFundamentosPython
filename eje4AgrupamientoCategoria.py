import pandas as pd
import matplotlib.pyplot as plt

dataFrame=pd.read_csv("estudiantes.csv")

dataFrame.pivot(index="Nombre",columns="Carrera",values="Nota").plot(kind="bar")
plt.title("Notas por estudinate y carreras")
plt.ylabel("Nota")

plt.show()