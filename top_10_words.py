from shutil import copyfile #dosyayı hedef dosyaya kopyalamak için
import random
import nltk #doğal dil işleme paketi
import os
from nltk.corpus import stopwords #doğal dil işlemede yararsız kelimeler(veriler) durma sözcükleri olarak adlandırılır. işe yaramayan verileri filtreleriz
from collections import Counter #nesneleri saymak için bir alt sınıftır.
import matplotlib.pyplot as plt #bilmediğimiz bir okuyucuya yanlış göndermemek için ipucu gönderririz. #grafik kütüp
import numpy as np #bilimsel işlemler için matematik kütüphanesi

def make_Dictionary(path): #sözlük oluşturduk
    emails = [os.path.join(path,f) for f in os.listdir(path)]
    all_words = []
    for email in emails:
        with open(email, encoding='latin1') as m:
            content = m.read() #mailleri okudu
            all_words += nltk.word_tokenize(content) #boşluk ve noktalama işartelerine göre ayırır
    dictionary = [word for word in all_words if word not in stopwords.words('english')] #
    dictionary = [word.lower() for word in dictionary if word.isalpha()] #lower küçük harfe çevirir, isalpha karakterlerin alfade var olup olmadığını kontrol eder
    dictionary = Counter(dictionary) #sayıcıyla sözlüğü döndürdük.
    dictionary = dictionary.most_common(10) #en yaygın kelimeden en az kelimeye kadar döndürdük kelimelerin içinde 10 kelimenin kaç kere tekrar ettiğini bulduk.
    return dictionary

spam_path = r"C:\Users\Aybilge\Desktop\Proje2_SpamTespiti\spam" #onlarda ham

spam_dict = make_Dictionary(spam_path)
#oluşturacağımız grafik için apsisine x   ordinatına y dedik
x = []
y = []
my_xticks = []
width = 1/1.5

for i in range(len(spam_dict)): #sözlükteki kelimelerin uzunluğu kadar döndürdük
    x.append(i) #x eksenine belirlenen kelimeleri yazdırdık
    y.append(spam_dict[i][1]) #kelimeleri arttırarak yerleştirir.
    my_xticks.append(spam_dict[i][0])#kelimeleri yerlerine yerleştirdik
#grafik gösterme ve özellikleri için;
plt.xticks(x, my_xticks)
plt.bar(x, y, width, color="purple")
plt.show()
