from django.contrib import admin
from .models import Header, Home, HomeSlider, HomeContainer, Footer
from .models import About, AboutContent, AboutPricing, AboutPricingContent, AboutInfo
from .models import Deal, DealContent
from .models import Reservation, ReservationContent, ReservationGet, ReservationPost, ReservationOffer
# Register your models here.

admin.site.register(Header)
admin.site.register(Home)
admin.site.register(HomeSlider)
admin.site.register(HomeContainer)
admin.site.register(About)
admin.site.register(AboutContent)
admin.site.register(AboutPricing)
admin.site.register(AboutPricingContent)
admin.site.register(AboutInfo)
admin.site.register(Deal)
admin.site.register(DealContent)
admin.site.register(Reservation)
admin.site.register(ReservationContent)
admin.site.register(ReservationGet)
admin.site.register(ReservationPost)
admin.site.register(ReservationOffer)
admin.site.register(Footer)