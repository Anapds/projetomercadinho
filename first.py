bd_produtos = list()

#-----------------------------cadastrar produto-------------------------------
def cadastrar_produto(cod, nome, valor):
  #Verifivar se não existe o produto
  if not existe_produto(cod):
    #Cria o dicionario e passa os respectivos valores
    produto = {
      "cod" : cod,
      "nome" : nome,
      "valor" : valor
    }
    #Verifica a quantidade de itens antes de cadastrar
    qtd_antes_bd = len(bd_produtos)
    #Para cadastrar precisa de uma copia dos dados
    bd_produtos.append(produto.copy())
    #Depois apagar o dicionario para que ele possa ser usado posteriormente
    produto.clear()
    #Verificar a quantidade de itens depois de cadastrar 
    qtd_depois_bd = len(bd_produtos)

    #Caso produto seja cadastrado retorna TRUE 
    if qtd_depois_bd > qtd_antes_bd:
      return True
    #Se NADA acontecer retorna falso
  return False

#-----------------------------buscar produto----------------------------------
def buscar_produto(cod):
  for produto in bd_produtos:
    if produto["cod"] == cod:
      return produto
      break

#-----------------------------existe produto?---------------------------------
def existe_produto(cod):
  for produto in bd_produtos:
    if produto["cod"] == cod:
      return True
      break
  return False
  
#-----------------------------remover produto--------------------------------- 
def remover_produto(cod):
  if existe_produto(cod):
    aux_prod = buscar_produto(cod)
    bd_produtos.remove(aux_prod)
    return True
  return False

 #---------------------Atualizar produto---------------------------------
def atualizar_produto_completo(cod, novo_nome, novo_valor):
  if existe_produto(cod):
    for produto in bd_produtos:
      if produto["cod"] == cod:
        produto["nome"] = novo_nome
        produto["valor"] = novo_valor
        return True
  return False
  

#testando as funções
#teste manual explicito
#testo direto do cadastrar, tem que ter tudo correto
cadastrar_produto(1, "Arroz", 4.99)
cadastrar_produto(3, "Feijão", 8.99)
cadastrar_produto(4, "Macarrão", 3.99)
#lista de produtos
print(bd_produtos)

#testando o remover produtos pelo codigo
print(remover_produto(4))
#lista os produtos
print(bd_produtos)

#teste manual
#primeiro for serve para repedir a quantidade de cadastros

for i in range(0, 1):
  #esse while repete ate a pessoa cadastrar corretamente.
  while True:
    try:
      cod = int(input("Informe o cod do produto: "))
      nome = int(input("Informe o nome do produto: "))
      valor = float(input("Informe o valor: "))
      if cadastrar_produto(cod, nome, valor):
        print("Produto cadastardo com sucesso!")
        break

      else: 
        print("Ja existe um produto com esse código cadastrado.")
        continue

    except:
      print("Dados inválidos, digite novamente as informações. ")
print(bd_produtos)

#testando o atualizar
for i in range(0,1):
   while True:
     try:
       if atualizar_produto_completo(1, "Arroz tio joão", 5.25):
         print("Produto atualizado")
         break
       else:
        print("O produto não existe")

     except:
        print("Dados invalidos, digite novamente!")