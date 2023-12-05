import os
print ('Bem Vindo ao sistema de Notas')
print ('='* 50)

def media(nota1,nota2):
    media = (nota1 + nota2)/2
    return media

while True:
   Nome = input('Digite o nome do aluno: ')
   if Nome.isalpha():
      break
   else:
      print ('Nome invalido,digite o nome do aluno novamente(Não utilize números): ')
   
while True: 
  try:
    nota1 = float(input('Digite a primeira nota: '))
    if 0 <=  nota1 <= 10:
      break
    else:
      os.system('cls')
      print ('Primeira nota invalida,digite as notas novamente(Nota maxima:10): ')
  except ValueError:
    os.system('cls')
    print('A primeira nota digitada não foi um numero,digite a nota novamente(Digite apenas números):')


while True:
  try:
    nota2 = float(input('Digite a segunda nota: '))
    if 0 <= nota2 <= 10:
      break
    else:
      os.system('cls')
      print ('segunda nota invalida,digite as notas novamente(Nota maxima:10): ')
  except ValueError:
    os.system('cls')
    print('A segunda nota digitada não foi um numero,digite a nota novamente(Digite apenas números):')
    os.system('cls')



if 10 >= (media(nota1,nota2)) >= 9:
  print ('='* 50)
  print (Nome)
  print ((media(nota1,nota2)))
  print('Aprovado')
  print('Conceito A')
  print ('Obrigado')
  print ('='* 50)

 
elif 9 > (media(nota1,nota2)) >= 7:
     print ('='* 50)
     print (Nome)
     print (media(nota1,nota2))
     print('Aprovado')
     print('Conceito B')
     print ('Obrigado')
     print ('='* 50)

if 7 > (media(nota1,nota2)) >= 6:
     print ('='* 50)
     print (Nome)
     print (media(nota1,nota2))
     print('Recuperação')
     print('Conceito C')
     print ('Obrigado')
     print ('='* 50)
    

if (media(nota1,nota2)) < 6:
     print ('='* 50)
     print (Nome)
     print ((media(nota1,nota2)))
     print('Reprovado')
     print('Conceito D')
     print ('Obrigado')
     print ('='* 50)
    


