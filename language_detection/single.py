def language_detect(text):
    import string
    import re
    import pickle
    translate_table = dict((ord(char), None) for char in string.punctuation)

    global LanguageDetectModel
    LanguageDetectFile = open('LanguageDetectModel.pckl', 'rb')
    LanguageDetectModel = pickle.load(LanguageDetectFile)
    LanguageDetectFile.close()

    text = " ".join(text.split())
    text = text.lower()
    text = re.sub(r"\d+", "", text)
    text = text.translate(translate_table)
    prediction = LanguageDetectModel.predict([text])
    prob = LanguageDetectModel.predict_proba([text])
    print(prob[0])
    return prediction[0]


data = language_detect("l'entrepreneuriat est la clé du succès")
print(data)
