while True:
    '''
    sempre tem como melhorar isso.
    
    '''
    
    print('\nmetodos de calculos são, +, *, / e -')
    
    metodo_de_calculo = input('qual o metodo vai querer usar para o seu calculo? ').lower()  
    
    #teste para saber, ser o codigo vai ter os operadores aritmético e vai ter um operado aritmético.
    if '+-*/' not in metodo_de_calculo:
        print('coloque apenas operadores aritmético!')
    
    if len(metodo_de_calculo) > 1:
        print('\naconteceu um erro, coloque apenas um metodo de calculo!')
        continue
    
    
    # parte que vai ser usada para fazer os calculos
    if '+' in metodo_de_calculo:
        
        soma = input('quantas somas você quer fazer? ')
        
        if '2' in soma:
            
            try:            
                soma_1 = int(input('qual vai ser o numero da soma? '))
            
                soma_2 = int(input('qual vai ser o outro numero? '))
                        
                total = soma_1 + soma_2
                
                                                
            except:
                
                print('aconteceu um erro, porfavor coloque apenas numeros!')
                continue
                
                
            print(f'o total da soma entre o numero {soma_1} e {soma_2} e o resultado é {total}')
        
        if '3' in soma:
            try:
                soma_1 = int(input('qual vai ser o numero da soma? '))
            
                soma_2 = int(input('qual vai ser o proximo numero? '))
            
                soma_3 = int(input('qual vai ser o proximo numero? '))
            
                total = soma_1 + soma_2 + soma_3
            
            except: 
                
                print('aconteceu um erro, porfavor coloque apenas numeros!')
                continue
            
            print(f'o total da soma entre os numeros {soma_1}, {soma_2} e {soma_3} o resultado é {total}')
        
        
    if '*' in metodo_de_calculo:
        
        multiplicação = input('quauntas multiplicaçao vai fazer? ')
        
        if '2' in multiplicação:
            try:
                mul_1 = int(input('qual vai ser o primeiro? '))
                    
                mul_2 = int(input('qual vai ser o proximo numero? '))
            
                total = mul_1 * mul_2
            except: 
                
                print('aconteceu um erro, porfavor coloque apenas numeros!')
                continue

            print(f'o total da multiplicação entre o numero {mul_1} e {mul_2} e o resultado é {total}')
        
        if '3' in multiplicação:
            try:
                mul_1 = int(input('qual vai ser o primeiro? '))
                    
                mul_2 = int(input('qual vai ser o proximo numero? '))
            
                mul_3 = int(input('qual vai ser o proximo numero? '))
            
                total = mul_1 * mul_2 * mul_3
            except: 
                
                print('aconteceu um erro, porfavor coloque apenas numeros!')
                continue

            print(f'o total da multiplicação entre os numeros {mul_1}, {mul_2} e {mul_3} o resultado é {total}')
                      
                       
    if '/' in metodo_de_calculo:
        
        divisão = input('quauntas divisão vai fazer? ')
        
        if '2' in divisão:
            try:
                divi_1 = int(input('qual vai ser o primeiro? '))
                    
                divi_2 = int(input('qual vai ser o proximo numero? '))
            
                total = divi_1 / divi_2
            except: 
                
                print('aconteceu um erro, porfavor coloque apenas numeros!')
                continue

            print(f'o total da divisão entre o numero {divi_1} e {divi_2} e o resultado é {total}')
        
        if '3' in divisão:
            try:
                divi_1 = int(input('qual vai ser o primeiro? '))
                    
                divi_2 = int(input('qual vai ser o proximo numero? '))
            
                divi_3 = int(input('qual vai ser o proximo numero? '))
            
                total = divi_1 / divi_2 / divi_3
            except: 
                
                print('aconteceu um erro, porfavor coloque apenas numeros!')
                continue

            print(f'o total da divisão entre os numeros {divi_1}, {divi_2} e {divi_3} o resultado é {total}')
        
    if '-' in metodo_de_calculo:
        
        subtração = input('quauntas subtração vai fazer? ')
        
        if '2' in subtração:
            try:
                sub_1 = int(input('qual vai ser o primeiro? '))
                    
                sub_2 = int(input('qual vai ser o proximo numero? '))
            
                total = sub_1 - sub_2
            except: 
                
                print('aconteceu um erro, porfavor coloque apenas numeros!')
                continue

            print(f'o total da subtração entre o numero {sub_1} e {sub_2} e o resultado é {total}')
        
        if '3' in subtração:
            try:
                sub_1 = int(input('qual vai ser o primeiro? '))
                    
                sub_2 = int(input('qual vai ser o proximo numero? '))
            
                sub_3 = int(input('qual vai ser o proximo numero? '))
            
                total = sub_1 - sub_2 - sub_3
            except: 
                
                print('aconteceu um erro, porfavor coloque apenas numeros!')
                continue

            print(f'o total da subtração entre os numeros {sub_1}, {sub_2} e {sub_3} o resultado é {total}')
    
    
    #fechar o while.
    sair =  input('você quer sair, sim ou não: ').lower().startswith('s')
    
    if sair is True:
        break

print('você saiu da calculatora espero que volte! ')