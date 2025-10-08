import os
from pathlib import Path

ruta = os.path.join(os.path.dirname(__file__),"Recetas")
print(ruta)

def contar_recetas(ruta):
    cont = 0
    for txt in Path(ruta).glob("**/*.txt"):
        cont += 1

    return cont

# Mostrar menu inicio
def inicio():
    eleccion_menu ='x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 7):
        os.system('cls')
        print("\n" + "="*50)
        print("👋 ¡Bienvenido al Administrador de Recetas! 👋")
        print("="*50)
        print(f"Las recetas se encuentran en {ruta}")
        print(f"Hay un todal de {contar_recetas(ruta)} recetas")
   
        print("\n" + "-"*44)
        print("           📋 MENÚ PRINCIPAL 📋")
        print("-"*44)
        print("1️⃣  Leer receta")
        print("2️⃣  Crear nueva receta")
        print("3️⃣  Crear nueva categoria")
        print("4️⃣  Eliminar receta")
        print("5️⃣  Eliminar categoria")
        print("6️⃣  ❌ Salir del programa")
        print("-"*44)
        eleccion_menu = input("Selecciona una opción (1-6): ")
        os.system('cls')
    return int(eleccion_menu)

def mostrar_categorias(ruta):
    print("\n📂 CATEGORÍAS DISPONIBLES:")
    print("-" * 40)
    ruta_categorias = Path(ruta)
    lista_categorias = []
    
    for i, categ in enumerate(ruta_categorias.iterdir(), start=1):
        print(f"[{i}.- {categ.name}]")
        lista_categorias.append(categ)

    print("-" * 40)
    return lista_categorias

def elegir_categoria(lista):
    eleccion = ''
    while not eleccion.isnumeric() or int(eleccion) not in range(1, len(lista) + 1):
        eleccion = input("\n🔸 Elige una categoría (número): ")
    return lista[int(eleccion) - 1]

def mostrar_recetas(ruta):
    print("\n📜 RECETAS DISPONIBLES:")
    print("-" * 40)
    ruta_recetas = Path(ruta)
    lista_recetas = []

    for i, receta in enumerate(ruta_recetas.glob("**/*.txt"), start=1):
        print(f"[{i}.- {receta.name}]")
        lista_recetas.append(receta)

    print("-" * 40)
    return lista_recetas

def elegir_receta(lista):
    eleccion = ''
    while not eleccion.isnumeric() or int(eleccion) not in range(1, len(lista) + 1):
        eleccion = input("\n🔸 Elige una receta (número): ")
    return lista[int(eleccion) - 1]

def leer_receta(receta):
    print("\n📖 CONTENIDO DE LA RECETA:")
    print("-" * 40)
    print(Path.read_text(receta))
    print("-" * 40)

def crear_receta(ruta):
    while True:
        nombre = input("\n📝 Escribe el nombre de la nueva receta: ").strip() + ".txt"
        print("✍️  Escribe el contenido de tu receta (escribe 'FIN' en una línea para terminar):")
        
        lineas = []
        while True:
            linea = input()
            if linea.strip().upper() == 'FIN':
                break
            lineas.append(linea)
        
        contenido = "\n".join(lineas).strip()
        
        if not contenido:
            print("⚠️ No escribiste ningún contenido. Intenta de nuevo.\n")
            continue
        
        ruta_nueva = Path(ruta, nombre)

        if not ruta_nueva.exists():
            Path.write_text(ruta_nueva, contenido, encoding='utf-8')
            print(f"✅ Receta '{nombre}' creada exitosamente.\n")
            break
        else:
            print("⚠️ Esa receta ya existe. Intenta con otro nombre.")

def crear_categoria(ruta):
    while True:
        nombre = input("\n📁 Escribe el nombre de la nueva categoría: ").strip()
        ruta_nueva = Path(ruta, nombre)

        if not ruta_nueva.exists():
            Path.mkdir(ruta_nueva)
            print(f"✅ Categoría '{nombre}' creada exitosamente.\n")
            break
        else:
            print("⚠️ Esa categoría ya existe. Intenta con otro nombre.")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"🗑️ Receta '{receta.name}' eliminada correctamente.")

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"🗑️ Categoría '{categoria.name}' eliminada correctamente.")


def volver_inicio():
    eleccion_regresar = 'x'

    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("Presione V para volver al menu: ")

Finalizar_programa = False

while not Finalizar_programa:
    menu = inicio()
    if menu == 1:
        mis_categorias = mostrar_categorias(ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("no hay recetas en esta categoría.")
        else:
            mi_receta = elegir_receta(mis_recetas)
            leer_receta(mi_receta)
        volver_inicio()
    elif menu == 2:
        mis_categorias = mostrar_categorias(ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()
    elif menu == 3:
        crear_categoria(ruta)
        volver_inicio()
    elif menu == 4:
        mis_categorias = mostrar_categorias(ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("no hay recetas en esta categoría.")
        else:
            mi_receta = elegir_receta(mis_recetas)
            eliminar_receta(mi_receta)
        volver_inicio()
    elif menu == 5:
        mis_categorias = mostrar_categorias(ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()
    elif menu == 6:
        Finalizar_programa = True

  

