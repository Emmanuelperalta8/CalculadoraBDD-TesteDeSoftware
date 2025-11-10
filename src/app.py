import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from src.calculadora import Calculadora

class CalculadoraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora BDD - Moderna")
        self.root.geometry("320x480")
        self.root.resizable(False, False)

        self.calc = Calculadora()
        self.style = ttk.Style("superhero")  # Tema moderno (pode mudar para "flatly", "cyborg", "darkly", etc.)

        # Display
        self.display_var = ttk.StringVar(value="")
        display = ttk.Entry(root, textvariable=self.display_var, font=("Consolas", 20), justify=RIGHT, bootstyle="info")
        display.pack(fill=X, padx=10, pady=15, ipady=10)

        # Botões numéricos e operadores
        botoes = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "√", "+"],
        ]

        frame = ttk.Frame(root)
        frame.pack(padx=10, pady=5)

        for linha in botoes:
            linha_frame = ttk.Frame(frame)
            linha_frame.pack()
            for texto in linha:
                ttk.Button(linha_frame, text=texto, width=6, command=lambda t=texto: self.adicionar(t),
                           bootstyle="secondary").pack(side=LEFT, padx=3, pady=3)

        # Botões especiais
        ttk.Button(root, text="C", width=14, command=self.limpar, bootstyle="danger").pack(pady=5)
        ttk.Button(root, text="=", width=14, command=self.calcular, bootstyle="success").pack(pady=5)

        # Resultado label
        self.label_resultado = ttk.Label(root, text="Resultado: ", font=("Arial", 12, "bold"), bootstyle="success")
        self.label_resultado.pack(pady=10)

    def adicionar(self, valor):
        if valor == "√":
            self.display_var.set(f"√({self.display_var.get()})")
        else:
            self.display_var.set(self.display_var.get() + valor)

    def limpar(self):
        self.display_var.set("")
        self.label_resultado.config(text="Resultado: ")

    def calcular(self):
        expressao = self.display_var.get()
        try:
            if "√" in expressao:
                # Extrair número dentro da raiz
                numero = expressao.replace("√(", "").replace(")", "")
                resultado = self.calc.raiz_quadrada(float(numero))
            elif "/" in expressao:
                a, b = map(float, expressao.split("/"))
                resultado = self.calc.dividir(a, b)
            elif "*" in expressao:
                a, b = map(float, expressao.split("*"))
                resultado = self.calc.multiplicar(a, b)
            elif "-" in expressao and expressao.count("-") == 1:
                a, b = map(float, expressao.split("-"))
                resultado = self.calc.subtrair(a, b)
            elif "+" in expressao:
                a, b = map(float, expressao.split("+"))
                resultado = self.calc.somar(a, b)
            else:
                resultado = float(eval(expressao))
            
            self.label_resultado.config(text=f"Resultado: {resultado}")
            self.display_var.set(str(resultado))
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
        except Exception:
            messagebox.showerror("Erro", "Expressão inválida.")

# --- Execução ---
if __name__ == "__main__":
    root = ttk.Window(themename="superhero")
    CalculadoraGUI(root)
    root.mainloop()
