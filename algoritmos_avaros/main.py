from binSearch import RangeMap

# se puede usar el codigo de la presentacion
# https://inst-fs-iad-prod.inscloudgate.net/files/42d43942-9974-48b2-9339-409504fc35d6/Programaci%C3%B3n%20Din%C3%A1mica%E2%80%8B.pdf?download=1&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3MjM3OTEyNjAsInVzZXJfaWQiOiIxNDMyODAwMDAwMDAyODk4NjciLCJyZXNvdXJjZSI6Ii9maWxlcy80MmQ0Mzk0Mi05OTc0LTQ4YjItOTMzOS00MDk1MDRmYzM1ZDYvUHJvZ3JhbWFjaSVDMyVCM24lMjBEaW4lQzMlQTFtaWNhJUUyJTgwJThCLnBkZiIsImp0aSI6ImNmYWY3NTBmLTVhMGMtNDEyMi04YmYwLWZkYjc3YWExOTllZiIsImhvc3QiOiJleHBlcmllbmNpYTIxLnRlYy5teCIsIm9yaWdpbmFsX3VybCI6Imh0dHBzOi8vYTE0MzI4LTE5NTcwMDI5NC5jbHVzdGVyMjExLmNhbnZhcy11c2VyLWNvbnRlbnQuY29tL2NvdXJzZXMvMTQzMjh-NDkxMzkzL2ZpbGVzLzE0MzI4fjE5NTcwMDI5NC9jb3Vyc2UlMjBmaWxlcy9Qcm9ncmFtYWNpJUMzJUIzbiUyMERpbiVDMyVBMW1pY2ElRTIlODAlOEIucGRmP2Rvd25sb2FkX2ZyZD0xXHUwMDI2bm9fY2FjaGU9dHJ1ZVx1MDAyNnJlZGlyZWN0PXRydWVcdTAwMjZzZl92ZXJpZmllcj1leUowZVhBaU9pSktWMVFpTENKaGJHY2lPaUpJVXpVeE1pSjkuZXlKMWMyVnlYMmxrSWpvaU1UUXpNamd3TURBd01EQXdNamc1T0RZM0lpd2ljbTl2ZEY5aFkyTnZkVzUwWDJsa0lqb2lNVFF6TWpnd01EQXdNREF3TURBd01EQXhJaXdpYjJGMWRHaGZhRzl6ZENJNkltVjRjR1Z5YVdWdVkybGhNakV1ZEdWakxtMTRJaXdpY21WMGRYSnVYM1Z5YkNJNmJuVnNiQ3dpWm1Gc2JHSmhZMnRmZFhKc0lqb2lhSFIwY0hNNkx5OWxlSEJsY21sbGJtTnBZVEl4TG5SbFl5NXRlQzlqYjNWeWMyVnpMelE1TVRNNU15OW1hV3hsY3k4eE9UVTNNREF5T1RRdlpHOTNibXh2WVdRX1pHOTNibXh2WVdSZlpuSmtQVEZjZFRBd01qWm1ZV3hzWW1GamExOTBjejB4TnpJek9ESXlOVGsySWl3aVpYaHdJam94TnpJek9ESXlPRGsyZlEuTzBFVEFKTTBITW1PN2doS3pzdTRxU3BNVlB1TlpNQ05rLVdNS1JnekhfcUptZ0x6M3lLTWloa09RaTU2OWU5TWVnR0NHcUF4SHc0dXNySkdZc2cyblEiLCJleHAiOjE3MjM4Nzc2NjB9.23Ylen2OT6D6zF3hMigh6MScT4P6zj-eQzKzTGAI4SLPMoRhwC0wes0xo2eMFc22BF_u8sljzXErqxpHdM3QuQ
cambio = {}

# TODO
# Aparentemente cambio es un apuntador, tengo que acceder a el para poder modificarlo
# en binsearch hay Assertion error supongo por lo mismo. de en que la funcion min_pesos cambio es un apuntador, mas no la lista literalmente


def min_pesos(total, denominations, cache = cambio):
    
    # Para poder buscar una llave que sea un entero en un diccionario de python, se tiene que hacer una estructura de dato personalizada, al menos eso encontre en stackoverflow
    # Cada que se llama la funcion volvemos a asignar el diccionario actualizado
    
    
    print(len(cambio))
    
    # Ya que el metodo __getitem__ lanza una excepcion si no encuentra un dato
    # Realizamos un try catch, si existe el resultado, lo regresamos, si no, no
    #
    if len(cambio) != 1:
        mapaBuscable = RangeMap(cambio)
        try:
            result = mapaBuscable[total]
            return result
        except KeyError:
            # Si el valor no existe en el diccionario, continuar con el cálculo
            print("Valor no ha sido calculado, prosiguiendo")
    
    
    denominations.sort(reverse=True)
    count = 0
    pesos_usados = []

    for pesos in denominations:
        if total >= pesos:
            num_pesos = total // pesos  # Número de monedas/billetes de esta denominación
            count += num_pesos
            total -= num_pesos * pesos
            pesos_usados.append((pesos, num_pesos))
    
    # Guardamos el resultado en el diccionario 'cambio'
    cambio[total] = (count, pesos_usados)
    return count, pesos_usados

def checkDenomination(billete, denominaciones):
    if billete in denominaciones:
        return True
    else:
        return False


denominaciones = [1,2,5,10,20,50,100,200,500,1000]
# cambio = {}
billetes = 1

while billetes != 0:
    print("Denominaciones actuales: ", denominaciones)
    billetes = int(input("Ingrese 0 para continuar \nIngrese una denominacion de billete: "))
    
    if billetes in denominaciones:
        print("Ese billete ya esta en las denominaciones")
    else:
        if billetes == 0:
            continue
        denominaciones.append(billetes)

transaccion = 1 # Flag para indicar que la transaccion esta sucediento

while transaccion == 1:
    


    precioP = int(input("Cual es el precio del producto que quiere comprar?: "))
    total = 0


    billeteQ = int(input("Con que billete se realiza el pago?: "))
    if checkDenomination(billeteQ, denominaciones):
            total = total + billeteQ
    else:
        print("Porfavor ingrese un billete valido")        

    while total <= precioP:
        billeteQ = int(input("Porfavor ingrese otro billete para que su pago sea mas que el total: "))
        if checkDenomination(billeteQ, denominaciones):
            total = total + billeteQ
            print("Total de pesos ingresados: ", total)
        else:
            print("Porfavor ingrese un billete valido")
        
    if total == precioP: # Se evita el calculo del cambio
        print("No hay cambio" )
    else:
        cambio = total - precioP
        # No vamos a modificar la funcion proporcionada en al diapositiva, solo agregamos la parte de revisar si el calculo existe
        # Para este punto vamos a estar seguros que la cantidad de billetes proporcionados es suficiente para realizar el pago    
        total_pesos, pesos_usados = min_pesos(cambio, denominaciones)
        print(f"Número mínimo de monedas/billetes necesarios: {total_pesos}")
        print("Monedas/Billetes usados:")
        for pesos, count in pesos_usados:
            print(f"{count} x {pesos} $")
    
    
    preguntaUsuario = input("Desea comprar otro producto? si o no: ").upper()
    while preguntaUsuario not in ("SI", "NO"):
        preguntaUsuario = input("Porfavor, solamente ingrese si o no: ").upper()
    
    if preguntaUsuario == "NO":
        transaccion = 0



