from pathlib import Path
class SelectorTema:

    def __init__(self):

        # Lista donde se guardarán las categorías
        self.Tematicas = []

    # Función para mostrar las categorías
    def SeleccionTematicas(self):

        # Buscar todas las carpetas dentro de "palabras"
        self.Tematicas = [
            carpeta.name #es una funcion de Path para extraer el nombre de un archivo o carpeta
            for carpeta in Path("palabras").iterdir() #Path abre la carpeta palabras e iterdir recorre lo que se encuentra adentro
            if carpeta.is_dir() #is.dir revisa si el archivo que selecciono es carpeta o no
        ]

        # Mostrar título
        print("\n----- SELECCIONA UNA CATEGORÍA -----\n")

        contador = 1

        for categoria in self.Tematicas: #se crea la variable categoria

            print(f"{contador}. {categoria}") #el for avanza automaticamente la categoria no hace falta aclarar que valor de la lista

            contador += 1

        opcion = int(input("\nSeleccione una opción: "))

        # Obtener el nombre de la categoría
        categoria_seleccionada = self.Tematicas[opcion - 1]

        return categoria_seleccionada



"""
if __name__ == "__main__":

    selector = SelectorTema()

    categoria = selector.SeleccionTematicas()
"""
