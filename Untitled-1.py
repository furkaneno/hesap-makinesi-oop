from code import compile_command
from hashlib import shake_128
from tkinter import *#kutuphanemizi cagırdık

def yaz(x): # bir nolu butona basınca yukarı 1 i gonder
   
    s = len(giris.get()) # s degiskenine giris deki degerin uzunlugu ataıyor

    giris.insert(s,str(x)) # s degerinden baslıyor
        
    #print(x)

hesap = 5
sayi1 = 0

def degerler(x):

    global hesap
    hesap = x

    global sayi1
    sayi1 = int(giris.get())

    print(hesap)
    print(sayi1)

    giris.delete(0,'end')


sayi2 = 0

def hesapla():
    global sayi2

    sayi2 = int(giris.get())

    print(sayi2)

    global hesap

    sonuc = 0

    if(hesap == 0):
        sonuc = sayi1+sayi2

    elif(hesap == 1):
        sonuc = sayi1-sayi2

    elif(hesap == 2):
        sonuc = sayi1*sayi2

    elif(hesap == 3):
        float ; sonuc = sayi1/sayi2

    giris.delete(0,'end')
    giris.insert(0,str(sonuc))
    
 
def temizle():
    global temiz
    giris.delete(0,'end')



pencere = Tk() #ekrana pencere gelmesi icin

pencere.geometry("500x400") # pencerenin boyutu

giris = Entry(font = "verdana 15 bold",width=25,justify=LEFT) #left diyerek soldan yazmak istedik
giris.place(x = 10,y = 10) # ekranda acilan kucuk yazı yazilan karenin koordinatları


b = [] # b diye bir bos kume tanimliyoruz

for i in range(1,10): # 1 den 9 a kadar butonlara numara vericez
    b.append(Button(text=str(i),fg="BLUE",font="verdana 25 bold",command=lambda x=i:yaz(x)))

sayac = 0

for i in range(0,3): # 3 e 3 bir i,j matrisi açtık
    for j in range(0,3):
        b[sayac].place(x=40+j*80,y=70+i*80)
        sayac += 1


islem = [] # islemler icin bos dizi

for i in range(0,4):
    islem.append(Button(font="verdana 15",fg="PURPLE",width=15,command=lambda x=i:degerler(x)))

islem[0]['text'] = "topla knka"
islem[1]['text'] = "cıkar gitsin"
islem[2]['text'] = "çarparım bitane"
islem[3]['text'] = "paramparça"

for i in range(0,4):
    islem[i].place(x = 290,y=80 + 60*i)


sifirbutonu = Button(text=0,font="verdana 25 bold",command=lambda x=0:yaz(x))
sifirbutonu.place(x=40,y=310)

noktabutonu = Button(text=".",font="verdana 25 bold",width=2,command=lambda x=".":yaz(x))
noktabutonu.place(x=120,y=310)

esittirbutonu = Button(text="=",fg="ORANGE",font="verdana 25 bold",width=2,command=hesapla)
esittirbutonu.place(x=200,y=310)

clearbutonu = Button(text="C",fg="ORANGE",font="verdana 25 bold",width=2,command=temizle)
clearbutonu.place(x=290,y=310)

sayibutonu = Button(text="🐼",fg="ORANGE",font="verdana 25 bold",width=2,command=lambda x="PANDAMMMM" :yaz(x))
sayibutonu.place(x=380,y=310)

pencere.mainloop()