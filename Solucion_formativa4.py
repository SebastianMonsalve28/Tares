turistas = {"001": ["John Doe", "Estados Unidos", "12-01-2024"],
            "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
            "012": ["Julian Martinez", "Argentina", "19-09-2023"],
            "014": ["Agustin Morales", "Argentina", "28-03-2024"],
            "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
            "006": ["Maria Lopez", "Mexico", "08-12-2023"],
            "007": ["Joao Silva", "Brasil", "20-06-2024"],
	        "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
	        "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
            "008": ["Ana Santos", "Brasil", "03-10-2023"],
            "010": ["Martin Fernandez", "Argentina", "13-03-2023"],
            "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
     }

### FUNCIONES
def turista_por_pais(pais):
    l = []
    for ident in turistas:
        p = turistas[ident][1]
        if pais == p:
            l.append(turistas[ident][0])
    l.sort()
    if len(l) == 0:
        print("No hay turistas de ese pais.")
    else:
        print(l)

def turista_por_mes(mes):
    if len(mes) == 1:
        mes = "0" + mes
    suma = 0
    for ident in turistas:
        nombre, pais, fecha = turistas[ident]
        m = fecha[3:5]
        if m == mes:
            suma += 1
    p = round((suma/len(turistas))*100,1)
    return p
  
def eliminar_turista():
    nombre = input("Ingrese nombre del turista a eliminar: ")
    for ident in turistas:
        name = turistas[ident][0]
        if name.lower() == nombre.lower():
            del turistas[ident]
            print("Turista eliminado con exito.")
            return
    print("Turista no encontrado. No se pudo eliminar.")

### MAIN
while True:
    print("MENU PRINCIPAL")
    print("1.- Turistas por pais.")
    print("2.- Turista por mes.")
    print("3.- Eliminar turista.")
    print("4.- Salir.")
    op = input("Ingrese opción: ")
    if op == "4":
        print("Programa terminado...")
        break
    elif op == "1":
        pais = input("Ingrese pais a buscar: ")
        turista_por_pais(pais)
    elif op == "2":
        while True:
            mes = input("Ingrese mes a buscar: ")
            if int(mes) >= 1 and int(mes) <= 12:
                break
            else:
                print("Debe ingresar un valor entre 1 y 12. Intentelo nuevamente.")
        porcentaje = turista_por_mes(mes)
        print("El numero de turistas equivale al", porcentaje, "% del total.")
    elif op == "3":
        eliminar_turista()
    else:
        print("Debe ingresar una opción válida!!")