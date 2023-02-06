from Tema5_YACC import parser

# filename = 'Ejemplo1.txt'
#filename = 'Ejemplo2.txt'
filename = 'Ejemplo3.txt'
#filename = 'Conerrores.txt'  archivo txt con errores lexicos y sintacticos

try:
    f = open(filename)    
    data = f.read()
    f.close()
except IndexError:
    print('Error en archivo:\n')
    data = ''

try:
    resultado = parser.parse(data)
    print('Analisis sintactico correcto')
except:
    print('Analisis sintactico incorrecto')