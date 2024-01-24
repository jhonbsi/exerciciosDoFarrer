def main():
    n1 = int(input('idede de um individuo:'))
    cont = 0
    soma_idade = 0
    
    while n1>0: 
        cont+=1
        soma_idade+=n1
        n1 = int(input('idede de um individuo:'))
        
    media= soma_idade/cont
    print(f"a media de idade dos individuos:{media}")

main()
        