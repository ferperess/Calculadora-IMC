print ("\n<<<<< CALCULADORA DE IMC >>>>>".center(50))

print ("\nOlá! Seja bem-vindo(a) a Calculadora de IMC")

nome = input ("\nPor favor, digite seu nome: ")
altura = float (input(f"Muito bem, {nome}. Agora digite sua altura em metros: "))
peso = float (input("Para finalizar, digite seu peso em kg: "))

imc = peso / (altura **2)

print (f"\n{nome}, seu IMC é {imc:.2f}.")

if imc <= 16.9:
    print("Sua saúde pode estar comprometida. Tente procurar ajuda!")
elif imc > 16.9 and imc < 18.5:
    print("Você está um pouco abaixo do padrão de saúde.")
elif imc >= 18.5 and imc < 25:
    print("Muito bem! Você está com um IMC adequado aos padrões de saúde.")
elif imc == imc >= 25 and imc < 30:
    print("Cuidado, você está um pouco acima do padrão de saúde.")
elif imc == imc >= 30 and imc < 35:
    print("Tente procurar ajuda, você já está com obesidade grau 1.")
elif imc == imc >= 35 and imc <= 40:
    print("Você está com obesidade grau 2. Procure ajuda!")
else:
    print("Procure ajuda imediatamente! Você se encontra no maior grau de obesidade.")