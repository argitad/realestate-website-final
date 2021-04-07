from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import SearchForm
from .models import *
from django.core.paginator import Paginator
from django.views.generic import ListView, FormView
from django.db.models import Q


# Create your views here.

def home(request):
    homes = Pronat.objects.all().order_by('id_prones')[::-1]
    test = Testimonials.objects.all()
    qs = Pronat.objects.all()
    searchi_query = request.GET.get('searchi')
    if searchi_query != '' and searchi_query is not None:
        qs = qs.filter(searchi__icontains = searchi_query)

    context = {'homes': homes, 'test': test, 'qs': qs}
    return render(request, 'home.html', context)


def listprona(request):
    homes = Pronat.objects.all()
    pagess = Pronat.objects.all().order_by('id_prones')[::-1]
    paginator = Paginator(pagess, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    propertylist = Pronat.objects.all()
    agjent = Agjent.objects.all()


    context = {'homes': homes, 'propertylist': propertylist, 'agjent': agjent, 'page_obj': page_obj}
    return render(request, 'listprona.html', context)

class CatListView(ListView):
    model = Pronat
    template_name = 'pronat.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'pronas': Pronat.objects.filter(category__name=self.kwargs['category'])
        }
        return content
def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {'category_list': category_list}
    return context



def prona(request, id):
    homes = Pronat.objects.all().order_by('id_prones')[::-1]
    prona = Pronat.objects.all()
    property = Pronat.objects.get(id_prones=id)
    fotopron=ImazheProna.objects.filter(prona_title=property)
    img_pronat = ImazheProna.objects.all()
    agjent = Agjent.objects.all()
    p_tengjashme = Pronat.objects.get(id_prones=id)
    tries = Pronat.objects.filter(tipi=p_tengjashme.tipi).exclude(id_prones=id)[:3]
    context = {'homes': homes, 'property': property, 'img_pronat': img_pronat, 'agjent': agjent, 'fotopron': fotopron, 'prona': prona,
               'tries': tries, 'p_tengjashme': p_tengjashme}
    return render(request, 'prona.html', context)



def About(request):
    return render( request, 'About.html' )


def AgjentPershkrim(request, id):
    agjents = Agjent.objects.all()
    agjent = Agjent.objects.get(agjent_id=id)
    prona_rev = Pronat.objects.filter().order_by('id_prones').reverse()[:3]   #tregon vtm 3 fotot e fundit
    prona = Pronat.objects.all().order_by('id_prones') #tregon gjith pronat e agjentit

    context = {'agjent': agjent, 'agjents': agjents, 'prona': prona, 'prona_rev': prona_rev}
    return render( request, 'AgjentPershkrim.html', context )


# ListaAgjenteve.file
def ListaAgjenteve(request):
    agjents = Agjent.objects.all()
    paginator = Paginator(agjents,8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'agjents': agjents, 'page_obj':page_obj }
    return render( request, 'ListaAgjenteve.html', context )


# Kontakt.file
def Kontakt(request):
    if request.method == 'POST':
        name = request.POST['full_name']
        email = request.POST['email']
        adresa = request.POST['adresa']
        tel = request.POST['telefon']
        sms = request.POST['mesazhi']


        data =  {
            'name': name,
            'email':email,
            'adresa':adresa,
            'tel':tel,
            'sms':sms
        }

        message = '''
        New sms: {}
         '''.format(data['sms'], data['tel'])


        send_mail(
            'Ju i keni derguar nje emeil te faqja e real Estate',
            message,
            email,
            ['erjus.stafa@gmail.com', 'tel'],
            fail_silently=False
        )

        messages.success(request, "Kontrolloni emeilin ju lutem ")




    # cf = ContactForm()
    # context = {'cf': cf}
    return render( request, 'Kontakt.html' )



class SearchResultsView(ListView):
    model = Pronat
    template_name = 'search.html'

    def get_queryset(self):

        query = self.request.GET.get('q')
        listprona = Pronat.objects.filter(Q(vendndodhja__icontains=query))
        return listprona





#
# def search(request):
#
#     searched = request.POST['searched']
#     zs = Pronat.objects.filter(Q(category__name__icontains=searched) & ~Q(vendndodhja__icontains = 'durres'))
#
#     context = {'searched': searched, 'zs':zs}
#     return render(request, 'search.html', context)




def search(request):

    if request.method == "POST":
        searched = request.POST['searched']
        zs = Pronat.objects.filter(kodi_prones__contains=searched)
        return render(request, 'search.html', {'searched': searched, 'zs':zs})
    else:
        return render(request, 'search.html')


def search_results(request):
    q = request.POST['q']
    z = Pronat.objects.filter(Q(category__name__icontains=q) | Q(vendndodhja__icontains=q))
    context = {'q': q, 'z': z}
    return render(request, 'search_results.html', context)




