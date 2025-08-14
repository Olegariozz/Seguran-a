# 📜 Descrição do Código

Este código em Python solicita o nome e a idade de uma pessoa e verifica se ela pode entrar em uma festa.  
Se for menor de idade, é barrada; se for maior ou igual a 18 anos, é liberada.

## 🚀 Como funciona
1. O programa pede:
   - Nome do usuário (`input` como string)
   - Idade (`input` convertido para `int`)
2. Verifica com uma estrutura condicional:
   - **Idade menor que 18** → Acesso negado e mensagem de retorno futuro 👴
   - **Idade maior ou igual a 18** → Acesso liberado com aviso para se divertir e se proteger 💃
3. Em ambos os casos, exibe uma linha de separação e agradece pelo uso do sistema.

## 📌 Código
```python
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade < 18:
    print(f"{nome}, você não pode entrar nessa festa, volte daqui alguns anos 👴")
    print("==================================================")
    print("Obrigado por usar o sistema de controle de entrada!")
else:
    if idade >= 18:
        print(f"{nome}, você pode entrar na festa! Vai ser feliz e se proteja💃!")
        print("==================================================")
        print("Obrigado por usar o sistema de controle de entrada!")
```

## 🖥️ Exemplo de uso
**Entrada:**
```
Digite seu nome: Lucas
Digite sua idade: 17
```

**Saída:**
```
Lucas, você não pode entrar nessa festa, volte daqui alguns anos 👴
==================================================
Obrigado por usar o sistema de controle de entrada!
```

## 🛠️ Observações
- A idade é convertida para `int`, pois só aceita números inteiros.
- O bloco `else` poderia ser simplificado, já que a condição interna `if idade >= 18` é redundante.
- Os emojis deixam o programa mais divertido, mas são opcionais.
