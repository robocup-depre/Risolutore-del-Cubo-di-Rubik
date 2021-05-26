from serial import *
import time
ser=0
soluzione=[]

def porta():
    global ser 
    while True:
        COM=input("Inserire porta COM: ")
        try:
            ser=Serial(COM,9600,timeout=0.3)
            break
        except SerialException:
            print("PORTA NON VALIDA")
            
def porta_scan():
    port=""
    for k in range(20):
        try:
            port=str("COM"+str(k))
            print(port+"?")
            ser=Serial(port,9600,timeout=0.3)
            if scrivi("R1")=="r1":
                ser.close()
                return port
            ser.close()
        except:
            print("no")
    return 0
    
            
def scrivi(messaggio):
    messaggio.strip()
    ser.write(messaggio.encode())
    time.sleep(0.9)
    return ser.readline().decode('ascii')

def aggiungi(mossa):#mossa=['R',1]______es. soluzione:[['Y',2],[R,-1]]
    global ser#oggetto porta seriale
    soluzione.append(mossa)#aggiunge la coppia [faccia,n_rotazioni] alla lista di mosse
    return soluzione

def opposto(colore):
    if colore=='R':
        return 'O'
    if colore=='O':
        return 'R'
    if colore=='Y':
        return 'W'
    if colore=='W':
        return 'Y'
    if colore=='B':
        return 'G'
    if colore=='G':
        return 'B'
    
def semplifica():
    azioni=1
    while azioni==1:
        azioni=0
        for k in range(len(soluzione)-1):#per ogni elemento dell'array
            if k<len(soluzione)-1:#se dopo aver tolto mosse inutili esiste ancora l'elemento k
                corrente=soluzione[k]
                prossima=soluzione[k+1]
                if corrente[0]==prossima[0]:#se la stessa faccia è in due mosse consecutive somma il numero di mosse
                    soluzione[k][1]+=prossima[1]
                    del soluzione[k+1]#elimina la mossa successiva, perchè è stata incorporata con quella corrente
                    azioni=1
            if k<len(soluzione)-2:#se la stessa faccia è in due mosse con un'altra in mezzo della faccia opposta le unisce
                corrente=soluzione[k]
                prossima=soluzione[k+1]
                prossima2=soluzione[k+2]
                if corrente[0]==prossima2[0] and corrente[0]==opposto(prossima[0]):
                    soluzione[k][1]+=prossima2[1]
                    del soluzione[k+2]
                    azioni=1
            else:#se non esistono più gli elementi successivi esce dal ciclo for
                break
    
    for k in soluzione:#corregge il numero di mosse(es. 5=1, 4=0)
        k[1]%=4
        
    i=0
    for k in soluzione:#corregge il numero di mosse(es. 3=-1)
        if k[1]==3:
            k[1]=-1
            azioni=1
        if k[1]==-3:
            k[1]==1
            azioni=1
        if k[1]==-2:
            k[1]==2
            azioni=1
        if k[1]==0:#se la somma delle due mosse consecutive è 0 elimina la mossa
            del soluzione[i]
            azioni=1
        i+=1
    return soluzione
            
def invia():
    global ser
    messaggio=""
    for k in range(len(soluzione)-1):
        if soluzione[k][1]==-1:
            soluzione[k][1]==3

    print('Invio soluzione')
    for k in soluzione:
        messaggio=k[0]+str(k[1])#unisce faccia e numero di rotazioni in un'unica stringa
        messaggio.strip()
        print(".")
        try:
            ser.write(messaggio.encode())
            time.sleep(0.9)
            ser.readline().decode('ascii')
        except:
            print("Errore di comunicazione")
            return 0
    print("Inviata soluzione!")




