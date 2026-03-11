import random

print("🎮 Bem-vindo ao Jogo de Adivinhação!")
print("Tente adivinhar o número entre 1 e 100.")

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("🔼 O número é MAIOR.")
    elif palpite > numero_secreto:
        print("🔽 O número é MENOR.")
    else:
        print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas.")
        break