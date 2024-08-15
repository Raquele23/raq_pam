login = "admin"
senha = "123"
loginPessoa = input("Digite seu login: ")
senhaPessoa = input("Digite sua senha: ")
if loginPessoa == login and senhaPessoa == senha:
    print("Olá admin, seja bem-vindo!")
else:
    print("login ou senha incorretos, tente novamente.")