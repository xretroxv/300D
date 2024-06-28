import csv

nam = print(str(input("Ingrese tus nombre completo: ")))
dir = print(str(input("Ingrese tus direccion: ")))
tef = print(int(input("Ingrese tus numero de telefono: ")))

import time
t = 2
time.sleep(t)

sw = 1
while sw==1:

    print("---------------------------------------------------")
    print("1.- Registrar Pedido | Permite a los clientes ingresar su información personal y los detalles de su pedido.")
    print("2.- Listar Pedidos | Muestra una lista de todos los pedidos realizados. inluyendo los detalles del cliente.")
    print("3.- Generar Factura | Genera una factura detallada para el cliente con el total a pagar y los detalles del pedido.")
    print("4.- Salir del Programa | Permite al usuario salir del sistema.")
    print("---------------------------------------------------")
    op = int(input("Selecciona una opcion: "))
    try:
        if(op > 0 and op < 5):
            if op == 1:
                print("1done")
                continu = int(input("presione (1) | Salir del programa (2) :"))
                if continu==2:
                    print("cierresesion")
                    sw=0
            if op == 2:
                print("Muestra una listas?")
                continu = int(input("SI (1) | Salir del programa (2) :"))
                if continu==2:
                    print("cierresesion")
                    sw=0
            if op == 3:
                print("done3")
                continu = int(input("presione (1) | Salir del programa (2) :"))
                if continu==2:
                    print("cierresesion")
                    sw=0
            if op == 4:
                print("Saliendo del Programa.")
                break
        else:
            print("seleccion fuera de rango")
    except:
        print("error")