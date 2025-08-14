nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade < 18:
    print(f"{nome}, você não pode entrar nessa festa, volte daqui alguns anos 👴3e")
    print("==================================================")
    print("Obrigado por usar o sistema de controle de entrada!")
else:
    if idade >= 18:
        print(f"{nome}, você pode entrar na festa! Vai ser feliz e se proteja💃!")
        print("==================================================")
        print("Obrigado por usar o sistema de controle de entrada!")