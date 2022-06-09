import string
import re
import codecs
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import feature_extraction
from sklearn import linear_model
from sklearn import pipeline
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pickle

english_dataset = pd.read_csv('datasets/English.csv', header=None, names=["English"])
spanish_dataset = pd.read_csv('datasets/Spanish.csv', header=None, names=["Spanish"])
french_dataset = pd.read_csv('datasets/French.csv', header=None, names=["French"])
german_dataset = pd.read_csv('datasets/German.csv', header=None, names=["German"])
# print(english_dataset.head(10))
# print(spanish_dataset.head(10))
# print(french_dataset.head(10))
# print(german_dataset.head(10))

# for char in string.punctuation:
#     print(char, end=" ")

translate_table = dict((ord(char), None) for char in string.punctuation)

data_eng = []
lang_eng = []
data_sp = []
lang_sp = []
data_fr = []
lang_fr = []
data_de = []
lang_de = []

for i, line in english_dataset.iterrows():
    line = line['English']
    if len(line) != 0:
        line = line.lower()
        line = re.sub(r"\d+", "", line)
        line = line.translate(translate_table)
        data_eng.append(line)
        lang_eng.append("English")


for i, line in spanish_dataset.iterrows():
    line = line['Spanish']
    if len(line) != 0:
        line = line.lower()
        line = re.sub(r"\d+", "", line)
        line = line.translate(translate_table)
        data_sp.append(line)
        lang_sp.append("Spanish")


for i, line in french_dataset.iterrows():
    line = line['French']
    if len(line) != 0:
        line = line.lower()
        line = re.sub(r"\d+", "", line)
        line = line.translate(translate_table)
        data_fr.append(line)
        lang_fr.append("French")


for i, line in german_dataset.iterrows():
    line = line['German']
    if len(line) != 0:
        line = line.lower()
        line = re.sub(r"\d+", "", line)
        line = line.translate(translate_table)
        data_de.append(line)
        lang_de.append("German")


df = pd.DataFrame({"Text":data_eng+data_sp+data_fr+data_de,"language":lang_eng+lang_sp+lang_fr+lang_de})
X, y = df.iloc[:, 0],df.iloc[:, 1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=0)

# print(X_train.shape)
# print(X_test.shape)
# print(y_train.shape)
# print(y_test.shape)

vectorizer = feature_extraction.text.TfidfVectorizer(ngram_range=(1, 3), analyzer='char')

language_detect_model = pipeline.Pipeline([
    ('vectorizer', vectorizer),
    ('clf', linear_model.LogisticRegression(max_iter=1000000))
])

language_detect_model.fit(X_train, y_train)

y_predicted = language_detect_model.predict(X_test)

acc = (metrics.accuracy_score(y_test, y_predicted))*100
print(acc, '%')
matrix = metrics.confusion_matrix(y_test, y_predicted)
print(matrix)

filename = open('LanguageDetectModel.pckl', 'wb')
pickle.dump(language_detect_model, filename)
filename.close()







