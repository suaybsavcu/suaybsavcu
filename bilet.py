print("Korku tüneline hoş geldiniz...")

boy = int(input('Boyunuzun uzunluğu "santimetre" cinsinden giriniz...\n'))

if boy >= 120 :
    print("Korku tüneline binebilirsiniz...")

    yas = int(input("Bilet parası için kaç yaşında olduğunuzu söyler misiniz?\n"))

    if yas >= 18:
        print("Bilet ücretleriniz: 25 TL")
    
    elif yas <= 23:
        print("Bilet ücretiniz: 35 TL")

else:
    print("Üzgünüz, Korku tüneline binme koşulunu sağlamıyorsunuz...")
