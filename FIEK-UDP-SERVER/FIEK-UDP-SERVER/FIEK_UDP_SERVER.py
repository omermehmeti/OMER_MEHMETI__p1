from socket import *
import random,datetime


emriServerit ="localhost"
portiServerit  = 13000
soketiServerit = socket(AF_INET, SOCK_DGRAM)
soketiServerit.bind((emriServerit, portiServerit))
print('Serveri eshte gati per te pranuar kerkesa nga klienti.')
#Operacionet e kerkuara ne Projekt
def IPADRESA():
    return str(adresaKlientit[0])
def PORT():
    return str(adresaKlientit[1])
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
   if nr1 > nr2: 
        small = y 
   else: 
        small = x 
   for i in range(1, small+1): 
        if((nr1 % i == 0) and (nr2 % i == 0)): 
            gcd = i 
              
   return gcd 

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
#Operacionet e Shtuara 


def KUBOIDI(brinja1,brinja2,brinja3):
    
    Vellimi = brinja1*brinja2*brinja3
    return  Vellimi
def TRAPEZI(lartesia,baza1,baza2):
    Syprina = ((baza1 + baza2) / 2) * lartesia
    return Syprina

while 1:
       
        fjaliaArdhur=(bytes)("fjalia string ".encode())
        try:

            while str(fjaliaArdhur.decode()) != "":
                try:

                    fjaliaArdhur ,adresaKlientit = soketiServerit.recvfrom(128)
                    
                    fjaliaDekoduar = fjaliaArdhur.decode()
                    fjaliaM =fjaliaDekoduar
    
                    fjaliaM  = fjaliaM .split (" ") 
                    fjaliaErradhes="".join(fjaliaM[1:])
                    fjaliaJoin=" ".join(fjaliaM[1:])
                except:
                    print('Klienti ka kerkuar' + fjalia.decode())

                if (fjaliaM[0] == 'IPADRESA'):
                    var  = IPADRESA();
                    dergimi  = ('Ip eshte: '+ str(var))
                    soketiServerit.sendto(dergimi.encode(),adresaKlientit)             
                elif (fjaliaM[0] == 'PORT'):
                    var = PORT()
                    dergimi = ('Numri i portit eshte: ' + str(var))
                    soketiServerit.sendto(dergimi.encode(),adresaKlientit) 
                elif (fjaliaM[0] == 'COUNT'):
                    var = COUNT(fjaliaErradhes)
                    dergimi = ( str(var))
                    soketiServerit.sendto(dergimi.encode(),adresaKlientit)
                elif(fjaliaM[0]=='PALINDROME'):
                    var = PALINDROME(fjaliaErradhes)
                    dergimi =('Fjalia eshte palindrome '+ str(var))
                    soketiServerit.sendto(dergimi.encode(),adresaKlientit)
                elif (fjaliaM[0] == 'REVERSE'):
                    var = REVERSE(fjaliaErradhes)
                    dergimi = ('Fjalia mbrapshte eshte:'+str(var))
                    soketiServerit.sendto(dergimi.encode(),adresaKlientit)
                elif (fjaliaM[0] == 'TIME'):
                    var = TIME()
                    dergimi = ('Koha e tanishme ne kompjuter eshte: ' +str(var))
                    soketiServerit.sendto(dergimi.encode(),adresaKlientit)      
                elif (fjaliaM[0] == 'GAME'):
                    var = GAME()
                    dergimi = ('Numrat e gjeneruar te rastit jane: ' +str(var))
                    soketiServerit.sendto(dergimi.encode(),adresaKlientit)          
                elif (fjaliaM[0] == 'GCF'):
                    var =  GCF(int(fjaliaM[1]),int(fjaliaM[2]))
                    dergimi = ('Faktori me i madh i perbashket eshte :' +str(var))
                    soketiServerit.sendto(dergimi.encode(),adresaKlientit)        
                elif (fjaliaM[0] == 'CONVERT'):
                    var = CONVERT(str(fjaliaM[1]),float(fjaliaM[2]))
                    dergimi = ('Konvertimi qe keni kerkuar eshte: ' +str(var))
                    soketiServerit.sendto(dergimi.encode(),adresaKlientit)  
                elif (fjaliaM[0] == 'KUBOIDI'):
                    var = KUBOIDI(float(fjaliaM[1]),float(fjaliaM[2]),float(fjaliaM[3]))
                    dergimi = ('Vellimi i kuboidit eshte : ' +str(var))
                    soketiServerit.sendto(dergimi.encode(),adresaKlientit)
                elif (fjaliaM[0] == 'TRAPEZI'):
                    var = TRAPEZI(float(fjaliaM[1]),float(fjaliaM[2]),float(fjaliaM[3]))
                    dergimi = ('Syrina e trapezit eshte: ' +str(var))
                    soketiServerit.sendto(dergimi.encode(),adresaKlientit)

                else:
                    serverSocket.sendto('Operacioni qe keni zgjedhur nuk eshte ne rregull.Rishkruani perseri',adresaKlientit)
       
        except Exception as gabim:
            print('Klienti ka shtypur diqka gabim ose ka mbyllur lidhjen')
            
    

