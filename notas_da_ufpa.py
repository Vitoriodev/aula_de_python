# pegunta qual o nome do aluno e as notas para joga no sistema.
nome = input('ola seja bem-vindo qual é o seu nome? ')

prova_1 = int(input('qual foi a nota da sua primeira avaliação? '))

prova_2 = int(input('qual foi a nota da sua segunda avaliação? '))

prova_3 = int(input('qual foi a nota da sua terceira avaliação? '))

# mostra o resultado do sistema.
print(' seja bem-vindo para disposições das notas.')

primeira_avaliação = prova_1

segunda_avaliação = prova_2

terceira_avaliação = prova_3

MEDIA = (primeira_avaliação + segunda_avaliação + terceira_avaliação)/3

if MEDIA >= 9:
  print(f'olá {nome}, parabens você foi "exelente" ')

if MEDIA >= 7 and MEDIA < 9:
  print(f'olá {nome} o teu resultado foi "bom"')
  
if MEDIA >= 5 and MEDIA < 7:
  print(f'olá {nome} o seu resultado foi "regula"')

if MEDIA < 5:
  print(f'olá {nome} o seu resultado foi "insuficiente"')