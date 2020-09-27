import os
import funciones

def menu():
	os.system('cls')
	print ("Seleccione una opcion")
	print ("\t1 - Recibir Cantidad")
	print ("\t2 - Tranferir Monto")
	print ("\t3 - Mostrar balance una moneda")
	print ("\t4 - Mostrar balance general")
	print ("\t5 - Mostrar historial de transacciones")
	print ("\t0 - Salir del programa")

while True:
	menu()
	opcionMenu = input("Inserta un numero valor: ")

#Recibir Cantidad
	if opcionMenu=="1":
		input("Has pulsado la opcion 1...\npulsa una tecla para continuar")
		funciones.recibirCantidad()
#Transferir Monto
	elif opcionMenu=="2":
		input("Has pulsado la opcion 2...\npulsa una tecla para continuar")
		funciones.enviarCantidad()
#Mostrar el balance de una moneda
	elif opcionMenu=="3":
		input("Has pulsado la opcion 3...\npulsa una tecla para continuar")
		funciones.mostrarBalanceMoneda()
#Mostrar el balance general
	elif opcionMenu=="4":
		input("Has pulsado la opcion 4...\npulsa una tecla para continuar")
		funciones.mostrarBalanceGeneral()
#Mostrar historial de transacciones
	elif opcionMenu=="5":
		input("Has pulsado la opcion 5...\npulsa una tecla para continuar")
		funciones.mostrarHistorial()
#Salir del programa
	elif opcionMenu=="0":
		break
	else:
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")


