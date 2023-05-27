from django.db import models

# Create your models here.

class Header(models.Model):

    img = models.ImageField('Image', upload_to='images')
    path1 = models.CharField('Path 1', max_length=50)
    path2 = models.CharField('Path 2', max_length=50)
    path3 = models.CharField('Path 3', max_length=50)
    path4 = models.CharField('Path 4', max_length=50)

    class Meta:

        verbose_name = 'Header'
        verbose_name_plural = 'Header'

class Home(models.Model):

    title = models.CharField('Title', max_length=80)
    btn_name1 = models.CharField('Button Name 1', max_length=40)
    subtitle1 = models.CharField('Subtitle 1', max_length=60)
    subtitle2 = models.CharField('Subtitle 2', max_length=60)
    subtitle3 = models.CharField('Subtitle 3', max_length=60)
    btn_name2 = models.CharField('Button Name 2', max_length=40)
    general_title = models.CharField('Page Title', max_length=50)

    class Meta:

        verbose_name = 'Home'
        verbose_name_plural = 'Home'

class HomeSlider(models.Model):

    img = models.ImageField('Background Image', upload_to='images')
    name = models.CharField('Country Name', max_length=50)
    info1 = models.CharField('Info 1', max_length=50)
    info2 = models.CharField('Info 2', max_length=50)
    info3 = models.CharField('Info 3', max_length=50)
    class_id = models.PositiveIntegerField('Dont Change This')

    class Meta:

        verbose_name = 'Home Slider'
        verbose_name_plural = 'Home Slider'

class HomeContainer(models.Model):

    title = models.CharField('Title', max_length=60)
    text = models.TextField('Text')
    btn_name = models.CharField('Button Name', max_length=40)
    link_name = models.CharField('Link Name', max_length=50)
    google_map = models.TextField('Google Map')

    
class About(models.Model):

    general_title = models.CharField('Page Title', max_length=50)
    img = models.ImageField('Background Image', upload_to='images')
    title1 = models.CharField('Title 1', max_length=50)
    subtitle = models.CharField('Subtitle', max_length=60)
    text = models.TextField('Text')
    btn_name = models.CharField('Button Name', max_length=40)
    title2 = models.CharField('Title 2', max_length=50)
    title2_colored = models.CharField('Title 2 Colored', max_length=50)

    class Meta:

        verbose_name = 'About'
        verbose_name_plural = 'About'

class AboutContent(models.Model):

    img = models.ImageField('Image', upload_to='images')
    name = models.CharField('Name', max_length=50)

class AboutPricing(models.Model):

    title = models.CharField('Title', max_length=50)
    text = models.TextField('Text')
    offer = models.CharField('Offer', max_length=50)
    btn_name = models.CharField('Button Name', max_length=40)

    class Meta:

        verbose_name = 'About Pricing'
        verbose_name_plural = 'About Pricing'

class AboutPricingContent(models.Model):

    img = models.ImageField('Image', upload_to='images')
    title = models.CharField('Title', max_length=50)
    people = models.CharField('People', max_length=50)
    price = models.PositiveIntegerField('Price')
    count = models.CharField('Person Count', max_length=30)
    offer1 = models.CharField('Offer 1', max_length=60)
    offer2 = models.CharField('Offer 2', max_length=60)
    offer3 = models.CharField('Offer 3', max_length=60)

class AboutInfo(models.Model):

    img = models.ImageField('Image', upload_to='images')
    title = models.CharField('Title', max_length=50)
    text1 = models.TextField('Text 1')
    subtitle1 = models.CharField('Subtitle 1', max_length=60)
    info1 = models.CharField('Info 1', max_length=30)
    subtitle2 = models.CharField('Subtitle 2', max_length=60)
    info2 = models.CharField('Info 2', max_length=30)
    subtitle3 = models.CharField('Subtitle 3', max_length=60)
    info3 = models.CharField('Info 3', max_length=30)
    subtitle4 = models.CharField('Subtitle 4', max_length=60)
    info4 = models.CharField('Info 4', max_length=30)
    text2 = models.TextField('Text 2')
    btn_name = models.CharField('Button Name', max_length=40)

class Deal(models.Model):

    img = models.ImageField('Background Image', upload_to='images')
    title1 = models.CharField('Title 1', max_length=60)
    subtitle = models.CharField('Subtitle', max_length=80)
    btn_name1 = models.CharField('Button Name 1', max_length=40)
    title2 = models.CharField('Title 2', max_length=60)
    text = models.TextField('Text')
    daily = models.CharField('Daily', max_length=50)
    btn_name2 = models.CharField('Button Name 2', max_length=40)
    general_title = models.CharField('Page Title', max_length=50)

class DealContent(models.Model):

    img = models.ImageField('Image', upload_to='images')
    country = models.CharField('Country', max_length=60)
    place = models.CharField('Place', max_length=60)
    text = models.TextField('Text')
    people = models.CharField('People', max_length=30)
    area = models.CharField('Area', max_length=30)
    money = models.CharField('Money', max_length=25)
    title = models.CharField('Title', max_length=60)
    days = models.CharField('Days', max_length=20)
    to_check = models.BooleanField('To Check', blank=True)

    def __str__(self) -> str:
        return self.country

class Reservation(models.Model):

    general_title = models.CharField('Page Title', max_length=50)
    img = models.ImageField('Background Image', upload_to='images')
    title = models.CharField('Title', max_length=50)
    subtitle = models.CharField('Subtitle', max_length=60)
    text = models.TextField('Text')
    btn_name = models.CharField('Button Name', max_length=40)
    
    class Meta:

        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservation'

class ReservationContent(models.Model):

    title = models.CharField('Title', max_length=50)
    info = models.CharField('Info 1', max_length=60)

class ReservationGet(models.Model):

    google_map = models.TextField('Google Map')
    title = models.CharField('Title', max_length=50)
    colored_title = models.CharField('Colored Title', max_length=50)
    placeholder1 = models.CharField('Placeholder 1', max_length=50)
    placeholder2 = models.CharField('Placeholder 2', max_length=50)
    placeholder3 = models.CharField('Placeholder 3', max_length=50)
    placeholder4 = models.CharField('Placeholder 4', max_length=50)
    placeholder5 = models.CharField('Placeholder 5', max_length=50)
    btn_name = models.CharField('Button Name', max_length=40)

    class Meta:

        verbose_name = 'Reservation GET'
        verbose_name_plural = 'Reservation GET'

class ReservationPost(models.Model):

    user_name = models.CharField('Username', max_length=50)
    user_phone = models.CharField('User Phone Number', max_length=50)
    user_count = models.CharField('User Count', max_length=10)
    user_date = models.CharField('User Date', max_length=10)
    user_destination = models.CharField('User Destination', max_length=50)

    class Meta:

        verbose_name = 'Reservation POST'
        verbose_name_plural = 'Reservation POST'

    def __str__(self) -> str:
        return self.user_name
    
class ReservationOffer(models.Model):

    img = models.ImageField('Background Image', upload_to='images')
    title = models.CharField('Title', max_length=50)
    subtitle = models.CharField('Subtitle', max_length=80)
    btn_name = models.CharField('Button Name', max_length=40)

class Footer(models.Model):

    copyright1 = models.CharField('Copyright', max_length=150)
    name = models.CharField('Name', max_length=50)
    name_link = models.URLField('Name Link')

    class Meta:

        verbose_name = 'Footer'
        verbose_name_plural = 'Footer'