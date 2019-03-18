from django.shortcuts import render,redirect
from .models import Person
from .forms import PersonForms

def list_person(request):
    person = Person.objects.all();
    return render(request, 'person.html', {'person': person})




def add_person(request):

    form = PersonForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_person')

    return render(request, 'person-form.html', {'form': form})



def update_person(request,id):
    person = Person.objects.get(id=id)
    form = PersonForms(request.POST or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('list_person')

    return render(request,'person-form.html', {'form': form, 'person': person})

def delete_person(request,id):
    person = Person.objects.get(id=id)
    if request.method == 'POST':
        person.delete()
        return redirect('list_person')

    return render(request, 'person-delete-form.html', {'person': person})