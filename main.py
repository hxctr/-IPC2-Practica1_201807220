from simplyLinkedList import SimplyLinkedList

def menu():
    cola = SimplyLinkedList()
    
    
    
    opcion = 0
    
    while opcion != 5:
        print("\n"+("> ESCOJA UNA OPCION :") + "\n")
        print('> [1] Ingresar orden' +
                '\n> [2] Entregar orden' +
                '\n> [3] Mostrar ordenes' +
                '\n> [4] Mostrar datos del estudiante' +
                '\n> [5] Salida')
        print('> Ingrese su opción: ', end='' )
        opcion = input()
        print('\n')
        if opcion == '1':
            print('Ingresando orden...')
            ingrediente = input(str('Ingrese el ingrediente de su pizza: '))
            cola.enqueue(ingrediente)
            print('Orden creada con exito')
        elif opcion == '2':
            print(cola.dequeue())
        elif opcion == '3':
            print('Mostrar ordenes...')
            cola.print_queue()
        elif opcion == '4':
            print('Mostrando datos del estudiante...')
            print('     [»]Hector Josue Ponsoy Ayala')
            print('     [»]201807220')
            print('     [»]Introduccion a la Programacion y computacion 2 sección "D"')
            print('     [»]Ingenieria en Ciencias y Sistemas')
            print('     [»]4.to Semestre')
        elif opcion == '5':
            print('Saliendo....')
            opcion = 5
        else:
            print('Opcion invalida')
menu()