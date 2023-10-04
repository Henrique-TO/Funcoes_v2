def calc(n):
    n1=1

    soma = 0

    while n1 <= n: 
        soma += n1
        n1 = n1 +1 

        print("O valor da soma é = ", soma) 

#calc()

#2
def contador (palavra, letra):
    c=0
    for i in palavra:
        if i == letra:
            c+=1
            print(i)

#contador ('casa','a')
#3
def calcula(n):
    if n < 0 :
        return 'negativo'
    elif n == 0 or n == 1:
        return 1 
    else:
        resultado= 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

  
numero = int(input('digite um numero'))
resultado = calcula(numero)
print(f'fatorial de {numero} é {resultado}')

#4
def lista_fruta(a):
    dicionario= {'banana':7
             ,'pera':4
             ,'maça':3}
    
    preço= input('insira um preço para o produto')
    dicionario[a]= preço
    print (dicionario)
# lista_fruta('cachorro')

#5
# mercado={'arroz':30
#          ,'feijao':20}

# a= input('digite um produto ')
# a1=input('Quanto custa >> ')

# b=input('digite outro produto ')
# b1=input('Quanto custa >> ')

# c=input('digite outro produto ')
# c1=input('Quanto custa >> ')

# mercado[a]=a1
# mercado[b]=b1
# mercado[c]=c1

# print(mercado)