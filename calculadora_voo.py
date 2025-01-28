import tkinter as tk
from tkinter import messagebox
import json

# Carregar dados das aeronaves
with open("aircraft_data.json", "r") as file:
    aircraft_data = json.load(file)

# Função para calcular velocidades e combustível
def calculate():
    aircraft = aircraft_var.get()
    weight = float(weight_entry.get())
    fuel = float(fuel_entry.get())
    origin = origin_entry.get()
    destination = destination_entry.get()

    # Verificar se o peso está dentro dos limites
    if weight > aircraft_data[aircraft]["max_takeoff_weight"]:
        messagebox.showerror("Erro", "Peso excede o máximo de decolagem!")
        return

    # Calcular velocidades
    V1 = aircraft_data[aircraft]["V1"]
    VR = aircraft_data[aircraft]["VR"]
    V2 = aircraft_data[aircraft]["V2"]

    # Calcular combustível necessário (exemplo simples)
    distance = 500  # Distância fictícia em km
    fuel_consumption = aircraft_data[aircraft]["fuel_consumption"]
    fuel_needed = (distance / 100) * fuel_consumption  # Exemplo de cálculo

    # Exibir resultados
    result_text = f"""
    Velocidades:
    - V1: {V1} nós
    - VR: {VR} nós
    - V2: {V2} nós

    Combustível necessário: {fuel_needed:.2f} litros
    """
    messagebox.showinfo("Resultados", result_text)

# Interface gráfica
root = tk.Tk()
root.title("Calculadora de Voos")

# Seleção de aeronave
tk.Label(root, text="Aeronave:").grid(row=0, column=0)
aircraft_var = tk.StringVar(value="C152")
aircraft_menu = tk.OptionMenu(root, aircraft_var, *aircraft_data.keys())
aircraft_menu.grid(row=0, column=1)

# Entrada de peso
tk.Label(root, text="Peso (kg):").grid(row=1, column=0)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1)

# Entrada de combustível
tk.Label(root, text="Combustível (litros):").grid(row=2, column=0)
fuel_entry = tk.Entry(root)
fuel_entry.grid(row=2, column=1)

# Entrada de origem e destino
tk.Label(root, text="Origem:").grid(row=3, column=0)
origin_entry = tk.Entry(root)
origin_entry.grid(row=3, column=1)

tk.Label(root, text="Destino:").grid(row=4, column=0)
destination_entry = tk.Entry(root)
destination_entry.grid(row=4, column=1)

# Botão de cálculo
tk.Button(root, text="Calcular", command=calculate).grid(row=5, column=0, columnspan=2)

root.mainloop()