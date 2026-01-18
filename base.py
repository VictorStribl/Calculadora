import tkinter
import math

botoes = [ 
    ["C","√","%","÷"],
    ["7","8","9","×"],
    ["4","5","6","-"],
    ["1","2","3","+"],
    ["+/-","0",",","="], 
]
simbolos_direita = ["÷","×","-","+","="]
simbolos_topo = ["C","√","%"]
simbolos_baixo = ["+/-"]

row_count = len(botoes)
column_count = len(botoes[0])

cor_cinza = "#5F6368"
cor_prata = "#80868B"
cor_cinza_escuro = "#3C4043"
cor_laranja = "#FF9500"
cor_branco = "white"

#código da janela
window = tkinter.Tk()
window.title("Calculadora")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 45), background=cor_prata,
                      foreground=cor_branco, anchor="e", width=column_count)

label.grid(row=0, column=0, columnspan=column_count, sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value = botoes[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30),
                                width=column_count-1, height=1,
                                command=lambda value=value: botao_apertado(value))
        if value in simbolos_topo:
            button.config(foreground=cor_branco, background=cor_cinza)
        elif value in simbolos_direita:
            button.config(foreground=cor_branco, background=cor_laranja)
        else:
            button.config(foreground=cor_branco, background=cor_cinza_escuro)
        button.grid(row=row+1, column=column)

frame.pack()

A = "0"
operator = None
B = None

def limpar():
    global A, B, operator
    A = None
    B = None
    operator = None

def remover_n_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)

def botao_apertado(value):
    global simbolos_direita, simbolos_topo, label, A, B, operator

    if value in simbolos_direita:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remover_n_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remover_n_decimal(numA - numB)
                elif operator == "×":
                    label["text"] = remover_n_decimal(numA * numB)
                elif operator == "÷":
                    label["text"] = remover_n_decimal(numA / numB)
                
                limpar()

        elif value in "+-×÷":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"

            operator = value
    elif value in simbolos_topo:
        if value == "C":
            limpar()
            label["text"] = "0"
        elif value == "√":
            num = float(label["text"])
            if num >= 0:
                resultado = math.sqrt(num)
                label["text"] = remover_n_decimal(resultado)
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remover_n_decimal(result)
    elif value in simbolos_baixo:
        if value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = str(result)
    else:
        if value == ",":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value

#janela abrir no meio
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()