import matplotlib.pyplot as plt

datos=[25,15,40,12,8]
lenguajes=["Java","C++","Python","Kotlin","PHP"]
plt.pie(datos,labels=lenguajes,autopct="%1.1f%%")

plt.title("LENGUAJES MAS USADOS")
plt.show()