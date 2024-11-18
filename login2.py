tentativas=3

while tentativas>0:
    email=input("EMAIL: ")
    senha=input("SENHA: ")
    if email=="22@malucao.com" and senha=="22maluco":
        print("login com sucesso")
        break
    tentativas=tentativas-1
    if email!="22@malucao.com" and senha!="22maluco":
        print("login invalido")
    elif email!="22@malucao.com":
        print("Email invalido")
    else:
        print("senha invalida")
    if tentativas==0:
        print("Conta bloqueada, Tente novamente mais tarde.")