# Luiz Miguel da Rocha Muller
# Rithiély Schmitt
inserir = []
y = []
refazer = []
pilha_invertida = []
string_invertida = ""
string_normal = ""

for x in range(0,3):
    comando = input("Você quer inserir, desfazer ou refazer?")
    if comando == "inserir":
        algo = input("Insira alguma palavra: ")
        for x in algo:
            inserir.append(x)
        while inserir:
            string_invertida = string_invertida + inserir.pop()
        pilha_invertida = string_invertida

    elif comando == "desfazer":
        if pilha_invertida:  
            print(inserir) ## ficou vazia após a troca de pilha inserir para pilha invertidq

    elif comando == "refazer":
        for palavra in pilha_invertida:
            refazer.append(palavra)
        while refazer:
            string_normal = string_normal + refazer.pop() 
            # tira cada ultimo item da pilha refazer e coloca na variavel string, ordenando elas novamente
            y = string_normal
        print(y)
