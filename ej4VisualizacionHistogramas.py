import matplotlib.pyplot as plt

notas=[35,45,48,50,55,60,45,80,100,67]

plt.hist(notas,bins=4)

plt.title("Distribucion de notas")
plt.xlabel("Notas")
plt.ylabel("Frecuencia")

plt.show()