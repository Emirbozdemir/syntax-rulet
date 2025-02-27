import random
import datetime

ad=input("oyuncu adınızı giriniz == ")
zaman=datetime.datetime.now()


kasa=0
prize=int(input("Girmek istediğiniz bahis miktarını yazınız == "))
kasa=kasa+prize
toplam=kasa



def ilac():
    print("Canlanmak için sana bir fırsat veriyorum",ad,"eğer şırıngalardan dolu olanı seçersen canlanacaksın")
    a=int(input("Şırıngalar 6 tanedir.Seçmek istediğiniz şırınganın oda numarasını söyleyiniz örneğin 2 == "))
    c=random.randrange(1,7)
    if a == c :
        print("ŞANSLI BİR İNSAN OLDUĞUNU SÖYLEMİŞ MİYDİM ? AAA EVET HATIRLIYORUM")
        print("Dünyaya hoşgelin",ad,"Doğum tarihi",zaman)
        rulet()
    else:
        print("ÇOK YAZIK OLDU HAHAHAHAHAHAHAHAHAHA!!!!!!")
        print(ad,"`ın ölüm tarihi",zaman)
        exit()
        
def zorrulet():
    tabanca = [1, 1, 1, 0, 0, 0]
    random.shuffle(tabanca)
    print("Cesaretine hayran kaldım", ad)
    print("Bu sefer 3 boş 3 dolu, şanslı mısın göreceğiz...")
    while True:
        input("Tetiği çekmek için ENTER tuşuna basınız")
        tetik = tabanca.pop(0)
        if tetik == 1:
            print("HAHAHAHAHA KAFANDA PATLADI")
            print(ad, "'ın ölüm tarihi", zaman)
            ilac()
        elif tetik == 0:
            print("Demek sıra bende, silah elimde. Ya sana sıkarsam? HAHAHAHAHAHA ŞAKAAAAA")
            print("Rakip kendine sıkar")
            while True:
                tetik = tabanca.pop(0)
                if tetik == 1:
                    yeni_bahis1=toplam*20
                    print("Kazandınız, işte ödülünüz!",yeni_bahis1,"$")
                    print("kasadaki miktar == ",yeni_bahis1,"$")
                    tur=(int(input("Daha çok para kazanmak ister misin ??? Paranı arttırmak istersen 1 e yeterli diyorsan 0 a bas " )))
                    
                    if tur==1:
                        
                        rulet()
                        
                    else:
                        exit()
                    return
                elif tetik == 0:
                    print("HAHAHAHAHAHA BENDEN KURTULUŞUN YOK")


def rulet():
    kasa=0
    prize=int(input("Girmek istediğiniz bahis miktarını tekrar yazınız == "))
    kasa=kasa+prize
    silah = [0, 0, 0, 1, 0, 0]
    random.shuffle(silah)
    print("Rus Ruletine Hoşgeldiniz")
    print("Tabancada bir mermi var, şansın varsa yaşarsın...")
    a = int(input("Eğer cesaretin varsa 3 boş 3 dolu oynayabilirsiniz eğer kabul ederseniz kazancınızın 10x olarak alacaksınız cevabınız evet ise 1, hayır ise 0 tuşlayınız == "))
    
    if a == 1:
        zorrulet()  
    elif a==0:
        while True:
            input("Tetiği çekmek için ENTER tuşuna basınız...")
            tkt = silah.pop(0)
            if tkt == 1:
                print("HAHAHAHAHAHAHA KAFANDA PATLADI")
                print(ad, "'ın ölüm tarihi", zaman)
                ilac()
            elif tkt == 0:
                print("Demek sıra bende, silah elimde. Ya sana sıkarsam? HAHAHAHAHAHAHA ŞAKAAAAA")
                print("Rakip kendine sıkar")
                tkt = silah.pop(0)
                if tkt == 1:
                    yeni_bahis=toplam*2
                    print("KAZANDINIZ, İŞTE ÖDÜLÜNÜZ!",yeni_bahis,"$")
                    turr=(int(input("Daha çok para kazanmak ister misin ??? Paranı arttırmak istersen 1 e yeterli diyorsan 0 a bas " )))
                    if turr==1:                        
                        kasa=yeni_bahis
                        rulet()
                            
                    else:
                        exit()
                elif tkt == 0:
                    print("HAHAHAHAHAHA BENDEN KURTULUŞUN YOK ")
            else:
                print("lütfen 1 veya 0 giriniz")
    else:
        print("lütfen 1 veya 0 giriniz")
        rulet()


rulet()
                            
