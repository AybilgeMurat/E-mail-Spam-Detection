import os
import numpy as np
import nltk
from nltk.corpus import stopwords
from collections import Counter
from sklearn.model_selection import train_test_split #Veri kümesini ikiye bölmek için kullanıyoruz.
from sklearn.naive_bayes import MultinomialNB #çok terimli modeller için  sınıflandırıcı
from sklearn.metrics import confusion_matrix  #Bir sınıflamanın doğruluğunu değerlendirmek için karışıklık matrisini hesaplar.
from sklearn.svm import LinearSVC #Doğrusal Destek Vektör Sınıflandırması.
import warnings
from sklearn.exceptions import ConvergenceWarning #yakınsama hatasını görmemek için import ettim
def make_Dictionary(path): #3000 kelimenin seçildiği bir sözlük oluşturduğumuz fonk.
    emails = [os.path.join(path,f) for f in os.listdir(path)]  #burası mail kadar listeye bağlantıları döndürmeye yarar ve f döndüreceği sayı demek
    all_words = [] #tüm kelimeler için bir liste oluşturduk
    for email in emails:  #email kadar mail döngüsüne soktuk
        with open(email, encoding='latin1') as m:
            content = m.read() #mailleri okudu
            all_words += nltk.word_tokenize(content)  #boşluk ve noktalama işartelerine göre ayırır
    dictionary = [word for word in all_words if word not in stopwords.words('english')]
    dictionary = [word.lower() for word in dictionary if word.isalpha()] #lower küçük harfe çevirir, isalpha karakterlerin alfade var olup olmadığını kontrol eder
    dictionary = Counter(dictionary)  #sayıcıyla sözlüğü döndürdük.
    dictionary = dictionary.most_common(3000) #en yaygın kelimeden en az kelimeye kadar döndürdük kelimelerin içinde 3000 kelimenin kaç kere tekrar ettiğini bulduk
    return dictionary
warnings.filterwarnings("ignore", category=DeprecationWarning) #önleyecği hatanın gözükeceği yer
def extract_features_train(path):
    docID = 0
    features_matrix = np.zeros((23594,3000)) #belirtilen değerler kadar 0lardan oluşan bir matris oluşturur.
    labels = np.zeros(23594) #[23594 tane yanyana 0 değerli matris]
    emails = [os.path.join(path,f) for f in os.listdir(path)]
    for mail in emails:
        with open(mail, encoding="latin1") as m:
            all_words = []
            for line in m: #içerik kadar satır döndürüyoruz
                words = line.split() #satırları bölüp kelimeleri bulduk
                all_words += words #kelimeleri all_words listesine ekledik
            for word in all_words: #listedeki kelimeleri döndürüyoruz
                wordID = 0
                for i,d in enumerate(dicti): #i arttırma d öğeyi yakalama Enumerate yinelenebilir öğeye bir sayaç ekler ve bunu bir numaralandırma nesnesi biçiminde döndürür.
                    if d[0] == word: #yakalanan öğe kelimeyse
                        wordID = i
                        features_matrix[docID,wordID] = all_words.count(word) #dosya, kelime matrisini listedeki saydığımız kelimelerle eşitledik.
        labels[docID] = int(mail.split(".")[-2] == 'spam') #?
        docID = docID + 1 #her döngüde +1
    return features_matrix,labels
warnings.filterwarnings("ignore", category=ConvergenceWarning)
def extract_features_test(test_dir):
    docID = 0
    features_matrix = np.zeros((10110,3000))
    labels = np.zeros(10110)
    emails = [os.path.join(test_dir,f) for f in os.listdir(test_dir)]
    for mail in emails:
        with open(mail, encoding="latin1") as m:
            all_words = []
            for line in m:
                words = line.split()
                all_words += words
            for word in all_words:
                wordID = 0
                for i,d in enumerate(dicti):
                    if d[0] == word:
                        wordID = i
                        features_matrix[docID,wordID] = all_words.count(word)
        labels[docID] = int(mail.split(".")[-2] == 'spam')
        docID = docID + 1
    return features_matrix,labels

path = r'C:\Users\Aybilge\Desktop\Proje2_SpamTespiti/trainenron/'
dicti = make_Dictionary(path)

train_matrix,train_labels = extract_features_train(path)

model1 = MultinomialNB()
model2 = LinearSVC()
model1.fit(train_matrix,train_labels) #öğrenme işlemi fit fonksiyonuyla
model2.fit(train_matrix,train_labels)

test_dir = r'C:\Users\Aybilge\Desktop\Proje2_SpamTespiti/testenron/'
test_matrix,test_labels = extract_features_test(test_dir)

result1 = model1.predict(test_matrix) #tahmin edilen etiket bilgisi predict
result2 = model2.predict(test_matrix)
print(confusion_matrix(test_labels,result1))
print(confusion_matrix(test_labels,result2))