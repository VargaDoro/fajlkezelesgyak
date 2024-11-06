def hany_negativ(lista):
    i:int=0
    db:int=0
    while(i<len(lista)):
        if(lista[i]<0):
            db+=1
        i+=1
    return db

def legnagyobb(lista):
    max_index=0
    for i in range(0,len(lista),1):
        if(lista[i]>lista[max_index]):
            max_index=i
    return lista[max_index]

def parosszam_lista(lista):
    paroslista=[]
    i:int=0
    while(i<len(lista)):
        if(lista[i]%2==0):
            paroslista.append(i)
        i+=1
    return paroslista