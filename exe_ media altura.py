def main(): 
    menor_altura = 111111111111111111
    maior_altura = -1
    cont = 0
    cont_masc =0
    soma_altura = 0
    
    gen = str(input("genero do individuo:"))
    
    while gen != "stop":
        altura = float(input("altura do individuo:"))
        
        if gen== "masc":
            cont_masc+=1
        elif gen == "fem": 
            cont+=1
            soma_altura+= altura
        
        if altura > maior_altura:
                maior_altura = altura
                
        if altura < menor_altura:
                menor_altura = altura
                 
        gen = str(input("genero do individuo:"))
        
    media=soma_altura/cont    
    print(f"media de altura fem:{media}") 
    print(f"a menor altura: {menor_altura}\n a maior altura: {maior_altura}")
    print(f"quantidade de masc:{cont_masc}")
    
    
main()
             
        
