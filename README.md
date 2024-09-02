# Bankamatik_uygulamasi
python bankamatik uygulaması 
Bu kod, bir bankamatik uygulamasını simüle eder. Mehmet ve Ali adında iki kişinin hesap bilgilerini içeren iki sözlük (MehmetHesap ve AliHesap) tanımlanmıştır. Her bir sözlük, kişinin adını, hesap numarasını, mevcut bakiyesini ve ek hesap limitini içerir.

Kodda iki ana fonksiyon bulunmaktadır: paraCek ve bakiyeSorgula. paraCek fonksiyonu, bir hesaptan belirli bir miktar para çekmek için kullanılır. İlk olarak, kullanıcının adı ekrana yazdırılır. Eğer hesap bakiyesi yeterliyse, bakiyeden çekilecek miktar düşülür ve kullanıcıya parayı alabileceği bildirilir. Eğer hesap bakiyesi yeterli değilse, toplam kullanılabilir bakiye (hesap bakiyesi + ek hesap) kontrol edilir. Toplam bakiye yeterliyse, kullanıcıya ek hesap kullanımı sorulur. Eğer kullanıcı ek hesap kullanmayı kabul ederse, ek hesaptan gerekli miktar düşülür ve kullanıcıya parayı alabileceği bildirilir. Aksi takdirde, mevcut bakiye ekrana yazdırılır. Toplam bakiye de yeterli değilse, kullanıcıya bakiye yetersiz olduğu bildirilir.

bakiyeSorgula fonksiyonu ise, bir hesabın mevcut bakiyesini ve ek hesap limitini ekrana yazdırır. Kodun sonunda, Mehmet’in hesabından iki kez para çekme işlemi gerçekleştirilir ve her iki işlemden sonra bakiye sorgulaması yapılır. İlk olarak, Mehmet’in hesabından 2000 TL çekilir ve ardından bakiye sorgulanır. Daha sonra, Mehmet’in hesabından 1000 TL daha çekilir ve bakiye tekrar sorgulanır. Bu işlemler, kullanıcıya hesap bakiyesinin ve ek hesap limitinin nasıl değiştiğini gösterir.



