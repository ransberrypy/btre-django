from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choice,bedroom_choices,state_choices
# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings':listings,
        'state_choices':state_choices,
        "bedroom_choices":bedroom_choices,
        'price_choice':price_choice
    }
    return render(request,'index.html',context)


def about(request):
    realtors = Realtor.objects.order_by('-hired_date')

    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context={
        'realtors':realtors,
        'mvp_realtors':mvp_realtors
    }
    return render(request,'about.html',context)