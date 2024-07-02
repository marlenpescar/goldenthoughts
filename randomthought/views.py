from django.shortcuts import render
import random



THOUGHT_LIST = [
    'baba z wozu, koniom lżej',
    'gdzie diabeł nie może, tam babę pośle',
    'jeszcze się taki nie narodził, co by babie we wszystkim dogodził',
]

def ThoughtView(request):
    thought = random.choice(THOUGHT_LIST)
    context = {'thought': thought}
    return render(
        request,
        'thought.html',
        context
    )

