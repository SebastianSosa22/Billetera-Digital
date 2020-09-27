#Recibir Cantidad
def recibirCantidad():
	nombreCriptoRecibir = input("Ingrese la Criptomoneda a Recibir: ")
	cantRecibir = input("Ingrese la Cantidad de "+nombreCriptoRecibir+" a Recibir: ")
	codigo = input("Ingrese el codigo del remitente: ")

#Transferir Monto
def enviarCantidad():
	nombreCriptoEnviar = input("Ingrese la Criptomoneda a Enviar: ")
	cantEnviar = input("Ingrese la cantidad de "+nombreCriptoEnviar+" a Enviar: ")
	codigo = input("Ingrese el codigo del destinatario: ")

#Mostrar el balance una moneda
def mostrarBalanceMoneda():
	nombreCriptoMostrar = input("Ingrese la Criptomoneda a Mostrar: ")

#Mostrar el balance en general
def mostrarBalanceGeneral():
	total = "" 
	print("Su balance general en USD es de: "+str(total))

#Mostrar historial de transacciones
def mostrarHistorial():
	pass

#headers = { 'Accepts': 'application/json', 'X-CMC_PRO_API_KEY':  '1b1e462c-30f7-446b-8a3d-2bf74cfc22d6'}
#parametros = {'symbol': symbol}
#requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest",headers=headers,params=parametros)
