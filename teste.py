frase = "ola como vai vou esta fazendo um teste aqui"

i= 0
teste = 0
letra = ""

while i < len(frase):
    mostra_cada_letra = frase[i]
    
    numeros_das_letras = frase.count(mostra_cada_letra)
    
    if (mostra_cada_letra == " "):
        i += 1
        continue
    
    if(numeros_das_letras > teste):
        
        teste = numeros_das_letras
        
        letra = mostra_cada_letra
    
    
    
    #print(mostra_cada_letra, numeros_das_letras)
    
    i += 1
    
print(letra, teste)