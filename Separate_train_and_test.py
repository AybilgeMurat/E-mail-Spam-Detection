import os
from shutil import copyfile #kaynak dosya içeriğini hedef dosyaya kopyalamak için..
import random
import nltk #doğal dil işleme paketi

abc = ['ham','spam'] #ham ve spam kelimelerinin olduğu liste oluşturduk.
for x in abc: #kelimeleri bulduğu kadar dönecek
    for y in range(6): #6 tane veri seti dosyamız var
        path = r'C:\Users\Aybilge\Desktop\Proje2_SpamTespiti/enron'+str(y+1)+'/'+x+'/' #veri setlerimizin bulunduğu pathle 6 klasörü tek tek döndürüyoruz
        percent_70 = (0.7)*len(os.listdir(path))  #%70ini aldığımız bölüm
        a = []
        for j in range(len(os.listdir(path))): #yolun uzunluğu kadar döndürdük
            a.append(j) #döngüdekileri a listesine ekledik
        b = random.sample(a, int(percent_70)) #a listesine ekleiğimiz benzer verilerin %70ini b parametresine aktardık.
        for i in b:
            copyfile(path+'/'+os.listdir(path)[i], r'C:\Users\Aybilge\Desktop\Proje2_SpamTespiti/trainenron/'+os.listdir(path)[i])
        for v in range(len(os.listdir(path))):
            c = os.listdir(path)[v] #b parametresine aktardığımız verileri test ve train olarak ayırdığımız verinin döndürüldüğü c listesini oluşturduk.
            train_path = r'C:\Users\Aybilge\Desktop\Proje2_SpamTespiti/trainenron/'
            h = os.listdir(train_path)
            if c not in h: #eğer c parametresinin içinde train(eğitilecek) veri kalmadıysa c listesi test verisidir.
                copyfile(path+'/'+c, r'C:\Users\Aybilge\Desktop\Proje2_SpamTespiti/testenron/'+c)