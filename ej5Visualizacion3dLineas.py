import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x=[1,2,3,4]
y=[2,3,4,5]
z=[5,9,10,3]

figura=plt.figure()
grafica=figura.add_subplot(111,projection="3d")

grafica.plot(x,y,z)

grafica.set_title("Lineas 3D")
grafica.set_xlabel("x")
grafica.set_ylabel("y")
grafica.set_zlabel("z")

plt.show()