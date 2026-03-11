import tkinter as tk
import random
from PIL import Image, ImageTk

numero_secreto = random.randint(1, 100)
tentativas = 0
palpites = []

def verificar(event=None):
    global tentativas, numero_secreto, palpites

    try:
        palpite = int(entrada.get())
    except:
        resultado.config(text="❌ Digite um número válido!", fg="red")
        return

    tentativas += 1
    palpites.append(palpite)

    tentativas_label.config(text=f"Tentativas: {tentativas}")
    historico_label.config(text="Palpites: " + ", ".join(map(str, palpites)))

    if palpite < numero_secreto:
        resultado.config(text="🔼 O número é MAIOR", fg="blue")

    elif palpite > numero_secreto:
        resultado.config(text="🔽 O número é MENOR", fg="orange")

    else:
        resultado.config(
            text=f"🏆 VOCÊ GANHOU!\nNúmero correto: {numero_secreto}\nTentativas: {tentativas}",
            fg="green"
        )

    entrada.delete(0, tk.END)

def reiniciar():
    global numero_secreto, tentativas, palpites

    numero_secreto = random.randint(1, 100)
    tentativas = 0
    palpites = []

    entrada.delete(0, tk.END)
    resultado.config(text="Novo jogo iniciado!", fg="black")
    tentativas_label.config(text="Tentativas: 0")
    historico_label.config(text="Palpites:")


# Janela
janela = tk.Tk()
janela.title("🎮 Jogo de Adivinhação")
janela.geometry("420x520")
janela.config(bg="#f0f0f0")

# ENTER para jogar
janela.bind("<Return>", verificar)

# IMAGEM
imagem = Image.open("imagens/jogo-adivinhacao.png")
imagem = imagem.resize((150,150))
foto = ImageTk.PhotoImage(imagem)

label_imagem = tk.Label(janela, image=foto, bg="#f0f0f0")
label_imagem.pack(pady=5)

# Título
titulo = tk.Label(
    janela,
    text="🎮 Jogo de Adivinhação",
    font=("Arial", 18, "bold"),
    bg="#f0f0f0"
)
titulo.pack(pady=10)

# Instrução
instrucao = tk.Label(
    janela,
    text="Adivinhe o número entre 1 e 100",
    font=("Arial", 12),
    bg="#f0f0f0"
)
instrucao.pack()

# Entrada
entrada = tk.Entry(janela, font=("Arial", 14), justify="center")
entrada.pack(pady=10)

# Botão tentar
botao = tk.Button(
    janela,
    text="Tentar",
    font=("Arial", 12),
    bg="#4CAF50",
    fg="white",
    width=15,
    command=verificar
)
botao.pack(pady=5)

# Botão reiniciar
reiniciar_btn = tk.Button(
    janela,
    text="Reiniciar Jogo",
    font=("Arial", 10),
    width=15,
    command=reiniciar
)
reiniciar_btn.pack(pady=5)

# Tentativas
tentativas_label = tk.Label(
    janela,
    text="Tentativas: 0",
    font=("Arial", 11),
    bg="#f0f0f0"
)
tentativas_label.pack(pady=5)

# Histórico
historico_label = tk.Label(
    janela,
    text="Palpites:",
    font=("Arial", 11),
    bg="#f0f0f0",
    wraplength=350
)
historico_label.pack(pady=5)

# Resultado
resultado = tk.Label(
    janela,
    text="",
    font=("Arial", 12, "bold"),
    bg="#f0f0f0"
)
resultado.pack(pady=10)

janela.mainloop()