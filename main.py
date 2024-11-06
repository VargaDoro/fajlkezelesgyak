import fajlkezeles
import feladatok

lista=fajlkezeles.fajlbol_olvas()

'''Hány negatív szám van a listában? Melyik a legnagyobb szám? Új lista paros_szamok néven.
 Mennyi az öttel osztható számok öszege? Hanyadi helyen áll a legkisebb szám? '''

db:int=feladatok.hany_negativ(lista)
print("Ennyi negatív szám van: ",db)

max=feladatok.legnagyobb(lista)
print("A legnagyobb szám: ",max)

paroslista=feladatok.parosszam_lista(lista)
print("Az új lista: ",paroslista)