
def partida():

    n=int(input("Quantas peças? "))
    m=int(input("Limite de peças por jogada? "))
    entre=0
    if n%(m+1)==0:
        print("Você começa!")
        entre=1
    else:
        print("Computador começa!")
    while n>0:
        if entre==1:
            n=n-usuario_escolhe_jogada(n,m)
            if n>0:
                v=n=n-computador_escolhe_jogada(n,m)
        else:
            v=n=n-computador_escolhe_jogada(n,m)
            if n>0:
                n=n-usuario_escolhe_jogada(n,m)                   
    else:
        if v<=0:
            print("Fim de jogo! O computador ganhou!")
            return 0

        else:
            print("Você ganhou!")
            return 1

def computador_escolhe_jogada(n,m):
    pecas=0
    if n>m:
        if (n-m)%(m+1)==0:
            pecas=m
        elif(n-(m-1))%(m+1)==0:
            pecas=m-1
        else:
            pecas=1
        print("O computador tirou",pecas,"peças.")
        
    else:
        print("O computador tirou",n,"peças.")
        pecas=n
    if n-pecas==1:
        print("Agora resta apenas uma peça no tabuleiro.")
    elif n-pecas>0:
        print("Agora restam apenas",n-pecas,"peças no tabuleiro.")
    return pecas        

def usuario_escolhe_jogada(n,m):
    t=int(input("Quantas peças você vai tirar? "))
    while t>m or t>n or t<=0:
        print("Oops! Jogada inválida! Tente de novo.")
        t=int(input("Quantas peças você vai tirar? "))
    else:
        if t==1:
            print("Você tirou uma peça")
            if n-t==1:
                print("Agora resta apenas uma peça no tabuleiro.")
            elif n-t>0:
                print("Agora restam apenas",n-t,"peças no tabuleiro.")
        else:
             print("Você tirou ",t,"peças.")
             if n-t>0:
                 print("Agora restam ",n-t,"peças no tabuleiro.")
    return t

def campeonato():
        passo=1
        voce=0
        computador=0
        while passo<=3:
            print("**** Rodada",passo,"****") 
            if partida()==0:
                computador=computador+1
            else:
                voce=voce+1
            passo=passo+1
        print("**** Final do campeonato! ****")

        print("Placar: Você",voce,"X Computador",computador)

print("Bem-vindo ao jogo do NIM! Escolha:")

E=int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato"))

if E==1:
    print("Voce escolheu uma partida isolada!")
    partida()

else:
    print("Voce escolheu um campeonato!")
    campeonato()

    
