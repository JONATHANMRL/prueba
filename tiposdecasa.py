# Clase base
class Casa:
    def __init__(self, ventanas, puertas, techo, color):
        self.ventanas = ventanas
        self.puertas = puertas
        self.techo = techo
        self.color = color

    def mostrar_info(self):
        print(f"Ventanas: {self.ventanas}")
        print(f"Puertas: {self.puertas}")
        print(f"Techo: {self.techo}")
        print(f"Color: {self.color}")

# Clase derivada: Vivienda Familiar
class ViviendaFamiliar(Casa):
    def __init__(self, ventanas, puertas, techo, color, num_habitaciones):
        super().__init__(ventanas, puertas, techo, color)
        self.num_habitaciones = num_habitaciones

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Habitaciones: {self.num_habitaciones}")

# Clase derivada: Apartamento
class Apartamento(Casa):
    def __init__(self, ventanas, puertas, techo, color, piso):
        super().__init__(ventanas, puertas, techo, color)
        self.piso = piso

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Piso: {self.piso}")

# Clase derivada: Búngalo
class Bungalo(Casa):
    def __init__(self, ventanas, puertas, techo, color, terraza):
        super().__init__(ventanas, puertas, techo, color)
        self.terraza = terraza  # booleano

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Terraza: {'Sí' if self.terraza else 'No'}")

# Ejemplo de uso
print("=== Vivienda Familiar ===")
v1 = ViviendaFamiliar(6, 2, "Teja", "Blanco", 4)
v1.mostrar_info()

print("\n=== Apartamento ===")
a1 = Apartamento(4, 1, "Concreto", "Gris", 3)
a1.mostrar_info()

print("\n=== Búngalo ===")
b1 = Bungalo(5, 2, "Palma", "Verde", True)
b1.mostrar_info()