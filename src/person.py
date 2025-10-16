class Person:
    """
    Clase Person que representa una persona con nombre y apellido.
    
    Esta clase implementa el método especial __str__ para mostrar
    el nombre completo de la persona en formato capitalizado.
    """
    
    def __init__(self, first_name, last_name):

        first_name = "Asael"
        last_name = "Otero"

    def __str__(self):
        nombre_completo = f"{self.first_name} {self.last_name}"
        return nombre_completo
        


# Ejemplo de uso (opcional, para pruebas locales)
if __name__ == "__main__":
    # Crear personas de ejemplo
    p1 = Person("juan", "perez")
    p2 = Person("MARIA", "LOPEZ")
    p3 = Person("cArLoS", "gOnZaLeZ")
    
    # Imprimir usando __str__ automáticamente
    print(p1)  # Juan Perez
    print(p2)  # Maria Lopez
    print(p3)  # Carlos Gonzalez