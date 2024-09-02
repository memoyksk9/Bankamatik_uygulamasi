# Bankamatik Uygulaması

# Mehmet'in hesap bilgileri
MehmetHesap = {
    'ad': 'Mehmet Yüksek',
    'hesapno': '13443287',
    'bakiye': 2000,
    'ekHesap': 2000
}

# Ali'nin hesap bilgileri
AliHesap = {
    'ad': 'Ali Yüksek',
    'hesapno': '1453561',
    'bakiye': 3000,
    'ekHesap': 1000
}

# Para çekme fonksiyonu
def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")
    # Eğer hesap bakiyesi yeterliyse
    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar  # Bakiyeden miktarı düş
        print('Paranızı alabilirsiniz.')
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']  # Toplam kullanılabilir bakiye
        # Eğer toplam bakiye yeterliyse
        if toplam >= miktar:
            ekHesapKullanimi = input('Ek hesap kullanılsın mı (e/h): ')
            if ekHesapKullanimi == 'e':
                ekhesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0  # Ana hesap bakiyesini sıfırla
                hesap['ekHesap'] -= ekhesapKullanilacakMiktar  # Ek hesaptan kalan miktarı düş
                print('Paranızı alabilirsiniz.')
            else:
                print(f"{hesap['hesapno']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır.")
        else:
            print('Üzgünüz, bakiye yetersiz.')

# Bakiye sorgulama fonksiyonu
def bakiyeSorgula(hesap):
    print(f"{hesap['hesapno']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")

# Mehmet'in hesabından 2000 TL çekme işlemi
paraCek(MehmetHesap, 2000)
# Mehmet'in hesap bakiyesini sorgulama
bakiyeSorgula(MehmetHesap)

print('*************************')

# Mehmet'in hesabından 1000 TL daha çekme işlemi
paraCek(MehmetHesap, 1000)
# Mehmet'in hesap bakiyesini tekrar sorgulama
bakiyeSorgula(MehmetHesap)
