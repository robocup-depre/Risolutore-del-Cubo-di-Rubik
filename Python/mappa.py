from numpy import *#importo tutte le funzioni di numpy(per gestire gli array)
''' numpy è la libreria che gestisce strutture dati complesse come gli array

   def serve per dichiarare una funzione
   
   if __name =="__main__": è come scrivere main(){} in C (punto di partenza se
   non uso il programma come una libreria
   
   "BIANCO"+str(retti):unisce in una stringa la parola "BIANCO" e
   la variabile "retti"(che sarebbe un numero) convertita in stringa
   (str(retti) converte in stringa il numero "retti)

   for k in range(retti):il ciclo for viene eseguito un numero di volte pari a "retti"
   se "retti"=3 la var. k assume(in ordine) i valori 0,1,2 ogni volta che si ripete il ciclo
'''
from seriale import *
fW=zeros(9,dtype=int)#creo l'array fW di 9 elementi di tipo intero e di valore 0
fO=zeros(9,dtype=int)
fY=zeros(9,dtype=int)
fB=zeros(9,dtype=int)
fG=zeros(9,dtype=int)
fR=zeros(9,dtype=int)

w="w"
r="r"
y="y"
o="o"
g="g"
b="b"

beer=zeros(9,dtype=int)

dizionario={"w":fW,"r":fR,"y":fY,"o":fO,"g":fG,"b":fB}
#es:"w" è il colore della faccia, fW è l'array di quella faccia
#_____________________________________________________________________________________
def assegna(colore,nSticker,valore):#cambia il colore a uno sticker di una faccia
    dizionario[colore][nSticker]=valore
        
def stic(colore,nSticker):#legge il colore di uno sticker 
    return dizionario[colore][nSticker]

def assegnaFaccia(colore,valori):#assegna a una faccia i 9 colori dei suoi sticker
    dizionario[colore]=valori
    
def leggiFaccia(colore):#restituisce tutto l'array di una faccia
    return dizionario[colore]

#_____________________________________________________________________________________
def bianco(retti):
    print("BIANCO"+str(retti))#scrive il numero di rotazioni(str(retti)) che deve fare la faccia bianca
    aggiungi(["W",retti])
    if retti>0:#se il senso di rotazione è orario
        for k in range(retti):#fa la rotazione il numero di volte che gli dico come parametro della funzione
            beer[8],beer[7],beer[6]=stic(g,8),stic(g,7),stic(g,6)
            assegna(g,8,stic(r,8))
            assegna(g,7,stic(r,7))
            assegna(g,6,stic(r,6))
            assegna(r,8,stic(b,8))
            assegna(r,7,stic(b,7))
            assegna(r,6,stic(b,6))
            assegna(b,8,stic(o,8))
            assegna(b,7,stic(o,7))
            assegna(b,6,stic(o,6))
            assegna(o,8,beer[8])
            assegna(o,7,beer[7])
            assegna(o,6,beer[6])
            beer[0]=stic(w,0)
            assegna(w,0,stic(w,6))
            assegna(w,6,stic(w,8))
            assegna(w,8,stic(w,2))
            assegna(w,2,beer[0])
            beer[1]=stic(w,1)
            assegna(w,1,stic(w,3))
            assegna(w,3,stic(w,7))
            assegna(w,7,stic(w,5))
            assegna(w,5,beer[1])
    else:
        for k in range(retti*-1):#idem
            beer[8],beer[7],beer[6]=stic(g,8),stic(g,7),stic(g,6)
            assegna(g,8,stic(o,8))
            assegna(g,7,stic(o,7))
            assegna(g,6,stic(o,6))
            assegna(o,8,stic(b,8))
            assegna(o,7,stic(b,7))
            assegna(o,6,stic(b,6))
            assegna(b,8,stic(r,8))
            assegna(b,7,stic(r,7))
            assegna(b,6,stic(r,6))
            assegna(r,8,beer[8])
            assegna(r,7,beer[7])
            assegna(r,6,beer[6])
            beer[0]=stic(w,0)
            assegna(w,0,stic(w,2))
            assegna(w,2,stic(w,8))
            assegna(w,8,stic(w,6))
            assegna(w,6,beer[0])
            beer[1]=stic(w,1)
            assegna(w,1,stic(w,5))
            assegna(w,5,stic(w,7))
            assegna(w,7,stic(w,3))
            assegna(w,3,beer[1])

def rosso(retti):
    print("ROSSO"+str(retti))
    aggiungi(["R",retti])
    if retti>0:
        for k in range(retti):
            beer[0],beer[1],beer[2]=stic(w,0),stic(w,1),stic(w,2)
            assegna(w,0,stic(g,6))
            assegna(w,1,stic(g,3))
            assegna(w,2,stic(g,0))
            assegna(g,6,stic(y,2))
            assegna(g,3,stic(y,5))
            assegna(g,0,stic(y,8))
            assegna(y,2,stic(b,2))
            assegna(y,5,stic(b,5))
            assegna(y,8,stic(b,8))
            assegna(b,2,beer[0])
            assegna(b,5,beer[1])
            assegna(b,8,beer[2])
            beer[0]=stic(r,0)
            assegna(r,0,stic(r,6))
            assegna(r,6,stic(r,8))
            assegna(r,8,stic(r,2))
            assegna(r,2,beer[0])
            beer[1]=stic(r,1)
            assegna(r,1,stic(r,3))
            assegna(r,3,stic(r,7))
            assegna(r,7,stic(r,5))
            assegna(r,5,beer[1])
            
            
    else:
        for k in range(retti*-1):
            beer[0],beer[1],beer[2]=stic(w,0),stic(w,1),stic(w,2)
            assegna(w,0,stic(b,2))
            assegna(w,1,stic(b,5))
            assegna(w,2,stic(b,8))
            assegna(b,2,stic(y,2))
            assegna(b,5,stic(y,5))
            assegna(b,8,stic(y,8))
            assegna(y,2,stic(g,6))
            assegna(y,5,stic(g,3))
            assegna(y,8,stic(g,0))
            assegna(g,6,beer[0])
            assegna(g,3,beer[1])
            assegna(g,0,beer[2])
            beer[0]=stic(r,0)
            assegna(r,0,stic(r,2))
            assegna(r,2,stic(r,8))
            assegna(r,8,stic(r,6))
            assegna(r,6,beer[0])
            beer[1]=stic(r,1)
            assegna(r,1,stic(r,5))
            assegna(r,5,stic(r,7))
            assegna(r,7,stic(r,3))
            assegna(r,3,beer[1])

def verde(retti):
    print("VERDE"+str(retti))#scrive il numero di rotazioni(str(retti)) che deve fare la faccia bianca
    aggiungi(["G",retti])
    if retti>0:#se il senso di rotazione è orario
        for k in range(retti):#fa la rotazione il numero di volte che gli dico come parametro della funzione
            beer[0],beer[1],beer[2]=stic(y,0),stic(y,1),stic(y,2)
            assegna(y,0,stic(r,2))
            assegna(y,1,stic(r,5))
            assegna(y,2,stic(r,8))
            assegna(r,2,stic(w,2))
            assegna(r,5,stic(w,5))
            assegna(r,8,stic(w,8))
            assegna(w,2,stic(o,6))
            assegna(w,5,stic(o,3))
            assegna(w,8,stic(o,0))
            assegna(o,6,beer[0])
            assegna(o,3,beer[1])
            assegna(o,0,beer[2])
            beer[0]=stic(g,0)
            assegna(g,0,stic(g,6))
            assegna(g,6,stic(g,8))
            assegna(g,8,stic(g,2))
            assegna(g,2,beer[0])
            beer[1]=stic(g,1)
            assegna(g,1,stic(g,3))
            assegna(g,3,stic(g,7))
            assegna(g,7,stic(g,5))
            assegna(g,5,beer[1])
            
    else:
        for k in range(retti*-1):#idem
            beer[0],beer[1],beer[2]=stic(y,0),stic(y,1),stic(y,2)
            assegna(y,0,stic(o,6))
            assegna(y,1,stic(o,3))
            assegna(y,2,stic(o,0))
            assegna(o,6,stic(w,2))
            assegna(o,3,stic(w,5))
            assegna(o,0,stic(w,8))
            assegna(w,2,stic(r,2))
            assegna(w,5,stic(r,5))
            assegna(w,8,stic(r,8))
            assegna(r,2,beer[0])
            assegna(r,5,beer[1])
            assegna(r,8,beer[2])
            beer[0]=stic(g,0)
            assegna(g,0,stic(g,2))
            assegna(g,2,stic(g,8))
            assegna(g,8,stic(g,6))
            assegna(g,6,beer[0])
            beer[1]=stic(g,1)
            assegna(g,1,stic(g,5))
            assegna(g,5,stic(g,7))
            assegna(g,7,stic(g,3))
            assegna(g,3,beer[1])

def arancione(retti):
    print("ARANCIONE"+str(retti))#scrive il numero di rotazioni(str(retti)) che deve fare la faccia bianca
    aggiungi(["O",retti])
    if retti>0:#se il senso di rotazione è orario
        for k in range(retti):#fa la rotazione il numero di volte che gli dico come parametro della funzione
            beer[2],beer[5],beer[8]=stic(g,2),stic(g,5),stic(g,8)
            assegna(g,2,stic(w,8))
            assegna(g,5,stic(w,7))
            assegna(g,8,stic(w,6))
            assegna(w,8,stic(b,6))
            assegna(w,7,stic(b,3))
            assegna(w,6,stic(b,0))
            assegna(b,6,stic(y,6))
            assegna(b,3,stic(y,3))
            assegna(b,0,stic(y,0))
            assegna(y,6,beer[2])
            assegna(y,3,beer[5])
            assegna(y,0,beer[8])
            beer[0]=stic(o,0)
            assegna(o,0,stic(o,6))
            assegna(o,6,stic(o,8))
            assegna(o,8,stic(o,2))
            assegna(o,2,beer[0])
            beer[1]=stic(o,1)
            assegna(o,1,stic(o,3))
            assegna(o,3,stic(o,7))
            assegna(o,7,stic(o,5))
            assegna(o,5,beer[1])
    else:
        for k in range(retti*-1):#idem
            beer[2],beer[5],beer[8]=stic(g,2),stic(g,5),stic(g,8)
            assegna(g,2,stic(y,6))
            assegna(g,5,stic(y,3))
            assegna(g,8,stic(y,0))
            assegna(y,6,stic(b,6))
            assegna(y,3,stic(b,3))
            assegna(y,0,stic(b,0))
            assegna(b,6,stic(w,8))
            assegna(b,3,stic(w,7))
            assegna(b,0,stic(w,6))
            assegna(w,8,beer[2])
            assegna(w,7,beer[5])
            assegna(w,6,beer[8])
            beer[0]=stic(o,0)
            assegna(o,0,stic(o,2))
            assegna(o,2,stic(o,8))
            assegna(o,8,stic(o,6))
            assegna(o,6,beer[0])
            beer[1]=stic(o,1)
            assegna(o,1,stic(o,5))
            assegna(o,5,stic(o,7))
            assegna(o,7,stic(o,3))
            assegna(o,3,beer[1])

def blu(retti):
    print("BLU"+str(retti))#scrive il numero di rotazioni(str(retti)) che deve fare la faccia bianca
    aggiungi(["B",retti])
    if retti>0:#se il senso di rotazione è orario
        for k in range(retti):#fa la rotazione il numero di volte che gli dico come parametro della funzione
            beer[2],beer[5],beer[8]=stic(o,2),stic(o,5),stic(o,8)
            assegna(o,2,stic(w,6))
            assegna(o,5,stic(w,3))
            assegna(o,8,stic(w,0))
            assegna(w,6,stic(r,6))
            assegna(w,3,stic(r,3))
            assegna(w,0,stic(r,0))
            assegna(r,6,stic(y,8))
            assegna(r,3,stic(y,7))
            assegna(r,0,stic(y,6))
            assegna(y,8,beer[2])
            assegna(y,7,beer[5])
            assegna(y,6,beer[8])
            beer[0]=stic(b,0)
            assegna(b,0,stic(b,6))
            assegna(b,6,stic(b,8))
            assegna(b,8,stic(b,2))
            assegna(b,2,beer[0])
            beer[1]=stic(b,1)
            assegna(b,1,stic(b,3))
            assegna(b,3,stic(b,7))
            assegna(b,7,stic(b,5))
            assegna(b,5,beer[1])
    else:
        for k in range(retti*-1):#idem
            beer[2],beer[5],beer[8]=stic(o,2),stic(o,5),stic(o,8)
            assegna(o,2,stic(y,8))
            assegna(o,5,stic(y,7))
            assegna(o,8,stic(y,6))
            assegna(y,8,stic(r,6))
            assegna(y,7,stic(r,3))
            assegna(y,6,stic(r,0))
            assegna(r,6,stic(w,6))
            assegna(r,3,stic(w,3))
            assegna(r,0,stic(w,0))
            assegna(w,6,beer[2])
            assegna(w,3,beer[5])
            assegna(w,0,beer[8])
            beer[0]=stic(b,0)
            assegna(b,0,stic(b,2))
            assegna(b,2,stic(b,8))
            assegna(b,8,stic(b,6))
            assegna(b,6,beer[0])
            beer[1]=stic(b,1)
            assegna(b,1,stic(b,5))
            assegna(b,5,stic(b,7))
            assegna(b,7,stic(b,3))
            assegna(b,3,beer[1])

def giallo(retti):
    print("GIALLO"+str(retti))#scrive il numero di rotazioni(str(retti)) che deve fare la faccia bianca
    aggiungi(["Y",retti])
    if retti>0:#se il senso di rotazione è orario
        for k in range(retti):#fa la rotazione il numero di volte che gli dico come parametro della funzione
            beer[0],beer[1],beer[2]=stic(g,0),stic(g,1),stic(g,2)
            assegna(g,0,stic(o,0))
            assegna(g,1,stic(o,1))
            assegna(g,2,stic(o,2))
            assegna(o,0,stic(b,0))
            assegna(o,1,stic(b,1))
            assegna(o,2,stic(b,2))
            assegna(b,0,stic(r,0))
            assegna(b,1,stic(r,1))
            assegna(b,2,stic(r,2))
            assegna(r,0,beer[0])
            assegna(r,1,beer[1])
            assegna(r,2,beer[2])
            beer[0]=stic(y,0)
            assegna(y,0,stic(y,6))
            assegna(y,6,stic(y,8))
            assegna(y,8,stic(y,2))
            assegna(y,2,beer[0])
            beer[1]=stic(y,1)
            assegna(y,1,stic(y,3))
            assegna(y,3,stic(y,7))
            assegna(y,7,stic(y,5))
            assegna(y,5,beer[1])
    else:
        for k in range(retti*-1):#idem
            beer[0],beer[1],beer[2]=stic(g,0),stic(g,1),stic(g,2)
            assegna(g,0,stic(r,0))
            assegna(g,1,stic(r,1))
            assegna(g,2,stic(r,2))
            assegna(r,0,stic(b,0))
            assegna(r,1,stic(b,1))
            assegna(r,2,stic(b,2))
            assegna(b,0,stic(o,0))
            assegna(b,1,stic(o,1))
            assegna(b,2,stic(o,2))
            assegna(o,0,beer[0])
            assegna(o,1,beer[1])
            assegna(o,2,beer[2])
            beer[0]=stic(y,0)
            assegna(y,0,stic(y,2))
            assegna(y,2,stic(y,8))
            assegna(y,8,stic(y,6))
            assegna(y,6,beer[0])
            beer[1]=stic(y,1)
            assegna(y,1,stic(y,5))
            assegna(y,5,stic(y,7))
            assegna(y,7,stic(y,3))
            assegna(y,3,beer[1])
            

if __name__=="__main__":
    '''bianco(1)
    for k in range(9):
        assegna(w,k,W)
    print(f"faccia:{leggiFaccia(w)}")
    '''
    print("Questa libreria contiene 4 funzioni che gestiscono la mappa e le rotazioni del cubo:\n")
    print("assegna(colore,nSticker,valore): serve per assegnare a uno sticker il suo valore\n")
    print("stic(colore,nSticker): restituisce il valore assegnato a uno sticker\n")
    print("assegnaFaccia(colore,valori): assegna a un'intera faccia un array di valori\n")
    print("leggiFaccia(colore): restituisce tutti i valori di una faccia")
    print(leggiFaccia("w"))
    input()
    
    





