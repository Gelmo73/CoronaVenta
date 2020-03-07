import marshal
import os
from datetime import datetime
lineas = '-----------------------------------'


def limpiar():
    os.system('cls')


def titulo():
    print('CoronaVenta SA')
    print(lineas)


def agregar():
    registro = dict()
    titulo()
    print('Registrar compra')
    print(lineas)
    registro['Nombre'] = input('Nombre del vendedor: ').strip()
    registro['Apellido'] = input('Apellido del vendedor: ').strip()
    registro['Fecha'] = str(datetime.now())
    registro['Cedula'] = input('Cedula del vendedor: ').strip()
    registro['Telefono'] = input('Telefono del vendedor: ').strip()
    registro['Articulo'] = input('Articulo a registrar: ').strip()
    registro['Valor'] = input('Valor del articulo: ').strip()
    registro['Dinero'] = input('Dinero entregado: ').strip()

    registros.append(registro)
    del (registro)
    print('Todo correcto...')
    return


def mostrar():

    for registro in registros:
        print('Registro:', registros.index(registro) + 1)
        print(registro['Fecha'])
        print(registro['Nombre'], registro['Apellido'])
        print('Cedula:', registro['Cedula'], 'Telefono:', registro['Telefono'])
        print('Articulo:', registro['Articulo'], 'Valor:', registro['Valor'],
              'Dinero Entregado:', registro['Dinero'])
        print(lineas)


def mostrarRegistro(registro):
    print('Nombre:', registro['Nombre'])
    print('Apellido:', registro['Apellido'])
    print('Fecha:', registro['Fecha'])
    print('Cedula:', registro['Cedula'])
    print('Telefono:', registro['Telefono'])
    print('Articulo:', registro['Articulo'])
    print('Valor:', registro['Valor'])
    print('Dinero Entregado:', registro['Dinero'])
    print(lineas)


def editar():
    titulo()
    print('Modificar compras')
    print(lineas)
    mostrar()
    try:
        r = int(
            input('Escriba el numero de registro que desee modificar: ').strip()) - 1
    except:
        print('Ha ocurrido un error')

    if r > len(registros) - 1 or r < 0:
        print('Registro no existe')
        return

    limpiar()
    cosa = True
    while (cosa):

        mostrarRegistro(registros[r])
        l = input('Escriba el campo que desee modificar: ').capitalize().strip()

        if l == 'Fecha':
            print('No es muy recomendale modificar las fechas')
            if not input('Esta seguro que desea hacer? [S/s] ').lower() == 's':
                continue

        if l == 'Dinero entregado':
            l = 'Dinero'

        if not l in registros[r]:
            print('Registro no existente')
            return

        registros[r][l] = input('Digite el reemplazo: ')
        print('Dato modificado')

        if input('Desea seguir modifincado? [S/s]').lower().strip() == 's':
            limpiar()
        else:
            cosa = False


def eliminar():
    titulo()
    print('Eliminar compras')
    print(lineas)
    mostrar()
    try:
        r = int(
            input('Escriba el numero de registro que desee modificar: ').strip()) - 1
    except:
        print('Ha ocurrido un error')

    if r > len(registros) - 1 or r < 0:
        print('Registro no existe')
        return

    registros.pop(r)
    print('Registro eliminado')


def menu():
    limpiar()
    titulo()
    print('''
1- Registrar compra
2- Editar compra
3- Eliminar compra
0- Salir
    ''')
    print(lineas)
    r = input()

    if r == '1':
        limpiar()
        agregar()
        input()
        limpiar()
        menu()
    elif r == '2':
        limpiar()
        editar()
        input()
        limpiar()
        menu()
    elif r == '3':
        limpiar()
        eliminar()
        input()
        limpiar()
        menu()
    elif r == '0':
        pass
    else:
        print('Opcion no valida')
        input()
        limpiar()
        menu()


if not os.path.exists('C:/Datos/'):
    os.mkdir('C:/Datos/')

if os.path.exists('C:/Datos/datos.bin'):
    with open('C:/Datos/datos.bin', 'rb') as f:
        registros = marshal.load(f)
else:
    registros = list()

menu()

if input('Presione [S/s] para guardar cambios: ').lower().strip() == 's':
    with open('C:/Datos/datos.bin', 'wb') as f:
        marshal.dump(registros, f)
        print('Guardado satisfactoriamente')
        input()
