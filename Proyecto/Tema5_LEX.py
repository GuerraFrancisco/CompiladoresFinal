#1. Instalamos Ply manualmente.
# python -m pip install ply

#2) Se importa la librería Lex desde Ply.
from ply import lex as lex

#3) Definimos todos los tokens del proyecto.
tokens = ['Ope', 'OpeComp', 'SepPto', 'SepPtoComa', 'SepDosPtos', 'ParApe', 'ParCie', 
    'TDEntero', 'TDTexto',  'TDDecimal', 'TDLogico', 'ValorBool', 'ValorEntero', 'ValorTexto', 'ValorDecimal',
    'AsignValor', 'Id', 'ComLinea', 'ComBloq', 'InicioProg', 'FinProg', 'PrADD', 'PrVAR', 'PrFUNC', 
    'PrRETORNO', 'PrPIN', 'PrOUTPUT', 'PrINPUT', 'PrIF', 'PrELSE', 'PrWHILE', 'PrBEGIN', 'PrEND', 
    'PrFOW', 'PrBACK', 'PrLEFT', 'PrRIGHT', 'PrWAIT', 'PrSTOP'] 

# Definición de los tokens
t_Ope	        = r"[+\-*/%]" # Un operador cualquiera, pusimos \- por character escape (?)
t_OpeComp	    = r"(<)|(>)|(<=)|(>=)|(==)|(!=)" # Hace falta hacer así para evitar lexemas de tipo <====
t_SepPto	    = r"[.]"
t_SepPtoComa    = r"[;]"
t_SepDosPtos	= r"[:]"
t_ParApe	    = r"[(]"
t_ParCie	    = r"[)]"
t_ValorEntero   = r"(\-)*[0-9]+" # Número de al menos un dígito positivo o negativo
t_ValorTexto    = r"(\")[a-zA-Z]+(\")" # Número de al menos un dígito positivo o negativo
t_ValorDecimal  = r"(\-)*[0-9]+(\,)[0-9]+" # Número de al menos un dígito positivo o negativo
t_AsignValor    = r"[=][:]"

# Ignorar comentarios
def t_ComLinea(t):
	r'(/\*).*'
	pass

def t_ComBloq(t):
	r'(//\*(.|\n)*?\*//)'
	pass

palabrasReservadas = {
	'INT': 'TDEntero',
	'STRING': 'TDTexto',
	'FLAOT': 'TDDecimal',
	'BOOL': 'TDLogico',
	'TRUE': 'ValorBool',
	'FALSE': 'ValorBool',
	'SUPERBEG': 'InicioProg',
	'SUPEREND': 'FinProg',
	'ADD': 'PrADD',
	'VAR': 'PrVAR',
	'FUNC': 'PrFUNC',
	'RETORNO': 'PrRETORNO',
	'PIN': 'PrPIN',
	'OUTPUT': 'PrOUTPUT',
	'INPUT': 'PrINPUT',
	'IF': 'PrIF',
	'ELSE': 'PrELSE',
	'WHILE': 'PrWHILE',
	'BEGIN': 'PrBEGIN',
	'END': 'PrEND',
	'FOW': 'PrFOW',
	'BACK': 'PrBACK',
	'LEFT': 'PrLEFT',
	'RIGHT': 'PrRIGHT',
	'WAIT': 'PrWAIT',
	'STOP': 'PrSTOP',
}

def t_Id(t):
	r"[a-zA-Z]([a-zA-Z0-9_])*"
	if t.value.upper() in palabrasReservadas:
		t.type = palabrasReservadas[t.value.upper()]
	return t

#4. Definimos una función para ignorar los espacios en blanco y tabulaciones.
t_ignore  = ' \t'

#5. Definimos una función para que cuente las líneas.
def t_newline(t):
    r'\n'
    t.lexer.lineno+=1

#6. Definimos una función para detectar los errores en caso de que hayan.
def t_error(t):
    print ("Error léxico: %s" % repr(t.value[0]), "en línea n°: ",repr(t.lexer.lineno))
    t.lexer.skip(1)

#7. Finalmente construimos el analizador léxico.
lexer = lex.lex()

# Prueba del analizador léxico
#2. Definimos el archivo a ser utilizado como entrada para la prueba del analizador léxico.
# f = open("entrada.txt")
# data = f.read()
# f.close()
# lexer.input(data)

#3. Identifica de la cadena de entrada los tokens y muestra el token y el lexema
# print('('+'Token'.center(27)+' | '+'Lexema'.center(27)+')')
# print('-----------------------------------------------------------')
# while True:
#     tok = lexer.token()
#     if not tok: break
#     print('(', tok.type.center(25), ' | ',tok.value.center(25), ')')