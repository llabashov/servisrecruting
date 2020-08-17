from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from .models import Recrut, Sith, Planet, Test_of_shadow_hand

def startpage(request):
    return render(request, 'servisrecruting/startpage.html')

def for_siths(request):
    return render(request, 'servisrecruting/for_siths.html')

#***MISTAKE***
def index_siths(request):
    for_siths = Sith.objects.order_by('sith_Name')
    
    return render(request, 'servisrecruting/for_siths.html', {'for_siths':for_siths})

def detail_siths(request, sith_id):
    try:
        a = sith.objects.get (id = sith_id )
    except:
        raise Http404 ("Ситх не найден!")
    return render(request, 'servisrecruting/detail_siths.html' , {'sith': a})

def recruts_without_shadow_hand(request, recrut_id):
    try:
        a = Recrut.objects.get (id = recrut_id )
    except:
        raise Http404 ("Рекруты без руки тени не найдены!")

    a.recrut_set.create(recrut_Name = request.POST['recrut_Name'], recrut_Age = request.POST['recrut_Age'] )

    return HttpResponseRedirect (reverse('sith:detail', args = (a.id,)) )