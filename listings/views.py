from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .models import Listing
from .choices import price_choice,bedroom_choices,state_choices


# Create your views here.
def index(request):
    # listings = Listing.objects.all() #getting all data
    listings = Listing.objects.order_by('-list_date').filter(is_published=True) #ordering by date

    # Pagination
    paginator = Paginator(listings,4)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        "listings":paged_listings
    }
    return render(request,'listings/listings.html',context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    context = {
        'listing':listing
    }
    return render(request,'listings/listing.html',context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

 # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

# price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices':state_choices,
        "bedroom_choices":bedroom_choices,
        'price_choice':price_choice,
        'listings':queryset_list,
        'values': request.GET
    }
    return render(request,'listings/search.html',context)
