import pandas as pd
import matplotlib.pyplot as plt

dataFrame=pd.read_csv("estudiantes.csv")

agrupar=dataFrame.groupby("Carrera")["Nota"].mean()

agrupar.plot(kind="bar")

plt.title("Promedio de notas por carrera")
plt.show()