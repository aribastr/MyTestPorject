import math
import webbrowser

# Resim ekleme kodu
webbrowser.open("aci_gorsel.png")

print("BU PROGRAM, ZAVİYE AÇISI BELLİ OLMAYAN TEKNİK RESİMLERDE ZAVİYE AÇISINI HESAPLAMAK İÇİN, POLİGON PLANLAMA BİRİMİ TARAFINDAN OLUŞTURULMUŞTUR.")
print("LÜTFEN AÇILAN RESİMDEKİ YÖNERGELERE UYARAK İSTENİLEN DEĞERLERİ GİRİNİZ. (ONDALIKLI DEĞERELERİ YAZMAK İÇİN . nokta KULLANINIZ.)\n")
def tekrar_hesaplama():
  while True:
    try:
      a = float(input("a Ölçüsünü Giriniz (mm): "))
      break
    except ValueError:
      print("Geçersiz giriş. Lütfen sadece sayı giriniz.")

  while True:
    try:
      b = float(input("b Ölçüsünü Giriniz (mm): "))
      break
    except ValueError:
      print("Geçersiz giriş. Lütfen sadece sayı giriniz.")

  hipotenüs = (((a**2)+(b**2))**0.5)
  c = math.asin(a/hipotenüs)
  d = 90-(c*180/math.pi)

  hipotenüs = round(hipotenüs,2)
  d = round(d,2)

  print("\n")
  print (f"Kesim Yapılan Kenarın Uzunluğu: {hipotenüs} MM. \nUyarı ! Eğer Minimal Parametresinde Kesim Yapılıyorsa Hipotenüs Hesaplanan Değerden Kısa Çıkacaktır.")
  print (f"Kesim Açısı: {d}°")

tekrar = True
while tekrar:
  tekrar_hesaplama()
  print("\n")
  secim = str(input("Tekrar hesaplama yapmak ister misiniz? (E/H): ").upper())
  if str(secim) == "E":
    tekrar = True
    continue
  elif str(secim) == "H":
    tekrar = False
    break
  else:
    print("Geçersiz seçim. Lütfen E veya H giriniz.")
    tekrar = input("Tekrar hesaplama yapmak ister misiniz? (E/H): ").upper()
    break
