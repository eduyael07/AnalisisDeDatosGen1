import numpy as np

#Ejercicio 1 - Arreglo de ceros
arregloCeros = np.zeros((3,4))
print(arregloCeros)

#Ejercicio 2- Suma de elementos:
arr1 = np.array([1, 2, 3, 4, 5])
print("\nSuma de los elementos: ", np.sum(arr1))

#Ejercicio 3 - Encontrar el máximo y mínimo:
array = np.array([10, 20, 30, 40, 50])
print(f"\nEl valor maximo del arreglo es {np.max(array)} y el valor minimo es {np.min(array)}")

#Ejercicio 5 - Generar números aleatorios:
arrAleatorio = np.random.rand(5)
print(f"\nArray aleatorio: {arrAleatorio}")

#Ejercicio 6 - Promedio de un array:
arrPromedio = np.arange(5,30,5)
print("\nEl promedio del arreglo es: ", np.mean(arrPromedio))

#Ejercicio 7 - Concatenar dos arrays
A = np.array([1,2,3])
B = np.array([4,5,6])
print("\nEl arreglo concatrnado es: ", np.concatenate((A,B)))

#Ejercicio 8 - Reshape de un Array
arreglo = np.arange(1,7)
print("\nArreglo modificado: \n", arreglo.reshape((2,3)))

#jercicio 9 - Producto punto (dot product):
a = np.arange(1,4)
b = np.arange(4,7)
print(f"\n El producto punto entre el arreglo {a} y {b} es: {np.dot(a,b)}")

#Ejercicio 10 - Reorganizar un array:
arrrrr = np.arange(1,11)
print("\n Arreglo reorganizado:\n ", arrrrr.reshape((2,5)))

#Ejercicio: Cálculo de ROI (Retorno de Inversión)
inversiones = np.array([1000, 1500, 2000])
retornos = np.array([1200, 1650, 1800])

def ROI(i):
    inversion = inversiones[i]
    retorno = retornos[i]
    resultado = (retorno - inversion) / (inversion * 100)
    print( resultado)

for i in range(len(inversiones)):
    ROI(i)

#Ejercicio: Normalización de Datos
dataset = np.array([250, 320, 150, 500, 210])

def normalizar(data):
    normalizacion = (data - np.min(dataset)) / (np.max(dataset) - np.min(dataset))
    print(normalizacion)

for i in range(len(dataset)):
    data = dataset[i]
    normalizar(data)


#Ejercicio: Filtrado de Datos
ventas = np.array(([1200, 0, 750, 2400, 0, 1800]))
promedio = np.mean(ventas[ventas != 0])

ventas[ventas == 0] = promedio

print(f"Las ventas fueron {ventas}")

#Ejercicio - Análisis de Presión Arterial
presion = np.array([120, 135, 140, 118, 150, 130, 160, 125, 142, 128, 87])
print(f"La media es {np.mean(presion)}")
print(f"La desviacion estandar es {np.std(presion)}")
presionesRaras = presion[(presion>140) | (presion<90)]
print(f"Estas presiones estan fuera del rango normal: {presionesRaras}")


#Ejercicio - Cálculo del PIB per Cápita
pib = np.array([500, 320, 700, 450])
poblacion = np.array([10, 8, 12, 9])

pibPerCapita = pib/poblacion

print(f"El pib per capita de cada pais es {pibPerCapita} y el valor mas alto es {np.max(pibPerCapita)}")

#Ejercicio - Sistema de Drops (Probabilidades)
import numpy as np

# Valores posibles y sus probabilidades
valores = [0, 1, 2, 3]
probabilidades = [0.5, 0.3, 0.15, 0.05]

drops = np.random.choice(valores, size=100, p=probabilidades)
artefactos = len(drops[drops == 3])   

print("Cantidad de artefactos obtenidos:", artefactos)


