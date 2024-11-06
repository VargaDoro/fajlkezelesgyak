import random

#generálj 100 véletle egész számot [-50,150] között. A függvény terjen vissza a számokat tartalmazó listával!
def lista_letrehozasa():
    lista=[]
    for i in range(0, 100, 1):
        szam:int=int(random.random()*(151+50)-50)
        lista.append(szam)
    return lista

lista=lista_letrehozasa()
#print(lista)

#a listában lévő számokat fűzd össze egy stringgé, az elválasztójel ; legyen az utolsó után ne vegyen!
def szovegge_alakit(lista):
    szoveg:str=""
    for i in range(0,len(lista),1):
        if(i<len(lista)-1):
            szoveg+=f"{lista[i]}; "
        else:
            szoveg+=f"{lista[i]}"
    return szoveg

'''def fajlba_mentes(szoveg):
    fajlom = open("adatok.txt", "a", encoding='utf-8')
    fajlom.write(szoveg)
    fajlom.close()'''

szoveges_lista=szovegge_alakit(lista)
print(szoveges_lista)
#fajlba_mentes(szoveges_lista)

'''Adatok belvasása fájlból'''

def fajlbol_olvas():
    fajlom = open("adatok.txt", "r", encoding='utf-8')
    szoveg_fajbol:str=fajlom.read()
    szoveg_lista=szoveg_fajbol.split(";")
    '''Végig kell meni és minden elemét számmá alakítom és eltávolítom belőle a felesleges szóközket'''
    lista=[]
    for i in range(0,len(szoveg_lista),1):
        szam:int=int(szoveg_lista[i].strip())
        lista.append(szam)
    '''print(szoveg_fajbol)
    print(lista)'''
    fajlom.close()
    return lista