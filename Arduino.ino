//HIGH significa 5V sui pin ENABLE, DIR e STEP
//LOW significa 0V sui pin ENABLE, DIR e STEP
#define u_ 20                  //definisce i pin degli enable dei driver
#define b_ 19
#define r_ 17
#define f_ 21
#define l_ 18
#define d_ 16

#define STEP 15                //definisce step e direzioni comuni
#define DIR 14

#define on LOW                 //definisce la costante on che rappresenta LOW 
                               //ovvero il driver attivo (ENABLE=0)
#define off HIGH               //definisce la costante off che rappresenta HIGH
                               //ovvero il driver disattivo (ENABLE=1)
#define orario HIGH            //definisce la costante orario che rappresenta HIGH 
                               //ovvero il verso di rotazione (DIR=1)
#define antiorario LOW         //definisce la costante antiorario che rappresenta LOW 
                               //ovvero il verso di rotazione (DIR=0)

#define tempo 1000             //pausa di 1000 micro secondi che regola la velocità durante
                               //la commutazione dello STEP da 0 a 1 e da 1 a 0 (nel ciclo for)
#define passi 50               //numero di passi nel ciclo for (corrisponde ad un angolo di 90°)
#define stabilizzazione 30     //per quanto viene tenuto fermo il motore dopo la rotazione
#define pausa 30               //pausa 30ms tra una mossa e l'altra
String input;
void setup() {
  
  Serial.begin(9600);          //Arduino trasmette dati con una velocità di 9600 bit al secondo
  for(int k=10;k<22;k++)       //imposta tutti i pin (ENABLE, STEP, DIR) come uscite e gli 
                               //assegna il valore HIGH=1 (driver disattivi)
  {
   pinMode(k,OUTPUT);          //k assume i valori dal 16 al 21, che sono i pin ENABLE, STEP e DIR
   digitalWrite(k,HIGH);
  }
  V12(on);                     //chiude il contatto del relè, così ai driver arrivano i 12V
}
void loop() 
{
  if (Serial.available()>0)
  {
    input=Serial.readStringUntil('\n');
    if (input=="Y1") 
    {
      u();
      Serial.write("u1");
    }
    if (input=="Y2") 
    {
      u2();//_________________________________________________________________
      Serial.write("u2");
    }
    if (input=="Y-1") 
    {
      u1();
      Serial.write("u-1");
    }
     if (input=="R1") 
    {
      f();
      Serial.write("f1");
    }
     if (input=="R2") 
    {
      f2();//_________________________________________________________________
      Serial.write("f2");
    }
    if (input=="R-1") 
    {
      f1();
      Serial.write("f-1");
    }
     if (input=="G1") 
    {
      r();
      Serial.write("r1");
    }
     if (input=="G2") 
    {
      r2();//_________________________________________________________________
      Serial.write("r2");
    }
     if (input=="G-1") 
    {
      r1();
      Serial.write("r-1");
    }
     if (input=="B1") 
    {
      l();
      Serial.write("l1");
    }
    if (input=="B2") 
    {
      l2();//________________________________________________________________
      Serial.write("l2");
    }
    if (input=="B-1") 
    {
      l1();
      Serial.write("l-1");
    }
     if (input=="O1") 
    {
      b();
      Serial.write("b1");
    }
    if (input=="O2") 
    {
      b2();//_______________________________________________________________
      Serial.write("b2");
    }
    if (input=="O-1") 
    {
      b1();
      Serial.write("b-1");
    }
     if (input=="W1") 
    {
      d();
      Serial.write("d1");
    }
     if (input=="W2") 
    {
      d2();
      Serial.write("d2");
    }
    if (input=="W-1") 
    {
      d1();
      Serial.write("d-1");
    }
  }
}
//____________________________________________________________________ANTIORARIO
void r1()
{
  digitalWrite(DIR,antiorario);
  digitalWrite(r_,LOW);
  for(int k=0;k<passi;k++)
  {
    digitalWrite(STEP,HIGH);
    delayMicroseconds(tempo);
    digitalWrite(STEP,LOW);
    delayMicroseconds(tempo);
  }
  delay(stabilizzazione);
  digitalWrite(r_,HIGH);
  delay(pausa);
}
void l1()
{
  digitalWrite(DIR,antiorario);
  digitalWrite(l_,LOW);
  for(int k=0;k<passi;k++)
  {
    digitalWrite(STEP,HIGH);
    delayMicroseconds(tempo);
    digitalWrite(STEP,LOW);
    delayMicroseconds(tempo);
  }
  delay(stabilizzazione);
  digitalWrite(l_,HIGH);
  delay(pausa);
}
void f1()
{
  digitalWrite(DIR,antiorario);      //assegna al pin DIR il valore antiorario (LOW, DIR=0)
  digitalWrite(f_,LOW);              //assegna al pin ENABLE del driver che comanda il 
                                     //motore Front "on" (LOW, ENABLE=0) 
  for(int k=0;k<passi;k++)           //per 50 volte alza e abbassa l'uscita del pin step 
  {
    digitalWrite(STEP,HIGH);
    delayMicroseconds(tempo);        //velocità di commutazione dello step
    digitalWrite(STEP,LOW);
    delayMicroseconds(tempo);
  }
  delay(stabilizzazione);            //l'ENABLE è ancora = 0, quindi il driver continua 
                                     //ad alimentare la stessa fase del motore 
                                     //tenendolo fermo su quel passo, 
                                     //quindi non ruota per inerzia
  digitalWrite(f_,HIGH);             //dopo che il motore è stato farmato in una posizione 
                                     //stabile disattivo il driver (ENABLE=1)
  delay(pausa);                      //fa una pausa tra una mossa e l'altra
}
void u1()
{
  digitalWrite(DIR,antiorario);
  digitalWrite(u_,LOW);
  for(int k=0;k<passi;k++)
  {
    digitalWrite(STEP,HIGH);
    delayMicroseconds(tempo);
    digitalWrite(STEP,LOW);
    delayMicroseconds(tempo);
  }
  delay(stabilizzazione);
  digitalWrite(u_,HIGH);
  delay(pausa);
}
void b1()
{
  digitalWrite(DIR,antiorario);
  digitalWrite(b_,LOW);
  for(int k=0;k<passi;k++)
  {
    digitalWrite(STEP,HIGH);
    delayMicroseconds(tempo);
    digitalWrite(STEP,LOW);
    delayMicroseconds(tempo);
  }
  delay(stabilizzazione);
  digitalWrite(b_,HIGH);
  delay(pausa);
}
void d1()
{
  digitalWrite(DIR,antiorario);
  digitalWrite(d_,LOW);
  for(int k=0;k<passi;k++)
  {
    digitalWrite(STEP,HIGH);
    delayMicroseconds(tempo);
    digitalWrite(STEP,LOW);
    delayMicroseconds(tempo);
  }
  delay(stabilizzazione);
  digitalWrite(d_,HIGH);
  delay(pausa);
}
//____________________________________________________________________________DOPPIE
void r2()
{
  digitalWrite(DIR,antiorario);
  digitalWrite(r_,LOW);
  for(int k=0;k<passi*2;k++)
  {
    digitalWrite(STEP,HIGH);
    delayMicroseconds(tempo);
    digitalWrite(STEP,LOW);
    delayMicroseconds(tempo);
  }
  delay(stabilizzazione);
  digitalWrite(r_,HIGH);
  delay(pausa);
}
void l2()
{
  digitalWrite(DIR,antiorario);
  digitalWrite(l_,LOW);
  for(int k=0;k<passi*2;k++)
  {
    digitalWrite(STEP,HIGH);
    delayMicroseconds(tempo);
    digitalWrite(STEP,LOW);
    delayMicroseconds(tempo);
  }
  delay(stabilizzazione);
  digitalWrite(l_,HIGH);
  delay(pausa);
}
void f2()
{
  digitalWrite(DIR,antiorario);
  digitalWrite(f_,LOW);
  for(int k=0;k<passi*2;k++)
  {
    digitalWrite(STEP,HIGH);
    delayMicroseconds(tempo);
    digitalWrite(STEP,LOW);
    delayMicroseconds(tempo);
  }
  delay(stabilizzazione);
  digitalWrite(f_,HIGH);
  delay(pausa);
}
void u2()
{
  digitalWrite(DIR,antiorario);
  digitalWrite(u_,LOW);
  for(int k=0;k<passi*2;k++)
  {
    digitalWrite(STEP,HIGH);
    delayMicroseconds(tempo);
    digitalWrite(STEP,LOW);
    delayMicroseconds(tempo);
  }
  delay(stabilizzazione);
  digitalWrite(u_,HIGH);
  delay(pausa);
}
void b2()
{
  digitalWrite(DIR,antiorario);
  digitalWrite(b_,LOW);
  for(int k=0;k<passi*2;k++)
  {
    digitalWrite(STEP,HIGH);
    delayMicroseconds(tempo);
    digitalWrite(STEP,LOW);
    delayMicroseconds(tempo);
  }
  delay(stabilizzazione);
  digitalWrite(b_,HIGH);
  delay(pausa);
}
void d2()
{
  digitalWrite(DIR,antiorario);
  digitalWrite(d_,LOW);
  for(int k=0;k<passi*2;k++)
  {
    digitalWrite(STEP,HIGH);
    delayMicroseconds(tempo);
    digitalWrite(STEP,LOW);
    delayMicroseconds(tempo);
  }
  delay(stabilizzazione);
  digitalWrite(d_,HIGH);
  delay(pausa);
}
//____________________________________________________________________________ORARIO
void r()
{
  digitalWrite(DIR,orario);
  digitalWrite(r_,LOW);
  for(int k=0;k<passi;k++)
  {
    digitalWrite(STEP,HIGH);
    delayMicroseconds(tempo);
    digitalWrite(STEP,LOW);
    delayMicroseconds(tempo);
  }
  delay(stabilizzazione);
  digitalWrite(r_,HIGH);
  delay(pausa);
}
void u()
{
  digitalWrite(DIR,orario);
  digitalWrite(u_,LOW);
  for(int k=0;k<passi;k++)
  {
    digitalWrite(STEP,HIGH);
    delayMicroseconds(tempo);
    digitalWrite(STEP,LOW);
    delayMicroseconds(tempo);
  }
  delay(stabilizzazione);
  digitalWrite(u_,HIGH);
  delay(pausa);
}
void b()
{
  digitalWrite(DIR,orario);
  digitalWrite(b_,LOW);
  for(int k=0;k<passi;k++)
  {
    digitalWrite(STEP,HIGH);
    delayMicroseconds(tempo);
    digitalWrite(STEP,LOW);
    delayMicroseconds(tempo);
  }
  delay(stabilizzazione);
  digitalWrite(b_,HIGH);
  delay(pausa);
}
void l()
{
  digitalWrite(DIR,orario);
  digitalWrite(l_,LOW);
  for(int k=0;k<passi;k++)
  {
    digitalWrite(STEP,HIGH);
    delayMicroseconds(tempo);
    digitalWrite(STEP,LOW);
    delayMicroseconds(tempo);
  }
  delay(stabilizzazione);
  digitalWrite(l_,HIGH);
  delay(pausa);
}
void f()
{
  digitalWrite(DIR,orario);
  digitalWrite(f_,LOW);
  for(int k=0;k<passi;k++)
  {
    digitalWrite(STEP,HIGH);
    delayMicroseconds(tempo);
    digitalWrite(STEP,LOW);
    delayMicroseconds(tempo);
  }
  delay(stabilizzazione);
  digitalWrite(f_,HIGH);
  delay(pausa);
}
void d()
{
  digitalWrite(DIR,orario);
  digitalWrite(d_,LOW);
  for(int k=0;k<passi;k++)
  {
    digitalWrite(STEP,HIGH);
    delayMicroseconds(tempo);
    digitalWrite(STEP,LOW);
    delayMicroseconds(tempo);
  }
  delay(stabilizzazione);
  digitalWrite(d_,HIGH);
  delay(pausa);
}
//____________________________________________________________________________
void V12(int stato)                   
{
  pinMode(22,OUTPUT);                   //imposta il pin che comanda il relè come uscita
  if (stato==on)                        //se voglio chiudere il contatto (accendere i 12V)
  {
    digitalWrite(22,HIGH);              //chiude il contatto al relè alimentando la bobina
  } 
  else
  {
    digitalWrite(22,LOW);
  }
}
