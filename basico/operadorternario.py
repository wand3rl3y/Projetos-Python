login = False

msg = "Usuario Logado" if login else "Usuar precisa logar"
print(msg)

idade = input("Qual a sua idade ")
if not idade.isnumeric():
    print("Digite numeros idiota")
else:
    idade = int(idade)
    mensagem = "Pode Entrar" if (idade >= 18) else "Menor de idade "
    print(mensagem)

