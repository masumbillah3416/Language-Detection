import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
import string
import re
import pickle
from django.conf import settings

# Create your views here.
def single_check(request):
    if request.method == 'GET' and 'text' in request.GET:
        text = request.GET['text']
    else:
        return HttpResponseBadRequest()

    translate_table = dict((ord(char), None) for char in string.punctuation)

    modelPath = os.path.join(settings.MODEL, 'LanguageDetectModel.pckl')


    global LanguageDetectModel
    LanguageDetectFile = open(modelPath, 'rb')
    LanguageDetectModel = pickle.load(LanguageDetectFile)
    LanguageDetectFile.close()

    text = " ".join(text.split())
    text = text.lower()
    text = re.sub(r"\d+", "", text)
    text = text.translate(translate_table)
    prediction = LanguageDetectModel.predict([text])
    prob = LanguageDetectModel.predict_proba([text])
    print(prob[0])
    return HttpResponse(prediction[0])

