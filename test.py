nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = int(input('Ingrese su edad: '))
print
if edad < 18:
    condicion = 'menor'
elif edad <= 65:
    condicion = 'mayor'
elif edad <= 120:
    condicion = 'jubilado'
else:
    condicion = 'cadaver'

print('Su nombre es: ' + nombre + ' ' + apellido + ' y usted es ' + condicion)
print('Su nombre es: {} {} y usted es {}'.format(nombre, apellido, condicion))