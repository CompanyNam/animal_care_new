from django.shortcuts import render, HttpResponseRedirect,get_object_or_404
from .models import Menu, Home, Donor_review,Languages,Event,Contacts,Message,Report
from .models import Animal_need_help,Volunteer
from django.urls import reverse

# Create your views here.


def redirect_to_homeen(request):
    return HttpResponseRedirect(reverse("animalcare:homeeng"))


def homeinenglish(request):
    langs=Languages.objects.all()
    language = Languages.objects.get(language_name="English")
    menu = Menu.objects.get(language=language)
    home = Home.objects.get(language=language)
    event=Event.objects.all().filter(upcoming=1)

    donor_review = Donor_review.objects.all().filter(language=language)
    animal_need_help = Animal_need_help.objects.all()
    # percentage = (animal_need_help.animal_is_donated/animal_need_help.animal_need_amount)*100
    context = {
        'menu':menu,
        'home':home,
        'langs':langs,
        'language':language,
        'animal_need_help': animal_need_help,
        # 'percentage':percentage,
        'event': event,
        'donor_review': donor_review,
    }
    return render(request, 'index.html', context)


def about_us_eng(request):
    langs = Languages.objects.all()
    language = Languages.objects.get(language_name="English")
    menu = Menu.objects.get(language=language)
    home = Home.objects.get(language=language)
    testimonial = Donor_review.objects.all().filter(language=language)

    about_us="About us"
    write_home="Home"
    context = {

        'menu': menu,
        'home': home,
        'about_us': about_us,
        'write-home': write_home,
        'langs': langs,
        'language':language,
        'testimonial': testimonial,

    }
    return render(request, 'about-us.html', context)


def events_eng(request):
    langs = Languages.objects.all()
    language = Languages.objects.get(language_name="English")

    menu = Menu.objects.get(language=language)
    event_charity_sale=Event.objects.all().filter(type="charity")
    event_concerts=Event.objects.all().filter(type="concert")
    event_films=Event.objects.all().filter(type="film")
    event_ecoproject=Event.objects.all().filter(type="ecoproject")
    home = Home.objects.get(language=language)
    event_feeding = Event.objects.all().filter(type="feeding")
    event_awareness = Event.objects.all().filter(type="awareness")
    context = {
        'menu': menu,
        'charity_sale':event_charity_sale,
        'concert': event_concerts,
        'film': event_films,
        'ecopro': event_ecoproject,
        'langs': langs,
        'feeding':event_feeding,
        'awareness':event_awareness,
        'home': home,
        'language': language,

    }
    return render(request, "event.html", context)


def rescued_animals_eng(request):

    language = Languages.objects.get(language_name="English")

    menu = Menu.objects.get(language=language)
    home = Home.objects.get(language=language)
    rescued = Event.objects.all().filter(type="rescued")
    context = {
        'menu': menu,
        'rescued':rescued,
        'home': home,
        'language': language,

    }
    return render(request, "rescued_animals.html", context)
def event_detail_eng(request,slug):
    language = Languages.objects.get(language_name="English")
    menu = Menu.objects.get(language=language)
    event = get_object_or_404(Event, slug=slug)
    home = Home.objects.get(language=language)

    context = {
        'menu':menu,
        'home':home,
        'event_date': event.date,
        'event_little_details': event.event_little_detail_in_eng,
        'event_title': event.title_in_eng,
        'slug':event.slug,
        'report': Report.objects.all().filter(event=event),
        "event_main_image": event.image_main,
        'event_img_1':event.event_image1,
        'event_img_2': event.event_image2,
        'event_img_3': event.event_image3,
        'event_img_4': event.event_image4,
        'event_img_5': event.event_image5,
        'event_img_6': event.event_image6,
        'event_img_7': event.event_image7,
        'event_img_8': event.event_image8,
        'event_img_9': event.event_image9,
        'event_img_10': event.event_image10,
        'event_img_11': event.event_image11,
        'event_img_12': event.event_image12,
        'event_img_13': event.event_image13,
        'event_img_14': event.event_image14,
        'event_img_15': event.event_image15,
        'event_img_16': event.event_image16,
        'event_img_17': event.event_image17,
        'event_img_18': event.event_image18,
        'event_img_19': event.event_image19,
        'event_img_20': event.event_image20,
        'event_img_21': event.event_image21,
        'event_img_22': event.event_image22,
        'event_img_23': event.event_image23,
        'event_img_24': event.event_image24,
        'event_img_25': event.event_image25,
        'event_img_26': event.event_image26,
        'event_img_27': event.event_image27,
        'event_img_28': event.event_image28,
        'event_img_29': event.event_image29,
        'event_img_30': event.event_image30,
        'event_img_31': event.event_image31,
        'event_img_32': event.event_image32,
        'event_img_33': event.event_image33,
        'event_img_34': event.event_image34,
        'event_img_35': event.event_image35,
        'event_img_36': event.event_image36,
        'event_img_37': event.event_image37,
        'event_img_38': event.event_image38,
        'event_img_39': event.event_image39,
        'event_img_40': event.event_image40,
        'event_details':event.details_in_eng,
        'home_logo':home.logo,
        'address':event.event_address,
        'city':event.event_city,
        'language': language,
		'event_iframe':event.event_iframe,

    }
    return render(request, "event-details.html", context)


def rescued_detail_eng(request,slug):
    language = Languages.objects.get(language_name="English")
    menu = Menu.objects.get(language=language)
    event = get_object_or_404(Event, slug=slug)
    home = Home.objects.get(language=language)

    context = {
        'menu':menu,
        'home':home,
        'rescued_date': event.date,
        'rescued_little_details': event.event_little_detail_in_eng,
        'rescued_title': event.title_in_eng,
        'slug':event.slug,
        'report':Report.objects.all().filter(event=event),
        "rescued_main_image": event.image_main,
        'rescued_img_1':event.event_image1,
        'rescued_img_2': event.event_image2,
        'rescued_img_3': event.event_image3,
        'rescued_img_4': event.event_image4,
        'rescued_img_5': event.event_image5,
        'rescued_img_6': event.event_image6,
        'rescued_img_7': event.event_image7,
        'rescued_img_8': event.event_image8,
        'rescued_img_9': event.event_image9,
        'rescued_img_10': event.event_image10,
        'rescued_img_11': event.event_image11,
        'rescued_img_12': event.event_image12,
        'rescued_img_13': event.event_image13,
        'rescued_img_14': event.event_image14,
        'rescued_img_15': event.event_image15,
        'rescued_img_16': event.event_image16,
        'rescued_img_17': event.event_image17,
        'rescued_img_18': event.event_image18,
        'rescued_img_19': event.event_image19,
        'rescued_img_20': event.event_image20,
        'rescued_img_21': event.event_image21,
        'rescued_img_22': event.event_image22,
        'rescued_img_23': event.event_image23,
        'rescued_img_24': event.event_image24,
        'rescued_img_25': event.event_image25,
        'rescued_img_26': event.event_image26,
        'rescued_img_27': event.event_image27,
        'rescued_img_28': event.event_image28,
        'rescued_img_29': event.event_image29,
        'rescued_img_30': event.event_image30,
        'rescued_img_31': event.event_image31,
        'rescued_img_32': event.event_image32,
        'rescued_img_33': event.event_image33,
        'rescued_img_34': event.event_image34,
        'rescued_img_35': event.event_image35,
        'rescued_img_36': event.event_image36,
        'rescued_img_37': event.event_image37,
        'rescued_img_38': event.event_image38,
        'rescued_img_39': event.event_image39,
        'rescued_img_40': event.event_image40,
        'rescued_details':event.details_in_eng,
        'home_logo':home.logo,
        'address':event.event_address,
        'city':event.event_city,
        'language': language,
		'event_iframe':event.event_iframe,

    }
    return render(request, "rescued-details.html", context)


def contac_us_eng(request):
    langs=Languages.objects.all()
    language = Languages.objects.get(language_name="English")
    menu = Menu.objects.get(language=language)
    home = Home.objects.get(language=language)
    contacts = Contacts.objects.get(language=language)
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')

        subject=request.POST.get('subject')

        message=request.POST.get('message')

        Message.objects.create(message_text=message,email=email,name=name,subject=subject)


    context = {
        'menu':menu,
        'langs':langs,
        'home':home,
        'contact':contacts,
        'language': language,
        'contacts_mail':contacts.mail,
        'contacts_mail_text': contacts.mail_text,
        'contacts_telephone': contacts.telephone_number,
        'contacts_telephone_text': contacts.telephone_number_text,

    }
    return render(request, "contact.html", context)


def volunteer_info():
    language = Languages.objects.all().filter(language_name="English")
    menu = Menu.objects.all().filter(language=language)
    volunteer = Volunteer.all().filter(language=language)
    context = {
        'menu_home': menu.home,
        'menu_gallery': menu.gallery,
        'menu_about': menu.about,
        'menu_events': menu.events,
        'menu_page': menu.events,
        'menu_blog': menu.blog,
        'menu_contact': menu.contact,
        'volunteer': volunteer

    }



###################################################################################
###################################################################################
###################################################################################

def homeinaze(request):
    langs=Languages.objects.all()
    language = Languages.objects.get(language_name="Azerbaijani")
    menu = Menu.objects.get(language=language)
    home = Home.objects.get(language=language)
    event=Event.objects.all().filter(upcoming=1)

    donor_review = Donor_review.objects.all().filter(language=language)
    animal_need_help = Animal_need_help.objects.all()
    # percentage = (animal_need_help.animal_is_donated/animal_need_help.animal_need_amount)*100


    context = {
        'menu':menu,
        'home':home,
        'langs':langs,
        'animal_need_help': animal_need_help,
        # 'percentage':percentage,
        'event': event,
        'language':language,


        'donor_review': donor_review,
    }
    return render(request, 'index.html', context)



def events_aze(request):
    langs = Languages.objects.all()
    language = Languages.objects.get(language_name="Azerbaijani")
    event_charity_sale = Event.objects.all().filter(type="charity")
    event_feeding = Event.objects.all().filter(type="feeding")
    event_awareness = Event.objects.all().filter(type="awareness")
    menu = Menu.objects.get(language=language)

    event_concerts=Event.objects.all().filter(type="concert")
    event_films=Event.objects.all().filter(type="film")
    event_ecoproject=Event.objects.all().filter(type="ecoproject")
    home = Home.objects.get(language=language)
    context = {

        'menu':menu,
        'menu_contact': menu.contact,
        'concert': event_concerts,
        'film': event_films,
        'ecopro': event_ecoproject,
        'langs': langs,
        'home': home,
        'language': language,
        'feeding': event_feeding,
        'awareness': event_awareness,
        'charity_sale':event_charity_sale,


    }
    return render(request, "event.html", context)



def event_detail_az(request,slug):
    language = Languages.objects.get(language_name="Azerbaijani")
    menu = Menu.objects.get(language=language)
    event = get_object_or_404(Event, slug=slug)
    home = Home.objects.get(language=language)

    context = {
        'menu':menu,
        'home':home,
        'event_date': event.date,
        'event_little_details': event.event_little_detail_in_az,
        'event_title': event.title_in_az,
        'slug':event.slug,
        'report': Report.objects.all().filter(event=event),
        "event_main_image": event.image_main,
        'event_img_1':event.event_image1,
        'event_img_2': event.event_image2,
        'event_img_3': event.event_image3,
        'event_img_4': event.event_image4,
        'event_img_5': event.event_image5,
        'event_img_6': event.event_image6,
        'event_img_7': event.event_image7,
        'event_img_8': event.event_image8,
        'event_img_9': event.event_image9,
        'event_img_10': event.event_image10,
        'event_img_11': event.event_image11,
        'event_img_12': event.event_image12,
        'event_img_13': event.event_image13,
        'event_img_14': event.event_image14,
        'event_img_15': event.event_image15,
        'event_img_16': event.event_image16,
        'event_img_17': event.event_image17,
        'event_img_18': event.event_image18,
        'event_img_19': event.event_image19,
        'event_img_20': event.event_image20,
        'event_img_21': event.event_image21,
        'event_img_22': event.event_image22,
        'event_img_23': event.event_image23,
        'event_img_24': event.event_image24,
        'event_img_25': event.event_image25,
        'event_img_26': event.event_image26,
        'event_img_27': event.event_image27,
        'event_img_28': event.event_image28,
        'event_img_29': event.event_image29,
        'event_img_30': event.event_image30,
        'event_img_31': event.event_image31,
        'event_img_32': event.event_image32,
        'event_img_33': event.event_image33,
        'event_img_34': event.event_image34,
        'event_img_35': event.event_image35,
        'event_img_36': event.event_image36,
        'event_img_37': event.event_image37,
        'event_img_38': event.event_image38,
        'event_img_39': event.event_image39,
        'event_img_40': event.event_image40,
        'event_details':event.details_in_az,
        'home_logo':home.logo,
        'address':event.event_address,
        'city':event.event_city,
        'language': language,
		'event_iframe':event.event_iframe,

    }
    return render(request, "event-details.html", context)



def contac_us_az(request):
    language = Languages.objects.get(language_name="Azerbaijani")
    home = Home.objects.get(language=language)
    menu = Menu.objects.get(language=language)
    contacts = Contacts.objects.get(language=language)
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')

        subject=request.POST.get('subject')

        message=request.POST.get('message')

        Message.objects.create(message_text=message,email=email,name=name,subject=subject)


    context = {
        'menu':menu,
        'home':home,
        'contact':contacts,
        'language':language,
        'contacts_mail':contacts.mail,
        'contacts_mail_text': contacts.mail_text,
        'contacts_telephone': contacts.telephone_number,
        'contacts_telephone_text': contacts.telephone_number_text,

    }
    return render(request, "contact.html", context)



def about_us_az(request):
    langs = Languages.objects.all()
    language = Languages.objects.get(language_name="Azerbaijani")
    menu = Menu.objects.get(language=language)
    home = Home.objects.get(language=language)
    testimonial = Donor_review.objects.all().filter(language=language)

    about_us="About us"
    write_home="Home"
    context = {

        'menu': menu,
        'home': home,
        'about_us': about_us,
        'write-home': write_home,
        'langs': langs,
        'language':language,
        'testimonial': testimonial,

    }
    return render(request, 'about-us.html', context)





def rescued_animals_az(request):

    language = Languages.objects.get(language_name="Azerbaijani")

    menu = Menu.objects.get(language=language)
    home = Home.objects.get(language=language)
    rescued = Event.objects.all().filter(type="rescued")
    context = {
        'menu': menu,
        'rescued':rescued,
        'home': home,
        'language': language,

    }
    return render(request, "rescued_animals.html", context)



def rescued_detail_az(request,slug):
    language = Languages.objects.get(language_name="Azerbaijani")
    menu = Menu.objects.get(language=language)
    event = get_object_or_404(Event, slug=slug)
    home = Home.objects.get(language=language)

    context = {
        'menu':menu,
        'home':home,
        'rescued_date': event.date,
        'rescued_little_details': event.event_little_detail_in_az,
        'rescued_title': event.title_in_az,
        'slug':event.slug,
        'report':Report.objects.all().filter(event=event),
        "rescued_main_image": event.image_main,
        'rescued_img_1':event.event_image1,
        'rescued_img_2': event.event_image2,
        'rescued_img_3': event.event_image3,
        'rescued_img_4': event.event_image4,
        'rescued_img_5': event.event_image5,
        'rescued_img_6': event.event_image6,
        'rescued_img_7': event.event_image7,
        'rescued_img_8': event.event_image8,
        'rescued_img_9': event.event_image9,
        'rescued_img_10': event.event_image10,
        'rescued_img_11': event.event_image11,
        'rescued_img_12': event.event_image12,
        'rescued_img_13': event.event_image13,
        'rescued_img_14': event.event_image14,
        'rescued_img_15': event.event_image15,
        'rescued_img_16': event.event_image16,
        'rescued_img_17': event.event_image17,
        'rescued_img_18': event.event_image18,
        'rescued_img_19': event.event_image19,
        'rescued_img_20': event.event_image20,
        'rescued_img_21': event.event_image21,
        'rescued_img_22': event.event_image22,
        'rescued_img_23': event.event_image23,
        'rescued_img_24': event.event_image24,
        'rescued_img_25': event.event_image25,
        'rescued_img_26': event.event_image26,
        'rescued_img_27': event.event_image27,
        'rescued_img_28': event.event_image28,
        'rescued_img_29': event.event_image29,
        'rescued_img_30': event.event_image30,
        'rescued_img_31': event.event_image31,
        'rescued_img_32': event.event_image32,
        'rescued_img_33': event.event_image33,
        'rescued_img_34': event.event_image34,
        'rescued_img_35': event.event_image35,
        'rescued_img_36': event.event_image36,
        'rescued_img_37': event.event_image37,
        'rescued_img_38': event.event_image38,
        'rescued_img_39': event.event_image39,
        'rescued_img_40': event.event_image40,
        'rescued_details':event.details_in_eng,
        'home_logo':home.logo,
        'address':event.event_address,
        'city':event.event_city,
        'language': language,


    }
    return render(request, "rescued-details.html", context)

