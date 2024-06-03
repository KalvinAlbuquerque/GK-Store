import BTreeBiblioteca as bt
# #Execução
Ap = None
chave = 1


#Menu
print("Bem-vindo, o que deseja realizar?")
menu = True
while menu:
  cmd = int(input("\nMenu de opções\n\n0 - Sair, 1 - Inserir, 2 - Pesquisar,\n 3 - Imprimir em-ordem, 4 - Imprimir valores menores que uma chave, 5 - Imprimir valores maiores que uma chave, 6 - Imprimir menores Dataframe, 7 - Imprimir maiores Datafreme.\n\nEscolher:"))
  print("\n")
  if cmd == 0:
    print("Programa finalizado. ")
    menu = False
  elif cmd == 1:
    Ap, chave, df = bt.Inserir(Ap, chave)
  elif cmd == 2:
    reg = bt.Registro()
    reg.Chave = int(input("\nDigite uma chave maior que zero: "))
    reg = bt.Pesquisa(reg,Ap)
    if reg != None:
      print(reg.Chave, "-", reg.Elemento)
  
        
  elif cmd == 3:
    bt.Imprime(Ap)
  elif cmd == 4:
    reg = bt.Registro()
    reg.Chave = int(input("\nDigite uma chave maior que zero: "))
    bt.ImprimeMenor(reg, Ap)
  elif cmd == 5:
    reg = bt.Registro()
    reg.Chave = int(input("\nDigite uma chave maior que zero: "))
    bt.ImprimeMaior(reg, Ap)
  elif cmd == 6:
    reg = bt.Registro()
    reg.Chave = int(input("\nDigite uma chave maior que zero: "))
    bt.ImprimeMenorDataFrame(reg, Ap, df)
  elif cmd == 7:
    reg = bt.Registro()
    reg.Chave = int(input("\nDigite uma chave maior que zero: "))
    bt.ImprimeMaiorDataFrame(reg, Ap, df)
  else:
    print("Comando inexistente.")