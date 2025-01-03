#LIBRARY
import random
import datetime

#loop for repeat when game is over
while True :
    ad=input("oyuncu adınızı giriniz == ")
    zaman=datetime.datetime.now() 

    def rulet():
        silah=[0,0,0,1,0,0]
        random.shuffle(silah)
        print("Rus Ruletine hoş geldin", ad)
        print("Tabancada bir mervi var şansın varsa yaşarsın...")
        a=int(input("Eğer cesaretin varsa 3 boş 3 dolu oynayabilirsin cavabın evet ise 1 hayır ise 0 giriniz."))  
        if a==1:
            def zorrulet():
                tabanca=[0,0,0,1,1,1]
                random.shuffle(tabanca)
                print("Cesaretine hayran kaldım", ad)
                print("Bu sefer 3 boş 3 dolu şanslı mısın göreceğiz...")
                while True :
                    input("Tetiği çekmek için ENTER tuşuna basınız (1)")
                    tetik=tabanca.pop(0)
                    if tetik==1:
                        print("HAHAHAHAHAHA KAFANDA PATLADI")
                        print(ad,"ın ölüm tarihi",zaman)
                        ilac()
                        break
                    elif tetik==0:
                        print("TİK TAK TİK TAK !!!!!!")
                    

            zorrulet()
    
        else:
            while True:
                input("Tetiği çekmek için ENTER tuşuna basınız...(2)")
                tkt=silah.pop(0)
                if tkt==1:
                    print("HAHAHAHAHAHA KAFANDA PATLADI")
                    print(ad,"ın ölüm tarihi",zaman)
                    ilac()
                elif tkt==0:
                    print("TİK TAK TİK TAK !!!!!!")
        
    def ilac():
        print("Canlanmak için sana bir fırsat veriyorum", ad, "eğer şırıngalardan dolu şırıngayı seçersen canlanacaksın")
        a=int(input("şırıngalar 6 tanedir seçmek istediğiniz şırınganın oda no söyleyiniz örneğin:2 == "))
        c=random.randrange(1,7)
        if a==c:
            print("ŞANSLI BİR İNSAN OLDUĞUNU SÖYLEMİŞ MİYDİM ?? AAA EVET HATIRLIYORUM")
            print("Dünyaya hoşgeldin!!")
                        
        else:
            if a!=c:
                print("ÇOK YAZIK OLDU HAHAHAHAHAHAHAHA!!!!!")
                print(ad,"ın ölüm tarihi",zaman)

    rulet()