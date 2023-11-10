from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from core.forms import PersonForm
from core.models import Person


def index(request):

    if request.method =='POST':
        full_name = request.POST['full_name']
        birthdate = request.POST['birthdate']

        Person.objects.create(full_name=full_name, birthdate=birthdate)
        # form = PersonForm(request.POST)
        # print('test')
        # print(form.is_valid())
        # if form.is_valid():
        #     person = form.save(commit=False)
        #     print(person)
        #     person.save()
        #     return redirect('index')
        
    persons = Person.objects.all()
    form = PersonForm()

    context = {'persons': persons, 'form': form}

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))