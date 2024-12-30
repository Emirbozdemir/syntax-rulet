import random 
def rulet():
    silah=[0,0,0,1,0,0]
    random.shuffle(silah)
    print("Rus Ruletine hoş geldiniz")
    print("Tabancada bir mervi var şansın varsa yaşarsın...")
    a=int(input("Eğer cesaretin varsa 3 boş 3 dolu oynayabilirsin cavabın evet ise 1 hayır ise 0 giriniz."))  
    if a==1:
        def zorrulet():
            tabanca=[0,0,0,1,1,1]
            random.shuffle(tabanca)
            print("Cesaretine hayran kaldım")
            print("Bu sefer 3 boş 3 dolu şanslı mısın göreceğiz...")
            while True :
                input("Tetiği çekmek için ENTER tuşuna basınız")
                tetik=tabanca.pop(0)
                if tetik==1:
                    print("HAHAHAHAHAHA KAFANDA PATLADI")
                    break
                elif tetik==0:
                    print("TİK TAK TİK TAK !!!!!!")
                if not tabanca :
                    break
        zorrulet()
   
    else:
        while True:
            input("Tetiği çekmek için ENTER tuşuna basınız...")
            tkt=silah.pop(0)
            if tkt==1:
                print("HAHAHAHAHAHA KAFANDA PATLADI")
                break
            elif tkt==0:
                print("TİK TAK TİK TAK !!!!!!")
            if not silah:
                break
print(rulet())
