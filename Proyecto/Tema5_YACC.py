#1. Importamos la librería Yacc desde Ply y el analizador léxico previamente construido.
from Tema5_LEX import *
import Tema5_LEX
from ply import yacc

#2. Definimos las reglas de producción.
start = 'Inicio'

def p_Inicio (p):
    '''Inicio : InicioProg SepPto sentencias FinProg SepPto'''

def p_sentencias (p):
    '''sentencias : inclibreria sentencias
                    | defvble sentencias
                    | asigvble sentencias
                    | deffunc sentencias
                    | defproc sentencias
                    | asigpin sentencias
                    | if sentencias
                    | while sentencias
                    | fow sentencias
                    | back sentencias
                    | left sentencias
                    | right sentencias
                    | wait sentencias
                    | stop sentencias
                    | empty'''

def p_inclibreria (p):
    '''inclibreria : PrADD ParApe listalibrerias ParCie SepPto'''
    print("inclibreria")

def p_listalibrerias (p):
    '''listalibrerias : Id SepPto Id
                    | Id SepPto Id SepPtoComa listalibrerias'''

def p_defvble (p):
    '''defvble : PrVAR ParApe tipodato SepDosPtos Id ParCie SepPto'''
    print("defvble")

def p_tipodato (p):
    '''tipodato : TDEntero
                | TDTexto
                | TDDecimal
                | TDLogico'''

def p_asigvble (p):
    '''asigvble : Id AsignValor valor SepPto'''
    print("asigvble")

def p_valor (p):
    '''valor : Id
            | ValorEntero
            | ValorTexto
            | ValorDecimal
            | ValorBool
            | Id Ope valor
            | ValorEntero Ope valor
            | ValorTexto Ope valor
            | ValorDecimal Ope valor
            | ValorBool Ope valor'''

def p_deffunc (p):
    '''deffunc : PrFUNC ParApe listaargs ParCie sentencias PrRETORNO valor SepPto'''
    print("deffunc")

def p_listaargs (p):
    '''listaargs : tipodato SepDosPtos Id
                | tipodato SepDosPtos Id listaargs'''

def p_defproc (p):
    '''defproc : PrFUNC ParApe listaargs ParCie sentencias SepPto'''
    print("defproc")

def p_asigpin (p):
    '''asigpin : PrPIN ParApe valor SepDosPtos tipopin ParCie SepPto'''
    print("asigpin")

def p_tipopin (p):
    '''tipopin : PrOUTPUT 
                | PrINPUT'''

def p_if (p):
    '''if : PrIF ParApe valor OpeComp valor ParCie PrBEGIN sentencias PrEND SepPto
        | PrIF ParApe valor OpeComp valor ParCie PrBEGIN sentencias PrEND PrELSE PrBEGIN sentencias PrEND SepPto'''
    print("if")

def p_while (p):
    '''while : PrWHILE ParApe valor OpeComp valor ParCie PrBEGIN sentencias PrEND SepPto'''
    print("while")

def p_fow (p):
    '''fow : PrFOW ParApe ParCie SepPto'''
    print("fow")

def p_back (p):
    '''back : PrBACK ParApe ParCie SepPto'''
    print("back")

def p_left (p):
    '''left : PrLEFT ParApe ParCie SepPto'''
    print("left")

def p_right (p):
    '''right : PrRIGHT ParApe ParCie SepPto'''
    print("right")

def p_wait (p):
    '''wait : PrWAIT ParApe valor ParCie SepPto'''
    print("wait")

def p_stop (p):
    '''stop : PrSTOP ParApe ParCie SepPto'''
    print("stop")

#3. Definimos la regla de producción empty para que muchas reglas no queden encerradas en un ciclo infinito.
def p_empty(p):
    'empty :'
    pass

#4. Definimos una función que detecta los errores y nos muestra en qué línea se detectó.
def p_error (p):
    print("Error sintáctico en la línea: " + str(p.lineno)
            + ". Token inesperado: " + str(p.value))
    raise Exception('syntax', 'error')

#5. Finalmente construimos el analizador sintáctico.
parser = yacc.yacc()
Tema5_LEX.lexer.lineno = 0