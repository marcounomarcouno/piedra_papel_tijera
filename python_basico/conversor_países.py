menu = """
Bienvenido al conversor de monedas

1- Pesos mexicanos
2- Pesos argentinos
3- Pesos colombianos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = float(input('¿cuántos pesos mexicanos tienes?'))
    valor_dolar = 19.90
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + 'dólares')
elif opcion == 2:
    pesos = float(input('¿cuántos pesos argentinos tienes?'))
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + 'dólares')
elif opcion == 3:
    pesos = float(input('¿cuántos pesos colombianos tienes?'))
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + 'dólares')
else: 
    print('Ingresa una opción correcta')