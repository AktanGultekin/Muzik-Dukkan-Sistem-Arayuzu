import sqlite3
from tkinter import *
from tkinter import messagebox

"""" 20202425014 / AKTAN GÜLTEKİN"""

root = Tk()
root.title("Müzik Dükkanı Arayüzü")
root.geometry("400x400")

connection = sqlite3.connect("muzik.db")
cursor = connection.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS muzikshop (
    enstruman_ad TEXT,
    enstruman_marka TEXT,
    enstruman_ucret INTEGER,
    enstruman_stok_adet INTEGER
    )
    """)

#connection.commit()
#connection.close()


def enstrumanEkle():
    appendPage = Tk()
    appendPage.geometry("400x400")
    appendPage.title("Enstrüman Ekleme Sayfası")
    
    def ekleKontrol():
        enstrumanAdi = enstrumanAdiEntry.get()
        enstrumanMarka = enstrumanMarkaEntry.get()
        enstrumanUcret = enstrumanUcretEntry.get()
        enstrumanStokAdet = enstrumanStokAdetEntry.get()
        
        #cursor.execute("SELECT COUNT(*) FROM muzikshop WHERE enstruman_ad = ' " + enstrumanAdi +"'AND enstruman_marka = ' " + enstrumanMarka +"'")
        cursor.execute("SELECT COUNT(*) FROM muzikshop WHERE enstruman_ad LIKE ? AND enstruman_marka LIKE ?",('%'+enstrumanAdi+'%','%'+enstrumanMarka+'%'))
        result = cursor.fetchone()
        print(result)
        
        if(int(result[0])>0):
            messagebox.showerror("Hata","Böyle bir enstrüman bulunmaktadır!")
    
        else:
            cursor.execute("INSERT INTO muzikshop(enstruman_ad, enstruman_marka, enstruman_ucret, enstruman_stok_adet) VALUES(?,?,?,?)",(enstrumanAdi,enstrumanMarka,enstrumanUcret,enstrumanStokAdet))
            connection.commit()
            connection.close()
            messagebox.showinfo("Sonuç","Enstrüman ekleme başarılı!")
        
        
    headerLabel = Label(appendPage,text="Enstrüman Ekle")
    headerLabel.grid(row=0,column=0,pady=10)
    
    enstrumanAdiLabel = Label(appendPage,text="Enstrüman Adı:")
    enstrumanAdiLabel.grid(row=1,column=0)
    
    enstrumanMarkaLabel = Label(appendPage,text="Enstrüman Marka:")
    enstrumanMarkaLabel.grid(row=2,column=0,sticky=W)
    
    enstrumanUcretLabel = Label(appendPage,text="Enstrüman Fiyat:")
    enstrumanUcretLabel.grid(row=3,column=0)
    
    enstrumanStokAdetLabel = Label(appendPage,text="Enstrüman Stok Adeti:")
    enstrumanStokAdetLabel.grid(row=4,column=0)
    
    enstrumanAdiEntry = Entry(appendPage,width=20)
    enstrumanAdiEntry.grid(row=1,column=1)
    
    enstrumanMarkaEntry = Entry(appendPage,width=20)
    enstrumanMarkaEntry.grid(row=2,column=1)
    
    enstrumanUcretEntry = Entry(appendPage,width=20)
    enstrumanUcretEntry.grid(row=3,column=1)
    
    enstrumanStokAdetEntry = Entry(appendPage,width=20)
    enstrumanStokAdetEntry.grid(row=4,column=1)
    
    appendButton = Button(appendPage,text="Ekle",command=ekleKontrol)
    appendButton.grid(row=5,column=1,pady=5,ipadx=10)
    
    appendPage.mainloop()
    
    
def enstrumanCikar():
    popPage = Tk()
    popPage.geometry("400x400")
    popPage.title("Enstrüman Silme Sayfası")
    
    def cikarKontrol():
        enstrumanAdi = enstrumanAdiEntry.get()
        enstrumanMarka = enstrumanMarkaEntry.get()
    
        #cursor.execute("SELECT COUNT(*) FROM muzikshop WHERE enstruman_ad LIKE ? AND enstruman_marka LIKE ?",('%'+enstrumanAdi+'%','%'+enstrumanMarka+'%'))
        #cursor.execute("SELECT COUNT(*) FROM muzikshop WHERE enstruman_ad= ' " + enstrumanAdi + "' AND enstruman_marka= ' " + enstrumanMarka + "'")
        cursor.execute("SELECT COUNT(*) FROM muzikshop WHERE enstruman_ad = ? AND enstruman_marka = ?",(enstrumanAdi,enstrumanMarka))
        saves = cursor.fetchone()
          
        if(int(saves[0])<1):
            messagebox.showerror("Hata","Böyle bir enstrüman bulunamadı!")
        else:
            cursor.execute("DELETE FROM muzikshop WHERE enstruman_ad='"+enstrumanAdi+"' AND enstruman_marka='"+enstrumanMarka+"'")
            connection.commit()
            connection.close()
            messagebox.showinfo("Sonuç","Enstrüman çıkarma başarılı!")
            
    """ if(int(result[0])<0):
            messagebox.showerror("Hata","Böyle bir enstrüman bulunamadı!")
        else:
            #cursor.execute("DELETE FROM muzikshop WHERE enstruman_ad LIKE ? AND enstruman_marka LIKE ?",('%'+enstrumanAdi+'%'+enstrumanMarka+'%'))
            cursor.execute("DELETE FROM muzikshop WHERE enstruman_ad='"+enstrumanAdi+"' AND enstruman_marka='"+enstrumanMarka+"'")
            connection.commit()
            connection.close()
            messagebox.showinfo("Sonuç","Enstrüman çıkarma başarılı!")      """   
    
    
    headerLabel = Label(popPage,text="Enstrüman Çıkar")
    headerLabel.grid(row=0,column=0,pady=10)
    
    enstrumanAdiLabel = Label(popPage,text="Enstrüman Adı:")
    enstrumanAdiLabel.grid(row=1,column=0,pady=5)
    
    enstrumanMarkaLabel = Label(popPage,text="Enstrüman Marka:")
    enstrumanMarkaLabel.grid(row=2,column=0,pady=5,sticky=W)
    
    enstrumanAdiEntry = Entry(popPage,width=20)
    enstrumanAdiEntry.grid(row=1,column=1,pady=5)
    
    enstrumanMarkaEntry = Entry(popPage,width=20)
    enstrumanMarkaEntry.grid(row=2,column=1,pady=5)
    
    popButton = Button(popPage,text="Çıkar",command=cikarKontrol)
    popButton.grid(row=3,column=0,pady=5,ipadx=10,padx=20,sticky=W)
    
    popPage.mainloop()
    
def enstrumanStokGuncelle():
    updatePage = Tk()
    updatePage.geometry("400x400")
    updatePage.title("Enstrüman Stok Adet Güncelleme Sayfası")

    def enstrumanStokKontrol():
        
        enstrumanAdi = enstrumanAdiEntry.get()
        enstrumanMarka = enstrumanMarkaEntry.get()
        enstrumanStokAdet = enstrumanStokAdetEntry.get()    

        cursor.execute("SELECT COUNT(*) FROM muzikshop WHERE enstruman_ad LIKE ? AND enstruman_marka LIKE ?",('%'+enstrumanAdi+'%','%'+enstrumanMarka+'%'))
        result=cursor.fetchone()
        print(result)
        
        if(int(result[0])>0):
            cursor.execute("UPDATE muzikshop SET enstruman_stok_adet = ? WHERE enstruman_ad = ? AND enstruman_marka = ?",(enstrumanStokAdet,enstrumanAdi,enstrumanMarka))
            connection.commit()
            connection.close()
            messagebox.showinfo("Sonuç","Enstrüman stoğu başarıyla güncellenmiştir!")
        else:
            messagebox.showerror("Hata","Böyle bir enstrüman bulunamadı!")
        

    headerLabel = Label(updatePage,text="Enstrüman Stok Adet Güncelle")
    headerLabel.grid(row=0,column=0,pady=10)
    
    enstrumanAdiLabel = Label(updatePage,text="Enstrüman Adı:")
    enstrumanAdiLabel.grid(row=1,column=0,pady=5)

    enstrumanMarkaLabel = Label(updatePage,text="Enstrüman Marka:")
    enstrumanMarkaLabel.grid(row=2,column=0,pady=5,sticky=W)
    
    enstrumanStokAdetLabel = Label(updatePage,text="Enstrüman Stok Adeti:")
    enstrumanStokAdetLabel.grid(row=3,column=0,pady=5)
    
    enstrumanAdiEntry = Entry(updatePage,width=20)
    enstrumanAdiEntry.grid(row=1,column=1,pady=5)
    
    enstrumanMarkaEntry = Entry(updatePage,width=20)
    enstrumanMarkaEntry.grid(row=2,column=1,pady=5)
    
    enstrumanStokAdetEntry = Entry(updatePage,width=20)
    enstrumanStokAdetEntry.grid(row=3,column=1,pady=5)
    
    updateButton = Button(updatePage,text="Güncelle",command=enstrumanStokKontrol)
    updateButton.grid(row=4,column=0,pady=5,ipadx=10,padx=20,sticky=W)
    
    updatePage.mainloop()


rootHeader = Label(root,text="Arayüz İşlem Sayfası")
rootHeader.grid(row=0,column=0)

appendButton = Button(root,text="Enstrüman Ekle",command = enstrumanEkle)
appendButton.grid(row=1,column=0,sticky=W,pady=25,padx=25)

popButton = Button(root,text="Enstrüman Çıkar",command = enstrumanCikar)
popButton.grid(row=1,column=1,sticky=E,pady=25,padx=0)

updateButton = Button(root,text="Enstrüman Stok Adet Belirle",command = enstrumanStokGuncelle)
updateButton.grid(row=3,column=0,sticky=W,pady=25,padx=25)

root.mainloop()
