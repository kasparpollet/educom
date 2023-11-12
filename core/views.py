from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from core.forms import PersonForm
from core.models import Person

from educom.utils import find_jubileums_of_all_persons

def index(request):

    if request.method =='POST':
        full_name = request.POST['full_name']
        birthdate = request.POST['birthdate']

        Person.objects.create(full_name=full_name, birthdate=birthdate)
        
    persons = Person.objects.all()
    form = PersonForm()

    jubileums = find_jubileums_of_all_persons()

    context = {'persons': persons, 'form': form, 'jubileums': jubileums}

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


def delete_everyone(request):
    Person.objects.all().delete()    
    return redirect('index')
    