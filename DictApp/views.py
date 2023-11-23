from django.shortcuts import render
from PyDictionary import PyDictionary as PyD

# Create your views here.
def index(request):
    return render(request, "index.html")

def word(request):
    search = request.GET.get('search')
    meaning = PyD.meaning(search)
    synonyms = PyD.synonym(search)
    antonyms = PyD.antonym(search)

    

    formatted_meaning = format_meaning(meaning)

    context = {
        'word':search,
        'formatted_meaning': formatted_meaning,
        #'synonyms': synonyms,(Currently not available)
        #'antonyms' : antonyms(Currently not available as well)
    }
    return render(request, 'word.html', context)

def format_meaning(meaning):
    if meaning:
        formatted_meaning = {}
        for part_of_speech, definitions in meaning.items():
            formatted_definitions = "\n\n\n".join([f"-{definition}" for definition in definitions])
            formatted_meaning[part_of_speech] = formatted_definitions
        return formatted_meaning
    else:
        return None
   