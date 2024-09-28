#Andressa de Oliveira Barros
#Melissa Weiss Perussulo
produtos = [[ 1, "Coca-cola", 3.75, 2],
  [2, "Pepsi", 3.67, 5],
  [3, "Monster", 9.96, 0],
 [4,"Café", 1.25, 100],
 [5, "Redbull", 13.99, 2]]

notas = [[200, 0], 
         [100, 0], 
         [50, 10], 
         [20, 10], 
         [10, 10], 
         [5, 10],
         [2, 10], 
         [1, 10], 
         [0.50, 10], 
         [0.25, 10], 
         [0.10, 10], 
         [0.05, 10]]

def produtosDisp(produtos):#Atualiza o estoque
  for i in range(len(produtos)):
    if produtos[i][3] > 0:#pra conferir se o produto tem no estoque
      print(f"ID-{produtos[i][0]} {produtos[i][1]}")

    else:#Se não tiver no estoque
      print(f"Produto {produtos[i][1]} indispnível! ")

# adicional para editar os produtos
def editarProduto(produtos):
  idProduto = int(input("Digite o ID do produto que deseja editar: "))
  # verifica se o id existe e se nao ele para
  if idProduto > len(produtos) or idProduto < 1:
    print("ID inválido!")
    return
    # id do produto que deseja editar
  produto = produtos[idProduto - 1]
  op = input("Deseja editar qual atributo? (nome, preco, quantidade): ")
  if op == "nome":
    novoNome = input("Digite o novo nome: ")
    produto[1] = novoNome
  elif op == "preco":
    novoPreco = float(input("Digite o novo preço: "))
    produto[2] = novoPreco
  elif op == "quantidade":
    novaQuantidade = int(input("Digite a nova quantidade: "))
    produto[3] = novaQuantidade
  else:
    print("Opção inválida!")
    return
  print(f"Produto atualizado com sucesso!")

# remover produto
def removerProduto(produtos):
  idProduto = int(input("Digite o ID do produto que deseja remover: "))
  if idProduto > len(produtos) or idProduto < 1:
    print("ID inválido!")
    return
  produtos.pop(idProduto - 1)
  print("Produto removido com sucesso!")

def cadastrarProduto(produtos):
  novoID = len(produtos) + 1 #cadastrar um novo id na matriz
  nome = input("Digite o nome do produto: ")
  preco = float(input("Digite o preço do produto: "))
  quantidade = int(input("Digite a quantidade do produto: "))
  produtos.append([novoID, nome, preco, quantidade])
  print(f"Produto {nome} cadastrado com sucesso!")

def modoAdministrador(produtos):
  while True:#Loop para o modo administrador
    print("--------------------------------------------")
    print("Menu Administrador")
    print("1 - Cadastrar Produto")
    print("2 - Editar Produto")
    print("3 - Remover Produto")
    print("4 - Voltar")
    print("--------------------------------------------")
    op = input("Digite a opção desejada: ")
    if op == "1":
      cadastrarProduto(produtos)
    elif op == "2":
      editarProduto(produtos)
    elif op == "3":
      removerProduto(produtos)
    elif op == "4":
      break
    else:
      print("Opção inválida!")

while True:#Loop para o modo cliente
  print("--------------------------------------------")
  print("Bem-vindo(a), aqui está a lista de produtos!")
  print("--------------------------------------------")
  produtosDisp(produtos)
  print("---------------------------------------------")
  senha = input("Digite a senha para acessar o modo administrador (ou digite 'cliente' para continuar): ")
  if senha == "admin":
    modoAdministrador(produtos)
  elif senha == "cliente":
    print("--------------------------------------------")
    idCliente = int(input("Digite o ID do produto: "))
    produtoEscolhido = produtos[idCliente - 1]#definir o produto escolhido pela linha da matriz
    if idCliente > produtoEscolhido[0] or idCliente < 1:
      print("ID inválido, digite novamente")
      idCliente = int(input("Digite o ID do produto: "))

    else: 
      if produtoEscolhido[3] <= 0:#Conferir se o produto está disponível
        print("Produto indisponível")

      else: 
        print(f"Você comprou {produtoEscolhido[1]} ")
        produtoEscolhido[3] -= 1
        print("--------------------------------------------")
        print(f"Agora temos {produtoEscolhido[3]} unidades de {produtoEscolhido[1]}")
        print("--------------------------------------------")
        print(f"Valor: R${produtoEscolhido[2]}")
        print("--------------------------------------------")
        valorPago = float(input("Digite o valor pago: "))
        if valorPago >= produtoEscolhido[2]:#Conferir se o valor pago é maior ou igual ao valor do produto
          troco = valorPago - produtoEscolhido[2]

          for nota in range(len(notas)):#verifica se o troco é possivel
            valorNota = notas[nota][0]#variavel para verificar o valor da nota
            qtNota = notas[nota][1]#variavel para verificar a quantidade de notas
            if qtNota > 0:#caso o troco seja possível e tenha notas disponíveis
              if troco > 0:#loop até zerar o troco
                if troco >= valorNota:#Encotrar uma igual ou menor que o troco
                  qtdeNotas = troco // valorNota#calcula a quantidade de not
  #atualiza a quantidade de notas
                  qtNota -= 1 #atualiza a quantidade de notas
                  troco -= qtdeNotas * valorNota#calcula o valor total do troco
                  print(f"Você recebeu {qtdeNotas} notas de {valorNota}")

            else:
              print("---------------------------------------------------")
              print(f"Nota de {valorNota} indisponível, compra cancelada!")
              produtoEscolhido[3] += 1#caso não tenha notas disponíveis, o produto é devolvido

        else:
          print("Valor insuficiente, digite novamente ")
          valorPago = float(input("Digite o valor pago: ")) 

