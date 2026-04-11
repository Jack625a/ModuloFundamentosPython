import pandas as pd

datos={
    "Lenguaje":["Python","c++","Java","JavaScript"],
    "Uso":[20,10,15,18]
}

tabla=pd.DataFrame(datos)
print(tabla)