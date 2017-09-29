from django.shortcuts import render


# Create your views here.

#def people_createview(request):
#    form = PeopleCreateForm()
#    if request.method == "POST":
#        form = PeopleCreateForm(request.POST)
#        if form.is_valid():
#            obj = People.objects.create(
#                name = form.cleaned_data.get('name'),
#                lastname = form.cleaned_data.get('lastname'),
#                age = form.cleaned_data.get('age')
#            )
#            return HttpResponseRedirect("/people/")
#        if form.errors:
#            print(form.errors)
#    template_name =
from django.views import generic
from .models import Person
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'people/index.html'
    context_object_name='all_persons'

    def get_queryset(self):
        return  Person.objects.all()

class DetailView(generic.DetailView):
    model = Person
    template_name = 'people/detail.html'

class PersonCreate(CreateView):
    model= Person
    fields=['name','lastname','age']

class PersonUpdate(UpdateView):
    model= Person
    fields=['name','lastname','age']

class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('people:index')

def info(request):
    return(request, 'people/info.html')