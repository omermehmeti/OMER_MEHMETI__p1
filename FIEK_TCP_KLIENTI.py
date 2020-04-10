from socket import *


#emriServerit = 'localhost'
#portiServerit = 13000
klientSoketi = socket(AF_INET,SOCK_STREAM)
emriServerit = input('Shenoni emrin e serverit: ')
portiServerit = int(input('Shenoni portin e serverit: '))

if (portiServerit>=1024 and portiServerit<=65535):
    klientSoketi.connect((emriServerit, portiServerit))
    print('Jeni lidhur me serverin\n')
else:
    print('Shenoni portin mes kufive te caktuar')

print('========================================================================================================================')
print('Serveri mund te kryej keto Operacione: IPADRESA, PORT, COUNT, REVERSE,' 
'\n\t\t\t\t\tPALINDROME, TIME, GAME, GCF, CONVERT,KUBOIDI,TRAPEZI')
print('========================================================================================================================')
print('1.IPADRESA kthen  Ipadresen e serverit.\n2.PORT kthen portin e serverit.'
      '\n3.COUNT kthen numrin e bashKtinglloreve dhe te zanoreve te shenuara nga nje fjali.Sheno {HAPSIRE} teksti:'
      '\n4.PALINDROME kthen fjaline NQS ESHTE PALINDROME  .Sheno {HAPSIRE} tekst.\n'
      '5.REVERSE kthen fjaline te shkruare mbrapshte Sheno {HAPSIRE} teksti.'
      '\n6.TIME kthen kohen(oren).''\n7.Operacioni GAME kthen numrat e rastit nga 1-35.'
      '\n8.GCF kthen faktorin me te madh te perbashket.Sheno {Hapsirë} Numër {Hapsirë} Numër'
      '\n9.CONVERT konverton njesit.''Lista e parametrave te KONVERTIMI janë:[MileToKm,'
      'KmToMile,''\n\t\t\t\t\t\tFeetToCm,CmToFeet]'
      '\n\t\t\t\t\t\tSheno {Hapsirë} Opcioni {Hapsirë} Numër\n'
      'Operacione e shtuara\n '
      '1.KUBOIDI kthen vellimin e kuboidit te formuar nga tre brinje Sheno {Hapsirë} Numër {Hapsirë} Numër {Hapsirë} Numër\n' 
      '2.TRAPEZI kthen syprinen e trapezit Sheno {Hapsirë} Numër {Hapsirë} Numër {Hapsirë} Numër \n'
      
      
      '\nSheno Perfundo per te mbyllur lidhjen me serverin')
print('========================================================================================================================')
while True:
    #inputi qe shenohet nga klienti se qka deshiron
    fjaliaHyrese = input('Shenoni njerin nga opsionet qe deshironi ta zgjidhni: ')
    #dergimi ne server ,gjithqka qe dergohet duhet te enkodohet
    klientSoketi.sendall(fjaliaHyrese.encode())
    #fjalia qe pranohet nga serveri
    fjaliaPranuar = klientSoketi.recv(128)
    print("Nga serveri " + fjaliaPranuar.decode())
    if(fjaliaHyrese == 'Perfundo'):
        print("Keni mbyllur lidhjen me serverin.Diten e mire")
        break
klientSoketi.close()


