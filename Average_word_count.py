import os
def word_count(path): #wordcount isimli fonksiyon oluşturduk
    all_words = [] #tüm kelimeler için bir liste oluşturduk
    emails = [os.path.join(path,f) for f in os.listdir(path)] #burası mail kadar listeye bağlantıları döndürmeye yarar ve f döndüreceği sayı demek
    for mail in emails: #email kadar mail döngüsüne soktuk
        with open(mail, encoding="latin1") as m: #mail dosyasını açtık encoding kısmı utf8 için
            for line in m: #m kadar satır döndürecek
                words = line.split() #kelimeleri satırları bölerek buluyoruz
                all_words += words # tüm kelimeler lişstesine bulduğumuz her kelimeyi ekliyoruz
    x = len(all_words) #kelimele listesinin uzunluğunu aldık
    y = len(os.listdir(path)) #listdirdeki yolların uzunluğunu aldık
    avg_wordcount = x/y # kelime listesinin uzlunluğunu yol uzunluğuna böldük
    return avg_wordcount

ham_path = r"C:\Users\Aybilge\Desktop\Proje2_SpamTespiti\ham" #trainlerden ham ve spamları ayıklayıp path yaz
spam_path = r"C:\Users\Aybilge\Desktop\Proje2_SpamTespiti\spam"

ham_wordCount = word_count(ham_path)
print('Ortalama Ham mail sayısı:',ham_wordCount) #ortalama ham mail sayısı

spam_wordCount = word_count(spam_path)
print('Ortalama Spam mail sayısı:',spam_wordCount) #ortalama spam mail sayısı