emailc="22@malucao.com"
senhac="22maluco"
email="22"
senha="22"
contar_tentativas=0
while email!=emailc and senha!=senhac:
    email=input("Introduza seu email: ")
    senha=input("Introduza sua senha: ")
    contar_tentativas=contar_tentativas+1
    if contar_tentativas>2:
        print("Conta Bloqueada, Tente novamente mais tarde.")
        break
    if email!=emailc and senha!=senhac:
        print("Login Falhou")
    elif email!=emailc:
        print("Email invalido")
    elif senha!=senhac:
        print("Senha invalida")
if emailc==email and senha==senhac:
    print("Login Realizado")