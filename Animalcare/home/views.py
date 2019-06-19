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
    event_campaign=Event.objects.all().filter(type="campaign")
    event_concerts=Event.objects.all().filter(type="concert")
    event_films=Event.objects.all().filter(type="film")
    event_ecoproject=Event.objects.all().filter(type="ecoproject")
    home = Home.objects.get(language=language)
    context = {
        'menu': menu,
        'campaign':event_campaign,
        'concert': event_concerts,
        'film': event_films,
        'ecopro': event_ecoproject,
        'langs': langs,
        'home': home,
        'language': language,

    }
    return render(request, "event.html", context)


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
        'report':Report.objects.all().filter(event=event),
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
        'event_details':event.details_in_eng,
        'home_logo':home.logo,
        'address':event.event_address,
        'city':event.event_city,
        'language': language,


    }
    return render(request, "event-details.html", context)


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


        'donor_review': donor_review,
    }
    return render(request, 'index.html', context)



def events_aze(request):
    langs = Languages.objects.all()
    language = Languages.objects.get(language_name="Azerbaijani")

    menu = Menu.objects.get(language=language)
    event_campaign=Event.objects.all().filter(type="campaign")
    event_concerts=Event.objects.all().filter(type="concert")
    event_films=Event.objects.all().filter(type="film")
    event_ecoproject=Event.objects.all().filter(type="ecoproject")
    home = Home.objects.get(language=language)
    context = {

        'menu':menu,
        'menu_contact': menu.contact,
        'campaign':event_campaign,
        'concert': event_concerts,
        'film': event_films,
        'ecopro': event_ecoproject,
        'langs': langs,
        'home': home,
        'language': language,

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
        'event_little_details': event.event_little_detail_in_eng,
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
        'event_details':event.details_in_az,
        'home_logo':home.logo,
        'address':event.event_address,
        'city':event.event_city,
        'language': language,


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
        'testimonial': testimonial,

    }
    return render(request, 'about-us.html', context)


