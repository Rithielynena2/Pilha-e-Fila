# Luiz Miguel da Rocha Muller
# Rithiély Schmitt

from datetime import datetime, timedelta

seis = datetime.now().replace(hour=18, minute=0, second=0)
sete = seis + timedelta(hours=1)
fila = []
senha = 1

def chamar_cliente():
    if fila:
        senha_chamada = fila.pop(0)
        print(f"Senha {senha_chamada}, por favor compareça ao caixa.")
    else:
        print("Não há senhas na fila.")

def tirar_senha():
    global senha
    tirar = int(input("Você deseja retirar uma senha? Digite 1 para sim e 2 para não."))
    if tirar == 1:
        if datetime.now() < seis:
            fila.append(senha)
            print(f"Senha {senha} retirada.")
            senha = senha + 1
        elif datetime.now() >= seis and datetime.now() < sete:# Se a hora de agora for maior que a horario_fechamento avisa que acabou 
            print("Horário de retirada de senhas encerrado.")
        else:
            fila.clear()
            print("Horário de atendimento encerrado. Volte amanha! ")
    elif tirar ==2:
        print("Volte sempre!")
    else:
        print("Resposta inválida, digite apenas '1' ou '2'.")

tirar_senha()
tirar_senha()
tirar_senha()
tirar_senha()
tirar_senha()
chamar_cliente()
chamar_cliente()
print(fila)