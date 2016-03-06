# -*- coding: utf-8 -*-
from django.shortcuts import redirect

from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import render
from core.models import Question
from django.http import HttpResponse
import json
# Create your views here.

def splash(request):
    return render(request, 'splash.html')

def language(request):
    languages = ['Afrikaans',
        'Azərbaycan dili',
        'Bahasa Indonesia',
        'Bahasa Melayu',
        'Basa Jawa',
        'Bisaya',
        'Bosanski',
        'Brezhoneg',
        'Català',
        'Čeština',
        'Cymraeg',
        'Dansk',
        'Deutsch',
        'Eesti',
        'English (UK)',
        'English (US)',
        'Español',
        'Español (Colombia)',
        'Español (España)',
        'Esperanto',
        'Euskara',
        'Filipino',
        'Føroyskt',
        'Français (Canada)',
        'Français (France)',
        'Frysk',
        'Gaeilge',
        'Galego',
        'Guarani',
        'Hrvatski',
        'Ikinyarwanda',
        'Íslenska',
        'Italiano',
        'Kiswahili',
        'Kurdî (Kurmancî)',
        'Latviešu',
        'Leet Speak',
        'Lietuvių',
        'lingua latina',
        'Magyar',
        'Nederlands',
        'Nederlands (België)',
        'Norsk (bokmål)',
        'Norsk (nynorsk)',
        'O\'zbek',
        'Polski',
        'Português (Brasil)',
        'Português (Portugal)',
        'Română',
        'Shqip',
        'Slovenčina',
        'Slovenščina',
        'Suomi',
        'Svenska',
        'Tiếng Việt',
        'Türkçe',
        'Ελληνικά',
        'Беларуская',
        'Български',
        'Қазақша',
        'Македонски',
        'Монгол',
        'Русский',
        'Српски',
        'Тоҷикӣ',
        'Українська',
        'ქართული',
        'Հայերեն',
        'עברית‏',
        'اردو‏',
        'العربية‏',
        'پښتو‏',
        'فارسی‏',
        'کوردیی ناوەندی‏',
        'नेपाली',
        'मराठी',
        'हिन्दी',
        'অসমীয়া',
        'বাংলা',
        'ਪੰਜਾਬੀ',
        'ગુજરાતી',
        'ଓଡ଼ିଆ',
        'தமிழ்',
        'తెలుగు',
        'ಕನ್ನಡ',
        'മലയാളം',
        'සිංහල',
        'ภาษาไทย',
        # 'မြန်မာဘာသာ',
        'ភាសាខ្មែរ',
        '한국어',
        '中文(台灣)',
        '中文(简体)',
        '中文(香港)',
        '日本語',
        '日本語(関西)'];
    return render(request, 'language.html', {'languages': languages});

def healthpass(request):
    # session_id = request.session.session_key
    #please check if no session saved
    # typeform_url = 'https://api.typeform.com/v0/form/cfeila?key=775e3cdde5d8e7d7c63816b9e0428066cffe31b6&completed=true'
    # import urllib
    # full_data = json.loads(urllib.urlopen(typeform_url).read())['responses']
    # data_id = 0
    # for data in full_data:
    #     if data['hidden']['id'] == session_id and int(data['id']) > data_id:
    #         data_id = int(data['id'])
    #         result = data


    questions = Question.objects.all().values()
    if 'nhs_answer' in request.session:
        answers =  json.loads(request.session['nhs_answer'])
        for question in questions:
            if('nhs_question_'+str(question['id']) in answers):
                question['answer'] = answers['nhs_question_'+str(question['id'])]
            else:
                question['answer']= 'notgiven'

        return render(request, 'healthpass.html', {'questions': questions, 'personal_data': ''})
    else:
        return redirect('question', 1)

def index(request):
    return render(request, 'index.html')


def question(request, question_id):
    question  = Question.objects.get(pk = question_id)
    
    return render(request, 'question.html', {'question': question})

def personal(request):
    session_id = request.session.session_key
    return render(request, 'personal.html', {'session_id': session_id})    

def submitanswer(request):
    data = request.POST
    request.session['nhs_answer'] = json.dumps(data)
    return HttpResponse(request.session.session_key)


def yourhome(request):
    return render(request, 'yourhome.html')    

