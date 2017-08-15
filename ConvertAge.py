yas = int(input("Yasinizi Giriniz: "))
print("-"*15)

yilSaniye = 365*24*60*60

def hesap(yas, yilSaniye):
    yasSaniye = yas * yilSaniye
    return (yasSaniye)
cikti = hesap(yas, yilSaniye)
print("Yasinizin Saniye Karsiligi: ", cikti)
