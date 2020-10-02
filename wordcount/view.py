# from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    return render(req, 'home.html')

def count(req):
    fulltext = req.GET['fulltext']
    words = fulltext.split(' ')
    words_num = len(fulltext.split(' '))
    words_dict = dict()
    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    sorted_words = {k: v for k, v in sorted(words_dict.items(), key=lambda item: item[1], reverse=True)}
    print(sorted_words)

    return render(req, 'count.html', {'word_num': words_num, 'text':fulltext, 'words':sorted_words.items()})

def about(req):
    return render(req, 'about.html')
