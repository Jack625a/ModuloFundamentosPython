import matplotlib.pyplot as plt

meses=[1,2,3,4,5,6,7,8,9,10]
ventas=[600,650,700,750,800,820,850,900,980,1000]

plt.bar(meses,ventas)

plt.title("Ventas por meses")
plt.xlabel("Meses")
plt.ylabel("Ventas")

plt.show()