# Este programa calcula las raices de un polinomio de grado 2
print('Encontraremos las raíces de una ecuación de la forma ax^2+bx+c')

a = float(input('Ingrese el valor del coeficiente <a>  '))
b = float(input('Ingrese el valor del coeficiente <b>  '))
c = float(input('Ingrese el valor del coeficiente <c>  '))

discriminante = ((b)**2)-4*a*c
if discriminante < 0:
    print('No existe una solución en los números reales')
else: 
    x1 = (-b+(((b)**2)-4*a*c))/(2*a)
    x2 = (-b-(((b)**2)-4*a*c))/(2*a)
    print('La raíz x1 es ' + str(x1))
    print('La raíz x2 es ' + str(x2))