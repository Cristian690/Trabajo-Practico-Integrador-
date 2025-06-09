import random
from faker import Faker
import time

fake = Faker('es')

cant_alumnos = int(input("Ingrese la cantidad de alumnos a generar: "))
buscar_nombre = input("Ingrese el nombre a buscar: ")

# Generador de alumnos
def generar_alumnos(n):
    alumnos = []
    for i in range(1, n + 1):
        nombre_completo = fake.name()
        nota = random.randint(1, 10)
        alumnos.append({'id': i, 'nombre': nombre_completo, 'nota': nota})
    return alumnos

# Mostrar alumnos
def mostrar(lista, titulo):
    print(f"\n{titulo}")
    print("-" * len(titulo))
    for a in lista:
        print(f"{a['id']}. {a['nombre']} - Nota: {a['nota']}")
    print()

# Búsqueda lineal
def buscar_lineal(lista, nombre):
    for a in lista:
        if a['nombre'].lower().startswith(nombre.lower()):
            return a
    return None

# Búsqueda binaria (requiere lista ordenada)
def buscar_binaria(lista, nombre):
    izq, der = 0, len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        nombre_medio = lista[medio]['nombre'].lower()
        if nombre_medio.startswith(nombre.lower()):
            return lista[medio]
        elif nombre.lower() < nombre_medio:
            der = medio - 1
        else:
            izq = medio + 1
    return None

# Ordenamiento por seleccion
def ordenar_seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j]['nombre'].lower() < lista[min_idx]['nombre'].lower():
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista


# Ordenamiento burbuja
def ordenar_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]['nombre'].lower() > lista[j+1]['nombre'].lower():
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# --- PRUEBA ---
alumnos = generar_alumnos(cant_alumnos)  

mostrar(alumnos, "Lista original (desordenada)")

# Medimos tiempo de ordenamiento burbujeo
#print("\nOrdenando con burbujeo...")
inicio_orden = time.time()
ordenados = ordenar_burbuja(alumnos.copy())
fin_orden = time.time()
mostrar(ordenados, "Lista ordenada (por nombre)")
print(f"Tiempo de ordenamiento burbujeo: {fin_orden - inicio_orden:.50e} segundos")

# Medimos tiempo de ordenamiento por selección
#print("\nOrdenando con selección...")
inicio = time.time()
ordenar_seleccion(alumnos)
fin = time.time()
print(f"Tiempo de ordenamiento por selección: {fin - inicio:.50e} segundos")


# Medimos búsqueda lineal
inicio_lineal = time.time()
encontrado_lineal = buscar_lineal(ordenados, buscar_nombre)
fin_lineal = time.time()
print(f"Búsqueda lineal encontró: {encontrado_lineal}")
print(f"Tiempo: {fin_lineal - inicio_lineal:.50e} segundos")

# Medimos búsqueda binaria
inicio_binaria = time.time()
encontrado_binaria = buscar_binaria(ordenados, buscar_nombre)
fin_binaria = time.time()
print(f"Búsqueda binaria encontró: {encontrado_binaria}")
print(f"Tiempo: {fin_binaria - inicio_binaria:.50e} segundos")
