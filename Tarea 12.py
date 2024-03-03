import numpy as np

# Crear una matriz 3D con dimensiones (ciudades, días de la semana, semanas)
temperaturas = np.random.randint(0, 40, size=(3, 7, 4))  # Ejemplo con 3 ciudades, 7 días de la semana, y 4 semanas

# Calcular el promedio de temperaturas para cada ciudad por semana
for ciudad in range(temperaturas.shape[0]):
    print(f"Promedio de temperaturas para la ciudad {ciudad + 1}:")
    for semana in range(temperaturas.shape[2]):
        promedio_semana = np.mean(temperaturas[ciudad, :, semana])
        print(f"Semana {semana + 1}: {promedio_semana}°C")
