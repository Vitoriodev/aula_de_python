from login import email
from login import senhar
from login import nome

import login

while True: #verificação do email e a senhar.
    verificacao_1 = input("qual o seu email: ")

    if verificacao_1 == email:
        
        while True:
            verificacao_2 = input("qual a sua senhar: ")
            
            if  verificacao_2 == senhar:
                print(f"Sejam bem-vindo {nome}")
                break
            else: #ser a senhar for errada ela vem aqui.
                print("a sua senhar deu errado por favor tente novamente")
                continue
    else: #ser o email for errado ele vem pra aqui.
        print("o seu gmail deu errado por favor tente novamente")
        continue
    
    break
