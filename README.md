Wi-Fi Şifre Tahmin Programı
Bu Python uygulaması, işletmelerin Wi-Fi şifrelerini tahmin etmek için bir wordlist (kelime listesi) oluşturan basit bir Tkinter tabanlı grafiksel arayüz sunar. Kullanıcı, belirli bir string ifadesini ve sayısal bir aralığı girerek, bu değerlerin kombinasyonlarından oluşan bir wordlist oluşturabilir ve bunu bir .txt dosyası olarak kaydedebilir.

Özellikler
Kullanıcı dostu bir grafik arayüz ile kolay kullanım.
Belirli bir string ve sayısal aralık ile kelime listesi oluşturma.
Wordlist'i .txt dosyası olarak seçilen konuma kaydetme.
Kullanılan Kütüphaneler
Tkinter: Python'un yerleşik grafiksel arayüz oluşturma kütüphanesi. Bu kütüphane, uygulamanın kullanıcı arayüzünü oluşturmak için kullanıldı.
filedialog: Dosya seçimi ve kaydetme işlemleri için Tkinter'in bir modülü olarak kullanıldı.

#Kurulum
Python 3'ün sisteminizde yüklü olduğundan emin olun.
Bu repoyu yerel makinenize klonlayın:
bash
Kodu kopyala
git clone https://github.com/YUNUSEMREALSANCAK/Wordlistmaker101.git

#Uygulamayı çalıştırmak için şu komutu kullanın:

bash
Kodu kopyala
python main.py

#Kullanım

"String Girişi" alanına Wi-Fi şifresinde yer alabileceğini düşündüğünüz kelimeyi girin (örneğin: starbucks).
"Başlangıç Numarası" ve "Bitiş Numarası" alanlarına sayısal bir aralık girin (örneğin: 1900 ve 2025).
"Wordlist Oluştur ve Kaydet" butonuna tıklayarak kelime listesini oluşturun ve .txt dosyası olarak kaydedin.

#Örnek
Giriş değerleri:

String Girişi: starbucks
Başlangıç Numarası: 1900
Bitiş Numarası: 2025
Oluşan wordlist içeriği:

python
Kodu kopyala
starbucks1900
starbucks1901
starbucks1902
...
starbucks2025
