

class Libro:
  def __init__(self,titulo,autor, genero,puntuacion):
    self.titulo = titulo
    self.autor = autor
    self.genero = genero
    self.puntuacion = puntuacion

lista_libros = []

lista_libros.append(Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 4.5))
lista_libros.append(Libro("1984", "George Orwell", "Ciencia Ficción", 4.3))
lista_libros.append(Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", 4.7))
lista_libros.append(Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2))
lista_libros.append(Libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clásico", 4.4))
lista_libros.append(Libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1))
lista_libros.append(Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", 4.6))
lista_libros.append(Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía", 4.8))
lista_libros.append(Libro("Los Pilares de la Tierra", "Ken Follett", "Histórica", 4.4))
lista_libros.append(Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasía", 4.0))

def agregar_libro():
    titulo = input("Escribe el nombre del libro: ")
    autor = input("Escribe el nombre del autor: ")
    genero = input("Escribe el genero")

     # Manejo básico de errores por si el usuario no escribe un número
    try:
        puntuacion = float(input("Puntuación (0.0 a 5.0): "))
    except ValueError:
        print("Error: La puntuación debe ser un número decimal. Inténtalo de nuevo.")
        return

    lista_libros.append(Libro(titulo, autor, genero, puntuacion))
    print(f"¡'{titulo}' ha sido agregado con éxito!")

def buscar_libro_genero():
  genero = input("Escribe que genero buscas: ")
  resultado = False
  print(f"\n--Lista de libros del genero, {genero}--\n ")
  for libros in lista_libros:
    if libros.genero.lower() == genero.lower():
      print(f"Titulo:{libros.titulo}")
      resultado = True
  if not resultado:
    print("No se encontraron libros de este genero")
def recomendar_libro():
  genero_interes = input("Escribe que genero buscas: ")
  resultado = False
  contador = []
  lista_genero = []

  for libros in lista_libros:

    if libros.genero.lower() == genero_interes.lower():
      contador.append(libros.puntuacion)
      lista_genero.append(libros)
      resultado = True
  if not resultado:
    print("No se encontraron libros de este genero")
    return
  mayor = max(contador)
  for libro2 in lista_genero:
    if libro2.puntuacion == mayor:
      print(f"Este es el libro: {libro2.titulo}, del genero: {genero_interes}, con mas puntuación")
while True:
    print("\n==== SISTEMA DE RECOMENDACIÓN DE LIBROS ====")
    print("1. Agregar Libro")
    print("2. Buscar Libros por Género")
    print("3. Recomendar Libro")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ").strip()

    if opcion == "1":
        agregar_libro()
    elif opcion == "2":
        buscar_libro_genero()
    elif opcion == "3":
        recomendar_libro()
    elif opcion == "4":
        print("¡Gracias por usar el sistema! Saliendo...")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")

