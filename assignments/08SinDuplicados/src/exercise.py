def main():
    #escribe tu código abajo de esta línea
    a = int(input())
    lista = []
    i = 0
    if a>0 :
        while i<a :
            valor = input()
            lista.append(valor)
            i = i+1
        print(lista)
        noduplicados=[]
        for i in lista :
            if i not in noduplicados:
                noduplicados.append(i)
            print(noduplicados)
    else:
        print('Error')

    pass

if __name__=='__main__':
    main()
    
