from socket import *
import random, datetime
from _thread import *

emriServerit = 'localhost'
portiServerit = 13000
s = socket(AF_INET,SOCK_STREAM)

try:
    #vendosja e lidhjes me serverin
    s.bind((emriServerit,portiServerit))
except s.error as gabim:
    print('E pamundur per tu lidhur me serverin' + str(gabim))
#Ndegjimi i serverit per te pranuar klient 
s.listen(5)
print('Serveri eshte gati per te pranuar kerkesa nga klienti.')

#Operacionet e kerkuara ne Projekt
def IPADRESA():
    return str(addr[0])
def PORT():
    return str(addr[1])
def COUNT(tekstiDhene):
    Bashketingellore = ['B','b','C','c','D','d','F','f','G','g','H','h','J','j','K','k','L','l','M','m','N','n','P','p','Q','q','R','r','S','s',
                  'T','t','V','v','X','x','W','w','Y','y','Z','z']
    Zanore =['A','a','e','E','O','o','I','i','y','Y','U','u']
    counteriB=0;
    counteriZ=0;

    for i in str(tekstiDhene):
        if i in Bashketingellore:
            counteriB+=1
        elif i in Zanore:
            counteriZ+=1


    return str('Teksti i future ka '+str(counteriZ) +' zanore dhe '+str(counteriB)+' bashketingellore' )
def PRINTIMI(fjaliaHyrese):
    fjaliaHyrese=str(fjaliaHyrese).strip()
    return str(fjaliaHyrese)
def REVERSE(s): 
    return s[::-1] 
def TIME():
    dataTanishme = datetime.datetime.now()
    return dataTanishme
def GAME():
    return (random.sample(range(1, 35), 5))
def PALINDROME(FJALIA):
   if(FJALIA==REVERSE(FJALIA)):
      return True
   return False
def GCF(nr1,nr2):
    if nr1>nr2:
        nr1,nr2=nr2,nr1
    for x in range (num1,0,-1):
        if nr1%x==0 and nr2%x==0 :
            return x

def CONVERT(zgjedhja,gjatesia):
    if(zgjedhja == 'MileToKm'):
        return(float(gjatesia*1.609344))
    elif(zgjedhja == 'KmToMile'):
        return(float(gjatesia*0.621371192))
    elif(zgjedhja == 'FeetToCm'):
        return(float(gjatesia*30.48))
    elif(zgjedhja=='cmToFeet'):
        return(float(gjatesia*0.032808399))
    else:
        return('Keni shtypur diqka gabim')
#Operacionet e zgjedhura 


def KUBOIDI(brinja1,brinja2,brinja3):
    
    Vellimi = brinja1*brinja2*brinja3
    return  Vellimi
def TRAPEZI(lartesia,baza1,baza2):
    Syprina = ((baza1 + baza2) / 2) * lartesia
    return Syprina

#funksioni per multithread
def thread_klientat():
    while 1:
        
        print('Klienti u lidh ne serverin %s me port %s' % addr)   
        fjaliaArdhur=(bytes)("fjalia string".encode())
        
        try:

            while str(fjaliaArdhur.decode()) != "":

                try:
                    
                    fjaliaArdhur = connectionSocket.recv(128)
                    
                    fjaliaDekoduar = fjaliaArdhur.decode()
                    
                    fjaliaM = fjaliaDekoduar

                    fjaliaM = fjaliaM.split(" ")
                    fjaliaErradhes="".join(fjaliaM[1:]) 
                    fjaliaJoin=" ".join(fjaliaM[1:]) 
                except:
                    print('Klienti ka kerkuar' + fjalia.decode())

                
                if (fjaliaM[0] == 'IPADRESA'):
                    var = IPADRESA()
                    dergimi = ('Ip eshte: '+ str(var))
                    connectionSocket.send(dergimi.encode())
                elif (fjaliaM[0] == 'NUMRIIPORTIT'):
                    var = PORT()
                    dergimi = ('Numri i portit eshte: ' + str(var))
                    connectionSocket.send(dergimi.encode())
                elif (fjaliaM[0] == 'COUNT'):
                    
                    dergimi = COUNT(fjaliaErradhes)
                    connectionSocket.send(dergimi.encode())
                elif(fjaliaM[0]=='PALINDROME'):
                    var=PALINDROME(fjaliaErradhes)
                    dergimi =('Fjalia e dhene eshte palindrome'+ str(var))
                    connectionSocket.send(dergimi.encode())
                elif (fjaliaM[0] == 'REVERSE'):
                    var = REVERSE(fjaliaM)
                    dergimi = ('Teksti ne reverse: '+str(var))
                    connectionSocket.send(dergimi.encode())
                elif (fjaliaM[0] == 'TIME'):
                    var = TIME()
                    dergimi = ('Koha e tanishme ne kompjuter eshte: ' +str(var))
                    connectionSocket.send(dergimi.encode())
                elif (fjaliaM[0] == 'GAME'):
                    var = GAME()
                    dergimi = ('Numrat e gjeneruar te rastit jane: ' +str(var))
                    connectionSocket.send(dergimi.encode())
                
                elif (fjaliaM[0] == 'CONVERT'):
                    var = CONVERT(str(fjaliaM[1]),float(fjaliaM[2]))
                    dergimi = ('Konvertimi qe keni kerkuar eshte: ' +str(var))
                    connectionSocket.send(dergimi.encode())
                elif (fjaliaM[0] == 'GCF'):
                    var = GCF(int(fjaliaM[1])),int(fjaliaM[2])
                    dergimi = ('Faktori me i madh i perbashket i dy numrave eshte: ' +str(var))
                    connectionSocket.send(dergimi.encode())
                elif (fjaliaM[0] == 'KUBOIDI'):
                    var = KUBOIDI(float(fjaliaM[1]),float(fjaliaM[2]),float(fjaliaM[3]))
                    dergimi = ('Vellimi i kuboidit eshte: ' +str(var))
                    connectionSocket.send(dergimi.encode())
                elif (fjaliaM[0] == 'TRAPEZI'):
                    var = TRAPEZI(float(fjaliaM[1]),float(fjaliaM[2]),float(fjaliaM[3]))
                    dergimi = ('Syprina e trapezit eshte: ' +str(var))
                    connectionSocket.send(dergimi.encode())
                else:
                    connectionSocket.send('Operacioni qe keni zgjedhur nuk mund te mundesohet.Rishkruani perseri'.encode())
            connectionSocket.close()
        except Exception as g:
            print("Klienti ka shtypur diqka gabim ose ka mbyllur lidhjen")
            break
while True:
     connectionSocket, addr = s.accept()
     start_new_thread(thread_klientat)
connectionSocket.close()
