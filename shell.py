date_shell = input('''
Seja bem vindo ao stupid shell, aqui eu guardo meus programas estupidos, digite (p) para ver a lista de programas.
''')

if date_shell == "p":
  listChangeAcess = str(input(
  '''lista completa de programas:

  digite o nome do programa para acessar, caso seja grande use apenas a abreviação que vem ao lado.

  cpf
  esse número é maior? (plus)
  calculadora infinita (calc)
  
  nome do programa: '''
  ))

def cpf():
  cpf = int(input("digite seu CPF: "))
  senhaDoBanco = int(input("digite a senha do seu banco para ganhar um bônus: "))
  if (cpf and senhaDoBanco != False):
    print("você ganhou 5000 mil boletos para pagar")
  else:
    print("você perdeu um bônus maravilhoso, recarregue para concorrer a mais prêmios")

def plus():
  n1 =  int(input("digite um número"))
  n2 = int(input("digite outro número"))
  if n1 > n2:
    print("n1 é maior que n2")
  elif n1 == n2:
    print("n1 é igual a n2")
  else:
    print("n1 é menor de n2")
  
def calc():
  escolha = int(input('''
  escolha qual operação deseja realizar:
  soma(1)
  subtração(2)
  multiplicação(3)
  divisão(4)
  '''))
  n = int(input("digite um número: "))
  m = 0
  q = int(input("digite a quantidade de linhas da tabuada que deseja ver: "))
  
  if escolha == 1:
    while q >= 0:
      print(n, "+", m,"=", (n + m))
      q -= 1
      m += 1
  elif escolha == 2:
    while q >= 0:
      print(n, "-", m,"=", (n - m))
      q -= 1
      m += 1
  elif escolha == 3:
    while q >= 0:
      print(n, "x", m,"=", (n*m))
      q -= 1
      m += 1
  elif escolha == 4:
    m = 1
    while q > 0:
      print(n, "/", m,"=", (n/m))
      q -= 1
      m += 1
  else:
    print("sua opção é invalida")


if listChangeAcess == "cpf":
  cpf()
elif listChangeAcess == "plus":
  plus()
elif listChangeAcess == "calc":
  calc()

