from django.shortcuts import render, redirect
from .models import Header, Home, HomeSlider, HomeContainer, Footer
from .models import About, AboutContent, AboutPricing, AboutPricingContent, AboutInfo
from .models import Deal, DealContent
from .models import Reservation, ReservationContent, ReservationGet, ReservationPost, ReservationOffer

from .forms import ReservationModelForm

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

def double_content():
    header = Header.objects.all()[0]
    reservation_offer = ReservationOffer.objects.all()[0]
    footer = Footer.objects.all()[0]
    return [header, reservation_offer, footer]

def index(request):
    home = Home.objects.all()[0]
    home_slider = HomeSlider.objects.all()
    home_container = HomeContainer.objects.all()[0]
    deal_content = DealContent.objects.all()
    return render(request, 'main/index.html', context={
        'link':'index',
        'header':double_content()[0],
        'home':home,
        'home_slider':home_slider,
        'home_container':home_container,
        'deal_content':deal_content,
        'reservation_offer':double_content()[1],
        'footer':double_content()[2]
    })

def about(request):
    about_page = About.objects.all()[0]
    about_content = AboutContent.objects.all()
    about_pricing = AboutPricing.objects.all()[0]
    about_pricing_content = AboutPricingContent.objects.all()
    about_info = AboutInfo.objects.all()[0]
    return render(request, 'main/about.html', context={
        'link':'about',
        'header':double_content()[0],
        'about_page':about_page,
        'about_content':about_content,
        'about_pricing':about_pricing,
        'about_pricing_content':about_pricing_content,
        'about_info':about_info,
        'reservation_offer':double_content()[1],
        'footer':double_content()[2]
    })

def deals(request):
    deal = Deal.objects.all()[0]
    deal_content = DealContent.objects.all()
    page = request.GET.get('page')
    num_of_items = 4
    paginator = Paginator(deal_content, num_of_items)

    try:
        deal_content = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        deal_content = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        deal_content = paginator.page(page)
    return render(request, 'main/deals.html', context={
        'link':'deals',
        'header':double_content()[0],
        'deal':deal,
        'deal_content':deal_content,
        'paginator':paginator,
        'reservation_offer':double_content()[1],
        'footer':double_content()[2]
    })

def reservation(request):
    if request.method == 'POST':
        form = ReservationModelForm(request.POST)
        if form.is_valid():
            ReservationPost.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = ReservationModelForm()
    reservation_page = Reservation.objects.all()[0]
    reservation_content = ReservationContent.objects.all()
    reservation_get = ReservationGet.objects.all()[0]
    deal_content = DealContent.objects.all()
    return render(request, 'main/reservation.html', context={
        'link':'reservation',
        'header':double_content()[0],
        'reservation_page':reservation_page,
        'reservation_content':reservation_content,
        'reservation_get':reservation_get,
        'deal_content':deal_content,
        'footer':double_content()[2]
    })