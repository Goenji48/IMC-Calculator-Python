import tkinter as ttk

tk = ttk.Tk()
tk.configure(width=800, height=400)
tk.resizable(False, False)
tk.title("IMC Calculator")

frame = ttk.Frame(tk, bg="black", width=600, height=400)
frame.pack()

text = ttk.Label(frame, text="IMC Calculator", fg="white", bg="black")
text.pack()

peso_input = ttk.Entry(frame, bg="white", width=100, fg="black", borderwidth=5, text="Peso")
peso_input.pack()

altura_input = ttk.Entry(frame, bg="white", width=100, fg="black", borderwidth=5)
altura_input.pack()

imc_value = ttk.Label(frame, bg="black", fg="white")
imc_value.pack()

button = ttk.Button(frame, text="Calcular", command= lambda : calculateIMC())
button.pack()

final_result = ttk.Label(frame, text="", fg="white", bg="black")
final_result.pack()

def calculateIMC():
    peso = 0
    altura = 0

    while peso == 0:
        try:
            peso = float(peso_input.get())
        except:
            final_result['text'] = "Insira um valor numérico"
            break
    while altura == 0:
        try:
            altura = float(altura_input.get())
        except:
            final_result['text'] = "Insira um valor numérico"
            break

    while peso > 1 and altura > 1:
        imc_result = imcValue(peso, altura)
        imc_value['text'] = f"Seu IMC é: {imc_result}"
        final_result['text'] = imcClassification(imc_result)
        break

def imcValue(peso, altura):
    imc = 0
    if peso > 1 or altura > 1:
        alturafinal = pow(altura, 2)
        imc = peso / alturafinal
    return imc

def imcClassification(imc):
    result = ""
    if imc <= 16.9:
        result = "Você está muito abaixo do peso"
    elif imc <= 18.4:
        result = "Você está abaixo do peso"
    elif imc <= 24.9:
        result = "Você está com peso normal"
    elif imc <= 29.9:
        result = "Você está acima do peso"
    elif imc <= 34.9:
        result = "Você está com Obesidade de grau I"
    elif imc <= 40:
        result = "Você está com Obesidade de grau II"
    elif imc > 40:
        result = "Você está com Obesidade de grau III"
    return result

tk.mainloop()