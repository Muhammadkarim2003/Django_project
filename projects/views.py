from django.shortcuts import render
from django.http import HttpResponse


data = [
    {
        'id' : '1',
        'title': 'Ekonom vewsayt',
        'description': 'Ekonimoka'
    },
    {
        'id' : '2',
        'title': 'Oyin sayt',
        'description': 'Wargame'
    },
    {
        'id' : '3',
        'title': 'Portfoliya vewsayti',
        'description': 'Portfoliyalar'
    }
]


# Create your views here.
def projects(request):
    return render(request, 'projects.html', {'data':data})

def project(request, pk):
    content = None
    for project in data:
        if project['id'] == str(pk):
            content = project
    return render(request, 'project.html', context=content)