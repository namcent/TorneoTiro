from clases import Disparo, Concurso, Participante

print("  ______                            __      _______          ")
print(" /_  __/__  _______  ___ ___    ___/ /__   /_  __(_)______   ")
print("  / / / _ \/ __/ _ \/ -_) _ \  / _  / -_)   / / / / __/ _ \  ")
print(" /_/  \___/_/ /_//_/\__/\___/  \_,_/\__/   /_/ /_/_/  \___/  ")
print("                                                             ")

concurso = Concurso()

while True:
    print("\nDatos del participante:")
    nombre = input('Ingrese el nombre: ')
    apellido = input('Ingrese el apellido: ')
    edad = int(input('Ingrese la edad: '))
    sexo = input('Ingrese el sexo: ')
    x1 = int(input('Ingrese x 1: '))
    y1 = int(input('Ingrese y 1: '))
    x2 = int(input('Ingrese x 2: '))
    y2 = int(input('Ingrese y 2: '))
    x3 = int(input('Ingrese x 3: '))
    y3 = int(input('Ingrese y 3: '))
    
    disparo = Disparo(nombre, apellido, edad, sexo, [x1, y1, x2, y2, x3, y3])
    concurso.agregar(disparo)
    
    opcion = input('\nDesea seguir ingresando participantes? (s/n): \n')
    if opcion == 'n':
        break

while True:

    print("\nIngrese la opción deseada:")
    print("1. Ver registros")
    print("2. Ver podio")
    print("3. Ver último puesto")
    print("4. Ver cantidad de participantes")
    print("5. Ver participantes ordenados por edad")
    print("6. Ver promedio total")
    print("7. Ver ganador")
    print("8. Guardar en csv")
    print("9. Guardar en base de datos")
    print("10. Ver desde base de datos")
    print("11. Ver premio del ganador\n")
    opcion = input()

    if opcion=='1':
        concurso.mostrar_registros()
    elif opcion=='2':
        concurso.mostrar_podio()
    elif opcion=='3':
        concurso.mostrar_ultimo()
    elif opcion=='4':
        concurso.mostrar_cantidad_participantes()
    elif opcion=='5':
        print("Participantes ordenados por edad:\n")
        concurso.ordenar_por_edad()
    elif opcion=='6':
        concurso.mostrar_promedio()
    elif opcion=='7':
        concurso.mostrar_ganador()
    elif opcion=='8':
        concurso.guardar_csv()
    elif opcion=='9':
        concurso.guardar_db()
    elif opcion=='10':
        print("Participantes desde base de datos:\n")
        concurso.mostrar_db()
    elif opcion=='11':
        concurso.mostrar_premio()
    else:
        print("Ingrese una opción válida\n")
    
    seguir = input('Desea ingresar otra opción? (s/n): ')
    if seguir == 'n':
        break