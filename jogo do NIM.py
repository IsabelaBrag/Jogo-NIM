print("Bem-vindo ao jogo do NIM! Escolha:")

E=int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato"))

if E==1:
    print("Voce escolheu uma partida isolada!")
    def partida():
        n=int(input("Quantas peças? "))
        m=int(input("Limite de peças por jogada? "))
        while n>0:
            if n%(m+1)==0:
                print("Você começa!")
                usuario_escolhe_jogada(n,m)
                computador_escolhe_jogada(n,m)
            else:
                print("Computador começa!")
                computador_escolhe_jogada(n,m)
                usuario_escolhe_jogada(n,m)
        else:
            print("O computador ganhou!")
            print("Você ganhou!")
            
    def computador_escolhe_jogada(n,m):
        if n%(m+1)!=0:
            n=n-1
            print("O computador tirou uma peça")
            print("Agora restam",n,"peças no tabuleiro.")
            return n
        else:
            n=n-m
            print("O computador tirou",m,"peças.")
            if n==1:
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam apenas",n,"peças no tabuleiro.")
            return n
                
    def usuario_escolhe_jogada(n,m):
        t=int(input("Quantas peças você vai tirar? "))
        while t>m:
            print("Oops! Jogada inválida! Tente de novo")
            t=int(input("Quantas peças você vai tirar? "))
        else:
            n=n-t
            if t==1:
                print("Você tirou uma peça")
                if n==1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                else:
                    print("Agora restam apenas",n,"peças no tabuleiro.")
            else:
                 print("Você tirou ",t,"peças.")
                 print("Agora restam ",n,"peças no tabuleiro.")
    
        
            

        


        
    





        
    
