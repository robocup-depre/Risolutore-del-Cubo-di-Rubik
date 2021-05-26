import telecamera as tel#importa la libreria telecamera con un nome più corto
from tkinter import *#lib. per finestre con pulsanti e colori(già fatta)
import string
from mappa import *
import winsound
from seriale import *

diz={119:"white",114:"red",103:"green",111:"orange",121:"yellow",98:"blue"}
alg=[]#algoritmo di risoluzione da calcolare

W=119#per indicare il colore di uno sticker
R=114
G=103
O=111
B=98
Y=121

w="w"#per indicare la faccia
r="r"
g="g"
o="o"
b="b"
y="y"

a=4
h=9
c=5
d=10
e=22
f=15
fS=13
def calcola():
    #________________________________________________________________________________________________1 STRATO
    #spigoloWR
    print("spigWR")
    if stic(w,1)==W and stic(r,7)==R:
        pass
    if stic(w,5)==W and stic(g,7)==R:
        bianco(-1)        
    if stic(w,3)==W and stic(b,7)==R:
        bianco(1)
    if stic(w,7)==W and stic(o,7)==R:
        bianco(2)
    if stic(w,1)==R and stic(r,7)==W:
        bianco(-1)
        blu(-1)
        rosso(-1)
    if stic(w,5)==R and stic(g,7)==W:
        verde(1)
        rosso(1)
    if stic(w,3)==R and stic(b,7)==W:
        blu(-1)
        rosso(-1)
    if stic(w,7)==R and stic(o,7)==W:
        arancione(-1)
        blu(-1)
        bianco(1)
    if stic(b,5)==R and stic(r,3)==W:
        blu(1)
        bianco(1)
    if stic(b,5)==W and stic(r,3)==R:
        rosso(-1)
    if stic(o,5)==R and stic(b,3)==W:
        arancione(1)
        bianco(2)
    if stic(o,5)==W and stic(b,3)==R:
        blu(-1)
        bianco(1)
    if stic(o,3)==W and stic(g,5)==R:
        verde(1)
        bianco(-1)
    if stic(o,3)==R and stic(g,5)==W:
        verde(2)
        rosso(1)
    if stic(g,3)==W and stic(r,5)==R:
        rosso(1)
    if stic(g,3)==R and stic(r,5)==W:
        verde(-1)
        bianco(-1)
    if stic(y,5)==W and stic(r,1)==R:
        rosso(2)
    if stic(y,5)==R and stic(r,1)==W:
        rosso(-1)
        blu(1)
        bianco(1)
    if stic(y,7)==W and stic(b,1)==R:
        blu(2)
        bianco(1)
    if stic(y,7)==R and stic(b,1)==W:
        blu(1)
        rosso(-1)
    if stic(y,3)==W and stic(o,1)==R:
        arancione(2)
        bianco(2)
    if stic(y,3)==R and stic(o,1)==W:
        giallo(1)
        verde(-1)
        rosso(1)
    if stic(y,1)==W and stic(g,1)==R:
        verde(2)
        bianco(-1)
    if stic(y,1)==R and stic(g,1)==W:
        verde(-1)
        rosso(1)
    #spigolo WG
    print("spigWG")
    if stic(g,7)==G and stic(w,5)==W:
        pass
    if stic(g,7)==W and stic(w,5)==G:
        bianco(1)
        arancione(1)
        bianco(-1)
        verde(1)
    if stic(o,7)==G and stic(w,7)==W:
        bianco(-1)
        verde(-1)
        bianco(1)
        verde(1)
    if stic(o,7)==W and stic(w,7)==G:
        arancione(1)
        verde(1)
    if stic(b,7)==G and stic(w,3)==W:
        blu(1)
        arancione(2)
        verde(1)
    if stic(b,7)==W and stic(w,3)==G:
        bianco(-1)
        arancione(1)
        bianco(1)
        verde(1)
    if stic(r,5)==W and stic(g,3)==G:
        verde(-1)
    if stic(r,5)==G and stic(g,3)==W:
        rosso(-1)
        giallo(-1)
        rosso(1)
        verde(2)
    if stic(g,5)==G and stic(o,3)==W:
        verde(1)
    if stic(g,5)==W and stic(o,3)==G:
        bianco(1)
        arancione(-1)
        bianco(-1)
    if stic(o,5)==G and stic(b,3)==W:
        bianco(1)
        arancione(1)
        bianco(-1)
    if stic(o,5)==W and stic(b,3)==G:
        arancione(2)
        verde(1)
    if stic(b,5)==G and stic(r,3)==W:
        bianco(2)
        blu(1)
        bianco(2)
    if stic(b,5)==W and stic(r,3)==G:
        bianco(-1)
        rosso(-1)
        bianco(1)
    if stic(g,1)==G and stic(y,1)==W:
        verde(2)
    if stic(g,1)==W and stic(y,1)==G:
        giallo(-1)
        arancione(-1)
        verde(1)
    if stic(r,1)==G and stic(y,5)==W:
        giallo(-1)
        verde(2)
    if stic(r,1)==W and stic(y,5)==G:
        rosso(1)
        verde(-1)
        rosso(-1)
    if stic(b,1)==G and stic(y,7)==W:
        giallo(2)
        verde(2)
    if stic(b,1)==W and stic(y,7)==G:
        giallo(1)
        arancione(-1)
        verde(1)
    if stic(o,1)==G and stic(y,3)==W:
        giallo(1)
        verde(2)
    if stic(o,1)==W and stic(y,3)==G:
        arancione(-1)
        verde(1)
    #spigolo OW
    print("spigWO")
    if stic(o,7)==O and stic(w,7)==W:
        pass
    if stic(o,7)==W and stic(w,7)==O:
        bianco(1)
        blu(1)
        bianco(-1)
        arancione(1)
    if stic(b,7)==W and stic(w,3)==O:
        blu(1)
        arancione(1)
    if stic(b,7)==O and stic(w,3)==W:
        bianco(-1)
        arancione(-1)
        bianco(1)
        arancione(1)
    if stic(g,5)==W and stic(o,3)==O:
        arancione(-1)
    if stic(g,5)==O and stic(o,3)==W:
        bianco(-1)
        verde(1)
        bianco(1)
    if stic(b,3)==W and stic(o,5)==O:
        arancione(1)
    if stic(b,3)==O and stic(o,5)==W:
        bianco(1)
        blu(-1)
        bianco(-1)
    if stic(g,3)==W and stic(r,5)==O:
        verde(2)
        arancione(-1)
        verde(2)
    if stic(g,3)==O and stic(r,5)==W:
        bianco(-1)
        verde(-1)
        bianco(1)
    if stic(b,5)==W and stic(r,3)==O:
        blu(2)
        arancione(1)
    if stic(b,5)==O and stic(r,3)==W:
        bianco(1)
        blu(1)
        bianco(-1)
    if stic(o,1)==O and stic(y,3)==W:
        arancione(2)
    if stic(o,1)==W and stic(y,3)==O:
        giallo(-1)
        blu(-1)
        arancione(1)
    if stic(g,1)==O and stic(y,1)==W:
        giallo(-1)
        arancione(2)
    if stic(g,1)==W and stic(y,1)==O:
        bianco(-1)
        verde(1)
        bianco(1)
        arancione(-1)
    if stic(r,1)==O and stic(y,5)==W:
        giallo(2)
        arancione(2)
    if stic(r,1)==W and stic(y,5)==O:
        giallo(1)
        blu(-1)
        arancione(1)
    if stic(b,1)==O and stic(y,7)==W:
        giallo(1)
        arancione(2)
    if stic(b,1)==W and stic(y,7)==O:
        blu(-1)
        arancione(1)
    #spigolo WB
    print("spigWB")
    if stic(b,7)==B and stic(w,3)==W:
        pass
    if stic(b,7)==W and stic(w,3)==B:
        bianco(-1)
        arancione(-1)
        bianco(1)
        blu(-1)
    if stic(g,3)==B and stic(r,5)==W:
        bianco(2)
        verde(1)
        bianco(2)
    if stic(g,3)==W and stic(r,5)==B:
        bianco(1)
        rosso(1)
        bianco(-1)
    if stic(o,3)==W and stic(g,5)==B:
        bianco(2)
        verde(1)
        bianco(2)
    if stic(o,3)==B and stic(g,5)==W:
        bianco(-1)
        arancione(-1)
        bianco(1)
    if stic(b,5)==B and stic(r,3)==W:
        blu(1)
    if stic(b,5)==W and stic(r,3)==B:
        bianco(1)
        rosso(-1)
        bianco(-1)
    if stic(b,3)==B and stic(o,5)==W:
        blu(-1)
    if stic(b,3)==W and stic(o,5)==B:
        bianco(-1)
        arancione(1)
        bianco(1)
    if stic(b,1)==B and stic(y,7)==W:
        blu(2)
    if stic(b,1)==W and stic(y,7)==B:
        giallo(-1)
        rosso(-1)
        blu(1)
        rosso(1)
    if stic(o,1)==B and stic(y,3)==W:
        giallo(-1)
        blu(2)
    if stic(o,1)==W and stic(y,3)==B:
        arancione(1)
        blu(-1)
        arancione(-1)
    if stic(r,1)==B and stic(y,5)==W:
        giallo(1)
        blu(2)
    if stic(r,1)==W and stic(y,5)==B:
        rosso(-1)
        blu(1)
        rosso(1)
    if stic(g,1)==B and stic(y,1)==W:
        giallo(2)
        blu(2)
    if stic(g,1)==W and stic(y,1)==B:
        arancione(-1)
        giallo(-1)
        arancione(1)
        blu(-1)
    #angoloWRG
    print("angWRG")
    if stic(w,2)==W and stic(g,6)==G and stic(r,8)==R:
        pass
    if (stic(w,2)==G and stic(g,6)==R and stic(r,8)==W) or (stic(w,2)==R and stic(g,6)==W and stic(r,8)==G) or (stic(g,0)==G and stic(y,2)==R and stic(r,2)==W) or (stic(g,0)==W and stic(y,2)==G and stic(r,2)==R) or (stic(g,0)==R and stic(y,2)==W and stic(r,2)==G):
        while stic(w,2)!=W or stic(g,6)!=G or stic(r,8)!=R:
            verde(1)
            giallo(1)
            verde(-1)
            giallo(-1)#OK
    if (stic(w,8)==G and stic(o,6)==R and stic(g,8)==W) or (stic(o,6)==W and stic(g,8)==G and stic(w,8)==R) or (stic(o,6)==G and stic(g,8)==R and stic(w,8)==W):
        arancione(1)
        giallo(1)
        arancione(-1)
        while stic(w,2)!=W or stic(g,6)!=G or stic(r,8)!=R:
            verde(1)
            giallo(1)
            verde(-1)
            giallo(-1)#OK
    if (stic(g,2)==G and stic(o,0)==R and stic(y,0)==W) or (stic(g,2)==W and stic(o,0)==G and stic(y,0)==R) or (stic(g,2)==R and stic(o,0)==W and stic(y,0)==G):
        giallo(1)
        while stic(w,2)!=W or stic(g,6)!=G or stic(r,8)!=R:
            verde(1)
            giallo(1)
            verde(-1)
            giallo(-1)#OK
    if (stic(w,6)==R and stic(b,6)==W and stic(o,8)==G) or (stic(w,6)==G and stic(b,6)==R and stic(o,8)==W) or (stic(w,6)==W and stic(b,6)==G and stic(o,8)==R):
        blu(1)
        giallo(1)
        blu(-1)
        giallo(1)
        while stic(w,2)!=W or stic(g,6)!=G or stic(r,8)!=R:
            verde(1)
            giallo(1)
            verde(-1)
            giallo(-1)#OK
    if (stic(b,0)==R and stic(y,6)==W and stic(o,2)==G) or (stic(b,0)==G and stic(y,6)==R and stic(o,2)==W) or (stic(b,0)==W and stic(y,6)==G and stic(o,2)==R):
        giallo(2)
        while stic(w,2)!=W or stic(g,6)!=G or stic(r,8)!=R:
            verde(1)
            giallo(1)
            verde(-1)
            giallo(-1)#OK
    if (stic(w,0)==R and stic(r,6)==W and stic(b,8)==G) or (stic(w,0)==G and stic(r,6)==R and stic(b,8)==W) or (stic(w,0)==W and stic(r,6)==G and stic(b,8)==R):
        rosso(1)
        giallo(1)
        rosso(-1)
        giallo(2)
        while stic(w,2)!=W or stic(g,6)!=G or stic(r,8)!=R:
            verde(1)
            giallo(1)
            verde(-1)
            giallo(-1)#OK
    if (stic(r,0)==R and stic(y,8)==W and stic(b,2)==G) or (stic(r,0)==G and stic(y,8)==R and stic(b,2)==W) or(stic(r,0)==W and stic(y,8)==G and stic(b,2)==R):
        giallo(-1)
        while stic(w,2)!=W or stic(g,6)!=G or stic(r,8)!=R:
            verde(1)
            giallo(1)
            verde(-1)
            giallo(-1)#OK
    #angoloWGO
    print("angWGO")
    if stic(g,8)==G and stic(w,8)==W and stic(o,6)==O:
        pass
    if (stic(g,8)==W and stic(w,8)==O and stic(o,6)==G) or (stic(g,8)==O and stic(w,8)==G and stic(o,6)==W):
        while stic(g,8)!=G or stic(w,8)!=W or stic(o,6)!=O:
            arancione(1)
            giallo(1)
            arancione(-1)
            giallo(-1)
    if (stic(g,2)==O and stic(o,0)==G and stic(y,0)==W) or (stic(g,2)==W and stic(o,0)==O and stic(y,0)==G) or (stic(g,2)==G and stic(o,0)==W and stic(y,0)==O):
        while stic(g,8)!=G or stic(w,8)!=W or stic(o,6)!=O:
            arancione(1)
            giallo(1)
            arancione(-1)
            giallo(-1)
    if (stic(o,8)==O and stic(w,6)==G and stic(b,6)==W) or (stic(o,8)==G and stic(w,6)==W and stic(b,6)==O) or (stic(o,8)==W and stic(w,6)==O and stic(b,6)==G):
        blu(1)
        giallo(1)
        blu(-1)
        while stic(g,8)!=G or stic(w,8)!=W or stic(o,6)!=O:
            arancione(1)
            giallo(1)
            arancione(-1)
            giallo(-1)
    if (stic(o,2)==G and stic(b,0)==W and stic(y,6)==O) or (stic(o,2)==O and stic(b,0)==G and stic(y,6)==W) or (stic(o,2)==W and stic(b,0)==O and stic(y,6)==G):
        giallo(1)
        while stic(g,8)!=G or stic(w,8)!=W or stic(o,6)!=O:
            arancione(1)
            giallo(1)
            arancione(-1)
            giallo(-1)
    if (stic(w,0)==W and stic(r,6)==O and stic(b,8)==G) or (stic(w,0)==G and stic(r,6)==W and stic(b,8)==O) or (stic(w,0)==O and stic(r,6)==G and stic(b,8)==W):
        rosso(1)
        giallo(1)
        rosso(-1)
        giallo(1)
        while stic(g,8)!=G or stic(w,8)!=W or stic(o,6)!=O:
            arancione(1)
            giallo(1)
            arancione(-1)
            giallo(-1)
    if (stic(b,2)==W and stic(r,0)==O and stic(y,8)==G) or (stic(b,2)==G and stic(r,0)==W and stic(y,8)==O) or (stic(b,2)==O and stic(r,0)==G and stic(y,8)==W):
        giallo(2)
        while stic(g,8)!=G or stic(w,8)!=W or stic(o,6)!=O:
            arancione(1)
            giallo(1)
            arancione(-1)
            giallo(-1)
    if (stic(r,2)==W and stic(g,0)==O and stic(y,2)==G) or (stic(r,2)==G and stic(g,0)==W and stic(y,2)==O) or (stic(r,2)==O and stic(g,0)==G and stic(y,2)==W):
        giallo(-1)
        while stic(g,8)!=G or stic(w,8)!=W or stic(o,6)!=O:
            arancione(1)
            giallo(1)
            arancione(-1)
            giallo(-1)
    #angoloWRB
    print("angWRB")
    if stic(w,0)==W and stic(r,6)==R and stic(b,8)==B:
        pass
    if (stic(w,0)==R and stic(r,6)==B and stic(b,8)==W) or (stic(w,0)==B and stic(r,6)==W and stic(b,8)==R):
        while stic(w,0)!=W or stic(r,6)!=R or stic(b,8)!=B:
            rosso(1)
            giallo(1)
            rosso(-1)
            giallo(-1)
    if (stic(b,2)==W and stic(r,0)==R and stic(y,8)==B) or (stic(b,2)==B and stic(r,0)==W and stic(y,8)==R) or (stic(b,2)==R and stic(r,0)==B and stic(y,8)==W):
        while stic(w,0)!=W or stic(r,6)!=R or stic(b,8)!=B:
            rosso(1)
            giallo(1)
            rosso(-1)
            giallo(-1)
    if (stic(w,6)==R and stic(b,6)==B and stic(o,8)==W) or (stic(w,6)==W and stic(b,6)==R and stic(o,8)==B) or (stic(w,6)==B and stic(b,6)==W and stic(o,8)==R):
        blu(1)
        giallo(1)
        blu(-1)
        giallo(2)
        while stic(w,0)!=W or stic(r,6)!=R or stic(b,8)!=B:
            rosso(1)
            giallo(1)
            rosso(-1)
            giallo(-1)
    if (stic(o,2)==R and stic(b,0)==B and stic(y,6)==W) or (stic(o,2)==W and stic(b,0)==R and stic(y,6)==B) or (stic(o,2)==B and stic(b,0)==W and stic(y,6)==R):
        giallo(-1)
        while stic(w,0)!=W or stic(r,6)!=R or stic(b,8)!=B:
            rosso(1)
            giallo(1)
            rosso(-1)
            giallo(-1)
    if (stic(g,2)==R and stic(o,0)==B and stic(y,0)==W) or (stic(g,2)==W and stic(o,0)==R and stic(y,0)==B) or (stic(g,2)==B and stic(o,0)==W and stic(y,0)==R):
        giallo(2)
        while stic(w,0)!=W or stic(r,6)!=R or stic(b,8)!=B:
            rosso(1)
            giallo(1)
            rosso(-1)
            giallo(-1)
    if (stic(r,2)==R and stic(g,0)==B and stic(y,2)==W) or (stic(r,2)==W and stic(g,0)==R and stic(y,2)==B) or (stic(r,2)==B and stic(g,0)==W and stic(y,2)==R):
        giallo(1)
        while stic(w,0)!=W or stic(r,6)!=R or stic(b,8)!=B:
            rosso(1)
            giallo(1)
            rosso(-1)
            giallo(-1)
    #angolo WOB
    print("angWOB")
    if stic(w,6)==W and stic(b,6)==B and stic(o,8)==O:
        pass
    if (stic(w,6)==B and stic(b,6)==O and stic(o,8)==W) or (stic(w,6)==O and stic(b,6)==W and stic(o,8)==B):
        while stic(w,6)!=W or stic(b,6)!=B or stic(o,8)!=O:
            blu(1)
            giallo(1)
            blu(-1)
            giallo(-1)#OK
            "inserita sotto"
    if (stic(b,2)==O and stic(r,0)==W and stic(y,8)==B) or (stic(b,2)==W and stic(r,0)==B and stic(y,8)==O) or (stic(b,2)==B and stic(r,0)==O and stic(y,8)==W):
         giallo(1)
         while stic(w,6)!=W or stic(b,6)!=B or stic(o,8)!=O:
            blu(1)
            giallo(1)
            blu(-1)
            giallo(-1)#OK
            "controllare sotto già inserita sopra la seconda"
    '''if (stic(w,6)==O and stic(b,6)==W and stic(o,8)==B) or (stic(w,6)==B and stic(b,6)==O and stic(o,8)==W) or (stic(w,6)==W and stic(b,6)==B and stic(o,8)==O):
        while stic(w,6)!=W or stic(b,6)!=B or stic(o,8)!=O:
            blu(1)
            giallo(1)
            blu(-1)
            giallo(-1)
        "controllare sotto non ci va giallo(1) (corretta)"
        '''
    if (stic(b,0)==O and stic(y,6)==W and stic(o,2)==B) or (stic(b,0)==B and stic(y,6)==O and stic(o,2)==W) or (stic(b,0)==W and stic(y,6)==B and stic(o,2)==O):
        while stic(w,6)!=W or stic(b,6)!=B or stic(o,8)!=O:
            blu(1)
            giallo(1)
            blu(-1)
            giallo(-1)#OK
    if (stic(r,2)==O and stic(g,0)==W and stic(y,2)==B) or (stic(r,2)==B and stic(g,0)==O and stic(y,2)==W) or (stic(r,2)==W and stic(g,0)==B and stic(y,2)==O):
        giallo(2)
        while stic(w,6)!=W or stic(b,6)!=B or stic(o,8)!=O:
            blu(1)
            giallo(1)
            blu(-1)
            giallo(-1)#OK
    if (stic(g,2)==O and stic(o,0)==W and stic(y,0)==B) or (stic(g,2)==B and stic(o,0)==O and stic(y,0)==W) or (stic(g,2)==W and stic(o,0)==B and stic(y,0)==O):
        giallo(-1)
        while stic(w,6)!=W or stic(b,6)!=B or stic(o,8)!=O:
            blu(1)
            giallo(1)
            blu(-1)
            giallo(-1)#OK
    #________________________________________________________________________________________________2 STRATO
    #spigolo RG
    print("2 strato GR")
    if (stic(r,5)==R and stic(g,3)==G):
        pass
    if (stic(r,5)==G and stic(g,3)==R):
        verde(1)
        giallo(2)
        verde(-1)
        giallo(1)
        verde(1)
        giallo(2)
        verde(-1)
        giallo(1)
        rosso(-1)
        giallo(-1)
        rosso(1)
    if(stic(g,5)==G and stic(o,3)==R):#GO PPPPPPPPP
        arancione(1)
        giallo(1)
        arancione(-1)
        giallo(-1)
        verde(-1)
        giallo(-1)
        verde(2)
        giallo(-1)
        verde(-1)
        giallo(-1)
        rosso(-1)
        giallo(1)
        rosso(1)
    if(stic(g,5)==R and stic(o,3)==G):
        arancione(1)
        giallo(1)
        arancione(-1)
        giallo(-1)
        verde(-1)
        giallo(-1)
        verde(1)
        giallo(1)
        rosso(-1)
        giallo(1)
        rosso(1)
        giallo(1)
        verde(1)
        giallo(-1)
        verde(-1)
    if(stic(o,5)==R and stic(b,3)==G):#OB
        blu(1)
        giallo(1)
        blu(-1)
        giallo(-1)
        arancione(-1)
        giallo(-1)
        arancione(1)
        giallo(2)
        rosso(-1)
        giallo(1)
        rosso(1)
        giallo(1)
        verde(1)
        giallo(-1)
        verde(-1)
    if(stic(o,5)==G and stic(b,3)==R):
        blu(1)
        giallo(1)
        blu(-1)
        giallo(-1)
        arancione(-1)
        giallo(-1)
        arancione(1)
        giallo(1)
        verde(1)
        giallo(-1)
        verde(-1)
        giallo(-1)
        rosso(-1)
        giallo(1)
        rosso(1)
    if(stic(b,5)==G and stic(r,3)==R):#BR
        rosso(1)
        giallo(1)
        rosso(-1)
        giallo(-1)
        blu(-1)
        giallo(-1)
        blu(1)
        giallo(2)
        verde(1)
        giallo(-1)
        verde(-1)
        giallo(-1)
        rosso(-1)
        giallo(1)
        rosso(1)
    if(stic(b,5)==R and stic(r,3)==G):
        rosso(1)
        giallo(1)
        rosso(-1)
        giallo(-1)
        blu(-1)
        giallo(-1)
        blu(1)
        giallo(-1)
        rosso(-1)
        giallo(1)
        rosso(1)
        giallo(1)
        verde(1)
        giallo(-1)
        verde(-1)
    if(stic(r,1)==R and stic(y,5)==G):#RY
        giallo(1)
        verde(1)
        giallo(-1)
        verde(-1)
        giallo(-1)
        rosso(-1)
        giallo(1)
        rosso(1)
    if (stic(r,1)==G and stic(y,5)==R):
        giallo(2)
        rosso(-1)
        giallo(1)
        rosso(1)
        giallo(1)
        verde(1)
        giallo(-1)
        verde(-1)
    if(stic(g,1)==G and stic(y,1)==R):#GY
        giallo(-1)
        rosso(-1)
        giallo(1)
        rosso(1)
        giallo(1)
        verde(1)
        giallo(-1)
        verde(-1)
    if(stic(g,1)==R and stic(y,1)==G):
        giallo(2)
        verde(1)
        giallo(-1)
        verde(-1)
        giallo(-1)
        rosso(-1)
        giallo(1)
        rosso(1)
    if (stic(o,1)==R and stic(y,3)==G):#OY
        giallo(-1)
        verde(1)
        giallo(-1)
        verde(-1)
        giallo(-1)
        rosso(-1)
        giallo(1)
        rosso(1)
    if(stic(o,1)==G and stic(y,3)==R):
        rosso(-1)
        giallo(1)
        rosso(1)
        giallo(1)
        verde(1)
        giallo(-1)
        verde(-1)
    if(stic(b,1)==G and stic(y,7)==R):
        giallo(1)
        rosso(-1)
        giallo(1)
        rosso(1)
        giallo(1)
        verde(1)
        giallo(-1)
        verde(-1)
    if(stic(b,1)==R and stic(y,7)==G):
        verde(1)
        giallo(-1)
        verde(-1)
        giallo(-1)
        rosso(-1)
        giallo(1)
        rosso(1)
    #spigolo GO
    print("2 strato GO")
    if(stic(g,5)==G and stic(o,3)==O):#GO
        pass
    if(stic(g,5)==O and stic(o,3)==G):
        arancione(1)
        giallo(2)
        arancione(-1)
        giallo(1)
        arancione(1)
        giallo(2)
        arancione(-1)
        giallo(1)
        verde(-1)
        giallo(-1)
        verde(1)
    if (stic(o,5)==O and stic(b,3)==G):#OB
        blu(1)
        giallo(1)
        blu(-1)
        giallo(-1)
        arancione(-1)
        giallo(-1)
        arancione(2)
        giallo(-1)
        arancione(-1)
        giallo(-1)
        verde(-1)
        giallo(1)
        verde(1)
    if(stic(o,5)==G and stic(b,3)==O):
        blu(1)
        giallo(1)
        blu(-1)
        giallo(-1)
        arancione(-1)
        giallo(-1)
        arancione(1)
        giallo(1)
        verde(-1)
        giallo(1)
        verde(1)
        giallo(1)
        arancione(1)
        giallo(-1)
        arancione(-1)
    if(stic(b,5)==G and stic(r,3)==O):#BR
        rosso(1)
        giallo(1)
        rosso(-1)
        giallo(-1)
        blu(-1)
        giallo(-1)
        blu(1)
        giallo(2)
        verde(-1)
        giallo(1)
        verde(1)
        giallo(1)
        arancione(1)
        giallo(-1)
        arancione(-1)
    if(stic(b,5)==O and stic(r,3)==G):
        rosso(1)
        giallo(1)
        rosso(-1)
        giallo(-1)
        blu(-1)
        giallo(-1)
        blu(1)
        giallo(1)
        arancione(1)
        giallo(-1)
        arancione(-1)
        giallo(-1)
        verde(-1)
        giallo(1)
        verde(1)
    if(stic(r,1)==O and stic(y,5)==G):#RY
        giallo(1)
        verde(-1)
        giallo(1)
        verde(1)
        giallo(1)
        arancione(1)
        giallo(-1)
        arancione(-1)
    if(stic(r,1)==G and stic(y,5)==O):
        arancione(1)
        giallo(-1)
        arancione(-1)
        giallo(-1)
        verde(-1)
        giallo(1)
        verde(1)
    if(stic(g,1)==O and stic(y,1)==G):#GY PPPPPPPP
        giallo(2)
        verde(-1)
        giallo(1)
        verde(1)
        giallo(1)
        arancione(1)
        giallo(-1)
        arancione(-1)
    if(stic(g,1)==G and stic(y,1)==O):
        giallo(1)
        arancione(1)
        giallo(-1)
        arancione(-1)
        giallo(-1)
        verde(-1)
        giallo(1)
        verde(1)
    if(stic(o,1)==O and stic(y,3)==G):#OY
        giallo(-1)
        verde(-1)
        giallo(1)
        verde(1)
        giallo(1)
        arancione(1)
        giallo(-1)
        arancione(-1)
    if(stic(o,1)==G and stic(y,3)==O):
        giallo(2)
        arancione(1)
        giallo(-1)
        arancione(-1)
        giallo(-1)
        verde(-1)
        giallo(1)
        verde(1)
    if(stic(b,1)==O and stic(y,7)==G):#OY
        verde(-1)
        giallo(1)
        verde(1)
        giallo(1)
        arancione(1)
        giallo(-1)
        arancione(-1)
    if(stic(b,1)==G and stic(y,7)==O):
        giallo(-1)
        arancione(1)
        giallo(-1)
        arancione(-1)
        giallo(-1)
        verde(-1)
        giallo(1)
        verde(1)
    #spigoloOB
    print("2 strato OB")
    if(stic(o,5)==O and stic(b,3)==B):
        pass
    if(stic(o,5)==B and stic(b,3)==O):
        blu(1)
        giallo(2)
        blu(-1)
        giallo(1)
        blu(1)
        giallo(2)
        blu(-1)
        giallo(1)
        arancione(-1)
        giallo(-1)
        arancione(1)
    if(stic(b,5)==B and stic(r,3)==O):#BR
        rosso(1)
        giallo(1)
        rosso(-1)
        giallo(-1)
        blu(-1)
        giallo(-1)
        blu(2)
        giallo(-1)
        blu(-1)
        giallo(-1)
        arancione(-1)
        giallo(1)
        arancione(1)
    if(stic(b,5)==O and stic(r,3)==B):
        rosso(1)
        giallo(1)
        rosso(-1)
        giallo(-1)
        blu(-1)
        giallo(-1)
        blu(1)
        giallo(1)
        arancione(-1)
        giallo(1)
        arancione(1)
        giallo(1)
        blu(1)
        giallo(-1)
        blu(-1)
    if(stic(r,1)==B and stic(y,5)==O):#RY
        arancione(-1)
        giallo(1)
        arancione(1)
        giallo(1)
        blu(1)
        giallo(-1)
        blu(-1)
    if(stic(r,1,)==O and stic(y,5)==B):
        giallo(-1)
        blu(1)
        giallo(-1)
        blu(-1)
        giallo(-1)
        arancione(-1)
        giallo(1)
        arancione(1)
    if(stic(g,1)==B and stic(y,1)==O):#GY
        giallo(1)
        arancione(-1)
        giallo(1)
        arancione(1)
        giallo(1)
        blu(1)
        giallo(-1)
        blu(-1)
    if(stic(g,1)==O and stic(y,1)==B):
        blu(1)
        giallo(-1)
        blu(-1)
        giallo(-1)
        arancione(-1)
        giallo(1)
        arancione(1)
    if(stic(o,1)==B and stic(y,3)==O):#OY
        giallo(2)
        arancione(-1)
        giallo(1)
        arancione(1)
        giallo(1)
        blu(1)
        giallo(-1)
        blu(-1)
    if(stic(o,1)==O and stic(y,3)==B):
        giallo(1)
        blu(1)
        giallo(-1)
        blu(-1)
        giallo(-1)
        arancione(-1)
        giallo(1)
        arancione(1)
    if(stic(b,1)==B and stic(y,7)==O):#BY
        giallo(-1)
        arancione(-1)
        giallo(1)
        arancione(1)
        giallo(1)
        blu(1)
        giallo(-1)
        blu(-1)
    if(stic(b,1)==O and stic(y,7)==B):
        giallo(2)
        blu(1)
        giallo(-1)
        blu(-1)
        giallo(-1)
        arancione(-1)
        giallo(1)
        arancione(1)
    #spigoloRB
    print("2 strato RB")
    if(stic(r,3)==R and stic(b,5)==B):#BR
        pass
    if(stic(r,3)==B and stic(b,5)==R):
        rosso(1)
        giallo(2)
        rosso(-1)
        giallo(1)
        rosso(1)
        giallo(2)
        rosso(-1)
        giallo(1)
        blu(-1)
        giallo(-1)
        blu(1)
    if(stic(r,1)==R and stic(y,5)==B):#RY
        giallo(-1)
        blu(-1)
        giallo(1)
        blu(1)
        giallo(1)
        rosso(1)
        giallo(-1)
        rosso(-1)
    if(stic(r,1)==B and stic(y,5)==R):
        giallo(2)
        rosso(1)
        giallo(-1)
        rosso(-1)
        giallo(-1)
        blu(-1)
        giallo(1)
        blu(1)
    if(stic(g,1)==R and stic(y,1)==B):#GY
        blu(-1)
        giallo(1)
        blu(1)
        giallo(1)
        rosso(1)
        giallo(-1)
        rosso(-1)
    if(stic(g,1)==B and stic(y,1)==R):
        giallo(-1)
        rosso(1)
        giallo(-1)
        rosso(-1)
        giallo(-1)
        blu(-1)
        giallo(1)
        blu(1)
    if(stic(o,1)==R and stic(y,3)==B):#OY
        giallo(1)
        blu(-1)
        giallo(1)
        blu(1)
        giallo(1)
        rosso(1)
        giallo(-1)
        rosso(-1)
    if(stic(o,1)==B and stic(y,3)==R):
        rosso(1)
        giallo(-1)
        rosso(-1)
        giallo(-1)
        blu(-1)
        giallo(1)
        blu(1)
    if(stic(b,1)==R and stic(y,7)==B):#BY
        giallo(2)
        blu(-1)
        giallo(1)
        blu(1)
        giallo(1)
        rosso(1)
        giallo(-1)
        rosso(-1)
    if(stic(b,1)==B and stic(y,7)==R):
        giallo(1)
        rosso(1)
        giallo(-1)
        rosso(-1)
        giallo(-1)
        blu(-1)
        giallo(1)
        blu(1)
#_________________________________________________________________________________________________FACCIA GIALLA
    #croce gialla
    if (stic(y,1)!=Y and stic(y,5)!=Y and stic(y,7)!=Y and stic(y,3)!=Y): #SOLO CENTRO GIALLO OK
        rosso(1)
        verde(1)
        giallo(1)
        verde(-1)
        giallo(-1)
        rosso(-1)
        giallo(2)
        rosso(1)
        verde(1)
        giallo(1)
        verde(-1)
        giallo(-1)
        verde(1)
        giallo(1)
        verde(-1)
        giallo(-1)
        rosso(-1)
    if (stic(y,1)==Y and stic(y,5)==Y and stic(y,7)!=Y and stic(y,3)!=Y): #L ANGOLO IN BASSO A DESTRA OK
        giallo(2)
        rosso(1)
        verde(1)
        giallo(1)
        verde(-1)
        giallo(-1)
        verde(1)
        giallo(1)
        verde(-1)
        giallo(-1)
        rosso(-1)
    if (stic(y,1)!=Y and stic(y,5)==Y and stic(y,7)==Y and stic(y,3)!=Y): #L ANGOLO IN BASSO A SINISTRA OK
        giallo(1)
        rosso(1)
        verde(1)
        giallo(1)
        verde(-1)
        giallo(-1)
        verde(1)
        giallo(1)
        verde(-1)
        giallo(-1)
        rosso(-1)
    if (stic(y,1)!=Y and stic(y,5)!=Y and stic(y,7)==Y and stic(y,3)==Y): #L GIUSTA, ANGOLO ALTO SINISTRA OK
        rosso(1)
        verde(1)
        giallo(1)
        verde(-1)
        giallo(-1)
        verde(1)
        giallo(1)
        verde(-1)
        giallo(-1)
        rosso(-1)
    if (stic(y,1)==Y and stic(y,5)!=Y and stic(y,7)!=Y and stic(y,3)==Y): #L ANGOLO ALTO DESTRA OK
        giallo(-1)
        rosso(1)
        verde(1)
        giallo(1)
        verde(-1)
        giallo(-1)
        verde(1)
        giallo(1)
        verde(-1)
        giallo(-1)
        rosso(-1)
    if (stic(y,1)==Y and stic(y,5)!=Y and stic(y,7)==Y and stic(y,3)!=Y): #STRISCIA ORIZZONTALE OK
        rosso(1)
        verde(1)
        giallo(1)
        verde(-1)
        giallo(-1)
        rosso(-1)
    if (stic(y,1)!=Y and stic(y,5)==Y and stic(y,7)!=Y and stic(y,3)==Y): #STRISCIA VERTICALE OK
        giallo(1)
        rosso(1)
        verde(1)
        giallo(1)
        verde(-1)
        giallo(-1)
        rosso(-1)
    if (stic(y,1)==Y and stic(y,5)==Y and stic(y,7)==Y and stic(y,3)==Y): #CROCE GIA' COMPOSTA OK
        pass
    print("croce gialla formata")
    #posizionare spigoli
    while (stic(g,1)!=G and stic(b,1)!=B and stic(r,1)!=R and stic(o,1)!=O) or (stic(g,1)==G and stic(b,1)!=B and stic(r,1)!=R and stic(o,1)!=O) or (stic(g,1)!=G and stic(b,1)==B and stic(r,1)!=R and stic(o,1)!=O) or (stic(g,1)!=G and stic(b,1)!=B and stic(r,1)==R and stic(o,1)!=O) or (stic(g,1)!=G and stic(b,1)!=B and stic(r,1)!=R and stic(o,1)==O):#1 SPIGOLO GIUSTO GLI ALTRI SBAGLIATI
        giallo(1)
    if (stic(g,1)==G and stic(b,1)==B and stic(r,1)!=R and stic(o,1)!=O): #SPIGOLI VERDE E BLU OPPOSTI GIUSTI
        arancione(1)#scambio spigoli opposti OK
        giallo(1)
        arancione(-1)
        giallo(1)
        arancione(1)
        giallo(2)
        arancione(-1)
    if (stic(r,1)==R and stic(o,1)==O and stic(g,1)!=G and stic(b,1)!=B): #SPIGOLI ROSSO E ARANCIONE OPPOSTI GIUSTI
        verde(1)#scambio spigoli opposti OK
        giallo(1)
        verde(-1)
        giallo(1)
        verde(1)
        giallo(2)
        verde(-1)
    if (stic(r,1)==R and stic(o,1)!=O and stic(g,1)==G and stic(b,1)!=B):#ok  SPIGOLO ROSSO E VERDE GIUSTI
        rosso(1)
        giallo(1)
        rosso(-1)
        giallo(1)
        rosso(1)
        giallo(2)
        rosso(-1)
        giallo(1)
    if (stic(r,1)==R and stic(o,1)!=O and stic(g,1)!=G and stic(b,1)==B):#ok  SPIGOLO ROSSO E BLU GIUSTI
        blu(1)
        giallo(1)
        blu(-1)
        giallo(1)
        blu(1)
        giallo(2)
        blu(-1)
        giallo(1)
    if (stic(r,1)!=R and stic(o,1)==O and stic(g,1)==G and stic(b,1)!=B): #ok SPIGOLO VERDE E ARANCIONE GIUSTI
        verde(1)
        giallo(1)
        verde(-1)
        giallo(1)
        verde(1)
        giallo(2)
        verde(-1)
        giallo(1)
    if (stic(r,1)!=R and stic(o,1)==O and stic(g,1)!=G and stic(b,1)==B): #ok SPIGOLO BLU E ARANCIONE GIUSTI
        arancione(1)
        giallo(1)
        arancione(-1)
        giallo(1)
        arancione(1)
        giallo(2)
        arancione(-1)
        giallo(1)
    if (stic(r,1)==R and stic(o,1)==O and stic(g,1)==G and stic(b,1)==B):
        pass
    print ("spigoli gialli sistemati")
    #posizionamento angoli gialli
    print("posizionamento angoli gialli")
    #tutti gli angoli sono sbagliati sia per posizione che per orientamento okbbbbbbb
    if (stic(b,2)!=B or stic(y,8)!=Y or stic(r,0)!=R) and (stic(b,2)!=Y or stic(y,8)!=R or stic(r,0)!=B) and (stic(b,2)!=R or stic(y,8)!=B or stic(r,0)!=Y) and (stic(o,2)!=O or stic(b,0)!=B or stic(y,6)!=Y) and (stic(o,2)!=B or stic(b,0)!=Y or stic(y,6)!=O) and (stic(o,2)!=Y or stic(b,0)!=O or stic(y,6)!=B) and (stic(g,2)!=O or stic(y,0)!=G or stic(o,0)!=Y) and (stic(g,2)!=Y or stic(y,0)!=O or stic(o,0)!=G) and (stic(g,2)!=G or stic(y,0)!=Y or stic(o,0)!=O) and (stic(r,2)!=R or stic(g,0)!=G or stic(y,2)!=Y) and (stic(r,2)!=G or stic(g,0)!=Y or stic(y,2)!=R) and (stic(r,2)!=Y or stic(g,0)!=R or stic(y,2)!=G):
        print("tutti gli angoli sono nella posizione sbagliata")
        verde(1)
        giallo(-1)
        blu(-1)
        giallo(1)
        verde(-1)
        giallo(-1)
        blu(1)
        giallo(1)
    #angolo rosso, giallo, blu nella posizione giusta (anche se orientato sbagliato) e angolo rosso, verde, giallo sbagliato okbbbbbb
    while (((stic(r,0)==R and stic(y,8)==Y and stic(b,2)==B) or (stic(r,0)==Y and stic(y,8)==B and stic(b,2)==R) or (stic(r,0)==B and stic(y,8)==R and stic(b,2)==Y))==1 and ((stic(r,2)==R and stic(g,0)==G and stic(y,2)==Y) or (stic(r,2)==G and stic(g,0)==Y and stic(y,2)==R) or (stic(r,2)==Y and stic(g,0)==R and stic(y,2)==G))==0):  
        print("angolo rosso, giallo, blu nella posizione giusta (anche se orientato sbagliato) e angolo rosso, verde, giallo sbagliato")
        verde(1)
        giallo(-1)
        blu(-1)
        giallo(1)
        verde(-1)
        giallo(-1)
        blu(1)
        giallo(1)
    #angolo rosso, verde, giallo nella posizione giusta (anche se orientato sbagliato) e angolo giallo, verde, arancione sbagliatobbbbbb    
    while (((stic(g,2)==O and stic(y,0)==G and stic(o,0)==Y) or (stic(g,2)==Y and stic(y,0)==O and stic(o,0)==G) or (stic(g,2)==G and stic(y,0)==Y and stic(o,0)==O))==0 and ((stic(r,2)==R and stic(g,0)==G and stic(y,2)==Y)or (stic(r,2)==G and stic(g,0)==Y and stic(y,2)==R) or (stic(r,2)==Y and stic(g,0)==R and stic(y,2)==G))==1):     
        print("angolo rosso, verde, giallo nella posizione giusta (anche se orientato sbagliato) e angolo giallo, verde, arancione sbagliato")
        arancione(1)
        giallo(-1)
        rosso(-1)
        giallo(1)
        arancione(-1)
        giallo(-1)
        rosso(1)
        giallo(1)
    #angolo giallo, verde, arancione nella posizione giusta (anche se orientato sbagliato) e angolo arancione, giallo, blu sbagliatobbbbbbb  
    while (((stic(o,2)==O and stic(b,0)==B and stic(y,6)==Y) or (stic(o,2)==B and stic(b,0)==Y and stic(y,6)==O) or (stic(o,2)==Y and stic(b,0)==O and stic(y,6)==B))==0 and ((stic(g,2)==O and stic(y,0)==G and stic(o,0)==Y) or (stic(g,2)==Y and stic(y,0)==O and stic(o,0)==G) or (stic(g,2)==G and stic(y,0)==Y and stic(o,0)==O))==1):
        print("angolo giallo, verde, arancione nella posizione giusta (anche se orientato sbagliato) e angolo arancione, giallo, blu sbagliato")
        blu(1)
        giallo(-1)
        verde(-1)
        giallo(1)
        blu(-1)
        giallo(-1)
        verde(1)
        giallo(1)
    #angolo arancione, giallo, blu nella posizione giusta (anche se orientato sbagliato) e angolo giallo, rosso, blu sbagliato    
    while (((stic(b,2)==B and stic(y,8)==Y and stic(r,0)==R) or (stic(b,2)==Y and stic(y,8)==R and stic(r,0)==B) or (stic(b,2)==R and stic(y,8)==B and stic(r,0)==Y))==0 and ((stic(o,2)==O and stic(b,0)==B and stic(y,6)==Y) or (stic(o,2)==B and stic(b,0)==Y and stic(y,6)==O) or (stic(o,2)==Y and stic(b,0)==O and stic(y,6)==B))==1):
        print("angolo angolo arancione, giallo, blu nella posizione giusta (anche se orientato sbagliato) e angolo giallo, rosso, blu sbagliato")
        rosso(1)
        giallo(-1)
        arancione(-1)
        giallo(1)
        rosso(-1)
        giallo(-1)
        arancione(1)
        giallo(1)

    #tutti gli angoli sono posizionati giusti, ma non è detto che siano orientati            
    else:
        print("tutti gli angoli sono posizionati giusti, ma non è detto che siano orientati")
        pass
    #orientamento angoli gialli
    print("angoli gialli posizionati")
    #angoli tutti giusti
    if (stic(y,8)==Y and stic(y,6)==Y and stic(y,0)==Y and stic(y,2)==Y):    
        print("Gli angoli sono tutti orientati quindi il cubo risolto!")        
    if (stic(y,8)!=Y and stic(y,6)==Y and stic(y,0)==Y and stic(y,2)==Y):
        print("l'angolo rosso, blu, giallo è orientato sbagliato")
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)          
        print("Il cubo è risolto!")
    if (stic(y,8)==Y and stic(y,6)!=Y and stic(y,0)==Y and stic(y,2)==Y):
        print("l'angolo blu, arancione, giallo è orientato sbagliato")
        giallo(-1)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)
        giallo(1)
        print("Il cubo è risolto!")
    if (stic(y,8)==Y and stic(y,6)==Y and stic(y,0)!=Y and stic(y,2)==Y):
        print("l'angolo verde, arancione, giallo è orientato sbagliato")
        giallo(2)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)
        giallo(2)    
        print("Il cubo è risolto!")
    if (stic(y,8)==Y and stic(y,6)==Y and stic(y,0)==Y and stic(y,2)!=Y):
        print("l'angolo verde, rosso, giallo è orientato sbagliato")
        giallo(1)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)
        giallo(-1)
        print("Il cubo è risolto!")
    if (stic(y,8)!=Y and stic(y,6)!=Y and stic(y,0)==Y and stic(y,2)==Y):
        print("M")
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)
        giallo(-1)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)        
        giallo(1)
        print("Il cubo è risolto!")
    if (stic(y,8)!=Y and stic(y,6)==Y and stic(y,0)!=Y and stic(y,2)==Y):
        print("L")
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)
        giallo(2)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)        
        giallo(2)
        print("Il cubo è risolto!")    
    if (stic(y,8)!=Y and stic(y,6)==Y and stic(y,0)==Y and stic(y,2)!=Y):
        print("A")
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)
        giallo(1)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)        
        giallo(-1)
        print("Il cubo è risolto!")
    if (stic(y,8)==Y and stic(y,6)!=Y and stic(y,0)!=Y and stic(y,2)==Y):
        print("I")
        giallo(-1)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)
        giallo(-1)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)        
        giallo(2)    
        print("Il cubo è risolto!")
    if (stic(y,8)==Y and stic(y,6)!=Y and stic(y,0)==Y and stic(y,2)!=Y):
        print("H")
        giallo(-1)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)
        giallo(2)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)        
        giallo(-1)    
        print("Il cubo è risolto!")
    if (stic(y,8)==Y and stic(y,6)==Y and stic(y,0)!=Y and stic(y,2)!=Y):
        print("G")
        giallo(2)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)
        giallo(-1)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)        
        giallo(-1)    
        print("Il cubo è risolto!")
    if (stic(y,8)!=Y and stic(y,6)!=Y and stic(y,0)!=Y and stic(y,2)==Y):
        print("F")
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)
        giallo(-1)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)
        giallo(-1)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)        
        giallo(2)
        print("Il cubo è risolto!")
    if (stic(y,8)!=Y and stic(y,6)!=Y and stic(y,0)==Y and stic(y,2)!=Y):
        print("D")
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)
        giallo(-1)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)
        giallo(2)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)        
        giallo(-1)
        print("Il cubo è risolto!")
    if (stic(y,8)!=Y and stic(y,6)==Y and stic(y,0)!=Y and stic(y,2)!=Y):
        print("C")
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)
        giallo(2)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)
        giallo(-1)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)        
        giallo(-1)
        print("Il cubo è risolto!")
    if (stic(y,8)==Y and stic(y,6)!=Y and stic(y,0)!=Y and stic(y,2)!=Y):
        print("B")
        giallo(-1)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)
        giallo(-1)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)
        giallo(-1)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)        
        giallo(-1)
        print("Il cubo è risolto!")
    if (stic(y,8)!=Y and stic(y,6)!=Y and stic(y,0)!=Y and stic(y,2)!=Y):
        print("A")
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)
        giallo(-1)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)
        giallo(-1)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)
        giallo(-1)
        while (stic(y,8)!=Y):
            blu(1)
            bianco(1)
            blu(-1)
            bianco(-1)        
        giallo(-1)
        print("Il cubo è risolto!")        
    semplifica()
    invia()
def scansione():
    #inizio scansione telecamera
    #colora gli adesivi del disegno
    carl=tel.scan()
    w0.configure(bg=diz[carl[0]])
    w1.configure(bg=diz[carl[1]])
    w2.configure(bg=diz[carl[2]])
    w3.configure(bg=diz[carl[3]])
    w4.configure(bg=diz[carl[4]])
    w5.configure(bg=diz[carl[5]])
    w6.configure(bg=diz[carl[6]])
    w7.configure(bg=diz[carl[7]])
    w8.configure(bg=diz[carl[8]])
    
    r0.configure(bg=diz[carl[9]])
    r1.configure(bg=diz[carl[10]])
    r2.configure(bg=diz[carl[11]])
    r3.configure(bg=diz[carl[12]])
    r4.configure(bg=diz[carl[13]])
    r5.configure(bg=diz[carl[14]])
    r6.configure(bg=diz[carl[15]])
    r7.configure(bg=diz[carl[16]])
    r8.configure(bg=diz[carl[17]])

    g0.configure(bg=diz[carl[18]])
    g1.configure(bg=diz[carl[19]])
    g2.configure(bg=diz[carl[20]])
    g3.configure(bg=diz[carl[21]])
    g4.configure(bg=diz[carl[22]])
    g5.configure(bg=diz[carl[23]])
    g6.configure(bg=diz[carl[24]])
    g7.configure(bg=diz[carl[25]])
    g8.configure(bg=diz[carl[26]])

    o0.configure(bg=diz[carl[27]])
    o1.configure(bg=diz[carl[28]])
    o2.configure(bg=diz[carl[29]])
    o3.configure(bg=diz[carl[30]])
    o4.configure(bg=diz[carl[31]])
    o5.configure(bg=diz[carl[32]])
    o6.configure(bg=diz[carl[33]])
    o7.configure(bg=diz[carl[34]])
    o8.configure(bg=diz[carl[35]])
    
    b0.configure(bg=diz[carl[36]])
    b1.configure(bg=diz[carl[37]])
    b2.configure(bg=diz[carl[38]])
    b3.configure(bg=diz[carl[39]])
    b4.configure(bg=diz[carl[40]])
    b5.configure(bg=diz[carl[41]])
    b6.configure(bg=diz[carl[42]])
    b7.configure(bg=diz[carl[43]])
    b8.configure(bg=diz[carl[44]])
    
    y0.configure(bg=diz[carl[45]])
    y1.configure(bg=diz[carl[46]])
    y2.configure(bg=diz[carl[47]])
    y3.configure(bg=diz[carl[48]])
    y4.configure(bg=diz[carl[49]])
    y5.configure(bg=diz[carl[50]])
    y6.configure(bg=diz[carl[51]])
    y7.configure(bg=diz[carl[52]])
    y8.configure(bg=diz[carl[53]])

    #mette i dati nella mappa
    assegnaFaccia("w",carl[:9])
    assegnaFaccia("r",carl[9:18])
    assegnaFaccia("g",carl[18:27])
    assegnaFaccia("o",carl[27:36])
    assegnaFaccia("b",carl[36:45])
    assegnaFaccia("y",carl[45:54])

    #fine scansione, inizia a calcolare la soluzione
        
if __name__=="__main__":
    porta()
    finestra=Tk()#crea una finestra
    finestra.configure(bg="black")
    finestra.title("Nome")
    finestra.attributes('-fullscreen',True)

    w0=Label(finestra,bg="white",height=c,width=d)
    w0.grid(column=4,row=8)
    w1=Label(finestra,bg="white",height=c,width=d)
    w1.grid(column=5,row=8)
    w2=Label(finestra,bg="white",height=c,width=d)
    w2.grid(column=6,row=8)
    w3=Label(finestra,bg="white",height=c,width=d)
    w3.grid(column=4,row=9)
    w4=Label(finestra,bg="white",height=c,width=d)
    w4.grid(column=5,row=9)
    w5=Label(finestra,bg="white",height=c,width=d)
    w5.grid(column=6,row=9)
    w6=Label(finestra,bg="white",height=c,width=d)
    w6.grid(column=4,row=10)
    w7=Label(finestra,bg="white",height=c,width=d)
    w7.grid(column=5,row=10)
    w8=Label(finestra,bg="white",height=c,width=d)
    w8.grid(column=6,row=10)

    r0=Label(finestra,bg="white",height=c,width=d)
    r0.grid(column=4,row=4)
    r1=Label(finestra,bg="white",height=c,width=d)
    r1.grid(column=5,row=4)
    r2=Label(finestra,bg="white",height=c,width=d)
    r2.grid(column=6,row=4)
    r3=Label(finestra,bg="white",height=c,width=d)
    r3.grid(column=4,row=5)
    r4=Label(finestra,bg="white",height=c,width=d)
    r4.grid(column=5,row=5)
    r5=Label(finestra,bg="white",height=c,width=d)
    r5.grid(column=6,row=5)
    r6=Label(finestra,bg="white",height=c,width=d)
    r6.grid(column=4,row=6)
    r7=Label(finestra,bg="white",height=c,width=d)
    r7.grid(column=5,row=6)
    r8=Label(finestra,bg="white",height=c,width=d)
    r8.grid(column=6,row=6)

    g0=Label(finestra,bg="white",height=c,width=d)
    g0.grid(column=8,row=4)
    g1=Label(finestra,bg="white",height=c,width=d)
    g1.grid(column=9,row=4)
    g2=Label(finestra,bg="white",height=c,width=d)
    g2.grid(column=10,row=4)
    g3=Label(finestra,bg="white",height=c,width=d)
    g3.grid(column=8,row=5)
    g4=Label(finestra,bg="white",height=c,width=d)
    g4.grid(column=9,row=5)
    g5=Label(finestra,bg="white",height=c,width=d)
    g5.grid(column=10,row=5)
    g6=Label(finestra,bg="white",height=c,width=d)
    g6.grid(column=8,row=6)
    g7=Label(finestra,bg="white",height=c,width=d)
    g7.grid(column=9,row=6)
    g8=Label(finestra,bg="white",height=c,width=d)
    g8.grid(column=10,row=6)

    o0=Label(finestra,bg="white",height=c,width=d)
    o0.grid(column=12,row=4)
    o1=Label(finestra,bg="white",height=c,width=d)
    o1.grid(column=13,row=4)
    o2=Label(finestra,bg="white",height=c,width=d)
    o2.grid(column=14,row=4)
    o3=Label(finestra,bg="white",height=c,width=d)
    o3.grid(column=12,row=5)
    o4=Label(finestra,bg="white",height=c,width=d)
    o4.grid(column=13,row=5)
    o5=Label(finestra,bg="white",height=c,width=d)
    o5.grid(column=14,row=5)
    o6=Label(finestra,bg="white",height=c,width=d)
    o6.grid(column=12,row=6)
    o7=Label(finestra,bg="white",height=c,width=d)
    o7.grid(column=13,row=6)
    o8=Label(finestra,bg="white",height=c,width=d)
    o8.grid(column=14,row=6)

    b0=Label(finestra,bg="white",height=c,width=d)
    b0.grid(column=0,row=4)
    b1=Label(finestra,bg="white",height=c,width=d)
    b1.grid(column=1,row=4)
    b2=Label(finestra,bg="white",height=c,width=d)
    b2.grid(column=2,row=4)
    b3=Label(finestra,bg="white",height=c,width=d)
    b3.grid(column=0,row=5)
    b4=Label(finestra,bg="white",height=c,width=d)
    b4.grid(column=1,row=5)
    b5=Label(finestra,bg="white",height=c,width=d)
    b5.grid(column=2,row=5)
    b6=Label(finestra,bg="white",height=c,width=d)
    b6.grid(column=0,row=6)
    b7=Label(finestra,bg="white",height=c,width=d)
    b7.grid(column=1,row=6)
    b8=Label(finestra,bg="white",height=c,width=d)
    b8.grid(column=2,row=6)

    y6=Label(finestra,bg="white",height=c,width=d)
    y6.grid(column=4,row=0)
    y3=Label(finestra,bg="white",height=c,width=d)
    y3.grid(column=5,row=0)
    y0=Label(finestra,bg="white",height=c,width=d)
    y0.grid(column=6,row=0)
    y7=Label(finestra,bg="white",height=c,width=d)
    y7.grid(column=4,row=1)
    y4=Label(finestra,bg="white",height=c,width=d)
    y4.grid(column=5,row=1)
    y1=Label(finestra,bg="white",height=c,width=d)
    y1.grid(column=6,row=1)
    y8=Label(finestra,bg="white",height=c,width=d)
    y8.grid(column=4,row=2)
    y5=Label(finestra,bg="white",height=c,width=d)
    y5.grid(column=5,row=2)
    y2=Label(finestra,bg="white",height=c,width=d)
    y2.grid(column=6,row=2)

    sp0=Label(finestra,height=a,width=h,bg="black")
    sp0.grid(column=3,row=3)
    sp1=Label(finestra,height=a,width=h,bg="black")
    sp1.grid(column=7,row=7)
    sp2=Label(finestra,height=a,width=h,bg="black")
    sp2.grid(column=11,row=3)
    sp3=Label(finestra,height=c,width=e,bg="black")
    sp3.grid(column=15,row=5)

    btn1=Button(text="START",command=scansione,width=f,font=("Segoe Print",16))
    btn1.grid(column=16,row=4)
    btn_close=Button(text="CHIUDI",command=finestra.destroy,width=f,font=("Segoe Print",16))
    btn_close.grid(column=16,row=6)
    btn_calcola=Button(text="CALCOLA",command=calcola,width=f,font=("Segoe Print",16))
    btn_calcola.grid(column=16,row=5)
    
    finestra.mainloop()
    input()















       
