while True:
    print("ola sejam ben-vindo")
    print("podemos fazer o seu cadrasto")
    
    nome = input("qual o seu nome: ")
    email = input("qual vai ser o seu email: ")
    senhar = input("qual vai ser a sua senhar: ")
    
    while True:
        con_senhar = input("confirmer a sua senhar: ")
        
        if senhar != con_senhar:
            print("a confirmação de senhar não estão iguais!")
            print("por favor tente novamente")
            continue
        else:
            break
    
    break

print(f"o seu email é {email}")
print(f"a sua senhar é {senhar}")