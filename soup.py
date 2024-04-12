import random
import string
from ply import lex, yacc
import tkinter as tk
from tkinter import simpledialog 
# Definición de tokens
tokens = (
    'TAMANO',
    'PALABRA',
    'COMA',
)

# Definición de expresiones regulares para tokens
t_TAMANO = r'\d+'
t_COMA = r','
t_PALABRA = r'[A-Za-z]+'

# Ignorar espacios y saltos de línea
t_ignore = ' \n'

# Función para manejar errores
def t_error(t):
    print("Carácter no permitido para el compilador '%s'" % t.value[0])
    t.lexer.skip(1)

# Definición de reglas de análisis sintáctico
def p_sopa_letras(p):
    '''sopa_letras : TAMANO palabras'''
    tamano = int(p[1])
    palabras = p[2]
    if not validar_entrada(tamano, palabras):
        print("La entrada no es válida.")
        return
    sopa = generar_sopa(tamano, palabras)
    escribir_sopa_en_archivo(sopa)

# Definición de la regla para la lista de palabras
def p_palabras(p):
    '''palabras : PALABRA
                | PALABRA COMA palabras'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

# Función para validar la entrada
def validar_entrada(tamano, palabras):
    for palabra in palabras:
        if len(palabra) > tamano:
            return False
    return True

# Función para generar la sopa de letras
def generar_sopa(tamano, palabras):
    sopa = [[' ' for _ in range(tamano)] for _ in range(tamano)]
    alphabet = string.ascii_uppercase
    for palabra in palabras:
        direccion = random.choice(['horizontal', 'vertical', 'diagonal'])
        palabra_colocada = False
        
        while not palabra_colocada:
            start_row = random.randint(0, tamano - 1)
            start_col = random.randint(0, tamano - 1)
            
            # Verificar si la palabra puede ser colocada en esta posición
            if direccion == 'horizontal' and start_col <= tamano - len(palabra):
                if all(sopa[start_row][start_col + i] == ' ' for i in range(len(palabra))):
                    for i, letra in enumerate(palabra):
                        sopa[start_row][start_col + i] = letra
                    palabra_colocada = True
            elif direccion == 'vertical' and start_row <= tamano - len(palabra):
                if all(sopa[start_row + i][start_col] == ' ' for i in range(len(palabra))):
                    for i, letra in enumerate(palabra):
                        sopa[start_row + i][start_col] = letra
                    palabra_colocada = True
            elif direccion == 'diagonal' and start_row <= tamano - len(palabra) and start_col <= tamano - len(palabra):
                if all(sopa[start_row + i][start_col + i] == ' ' for i in range(len(palabra))):
                    for i, letra in enumerate(palabra):
                        sopa[start_row + i][start_col + i] = letra
                    palabra_colocada = True

    # Llenar las celdas vacías con letras aleatorias
    for i in range(tamano):
        for j in range(tamano):
            if sopa[i][j] == ' ':
                sopa[i][j] = random.choice(alphabet)

    return sopa

# Función para escribir la sopa de letras en el archivo txt
def escribir_sopa_en_archivo(sopa):
    with open('sopa.txt', 'w') as f:
        for row in sopa:
            f.write(' '.join(row) + '\n')

# Función para manejar errores de análisis sintáctico
def p_error(p):
    print("Error de sintaxis en '%s'" % p.value)

# Construcción del analizador léxico y sintáctico
lexer = lex.lex()
parser = yacc.yacc()

from flask import Flask, request, render_template

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sopadeletras', methods=['POST'])

def main():
    numero = request.form['numero']
    palabras = request.form['palabras']
    entrada = f"{numero} {palabras}"
    parser.parse(entrada)
    recordatorio = f'Palabras: {palabras}'
    with open('sopa.txt','r') as file:
        sopa_content = file.read()
    return render_template('index.html', numero=numero, palabras=palabras, sopa_content=sopa_content, recordatorio=recordatorio)

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == "__main__":
    main()
