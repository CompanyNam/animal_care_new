from .views import homeinenglish,rescued_detail_eng,homeinaze,redirect_to_homeen,rescued_animals_eng,rescued_animals_az,rescued_detail_az,event_detail_az,about_us_eng,about_us_az,contac_us_az,event_detail_eng,events_eng,contac_us_eng,events_aze
from django.conf.urls import url
app_name="animalcare"
urlpatterns = [

    ################################################
    url(r'^$', redirect_to_homeen, name="redirect"),
    url(r'^home$', redirect_to_homeen, name="redirect"),
    ################################################
    url(r'^en/$', homeinenglish, name="homeeng"),
    url(r'^az/$', homeinaze, name="homeaz"),
    ################################################
    url(r'^about-us/en/$', about_us_eng , name="about_us_eng"),
    url(r'^haqqimizda/az/$', about_us_az , name="about_us_az"),
    ################################################
    url(r'^events/en/$', events_eng, name="events_eng"),
    url(r'^tedbirlerimiz/az/$', events_aze, name="events_az"),
    ################################################
    url(r'^event/(?P<slug>[\w-]+)/en/$', event_detail_eng, name='event_detail_eng'),
    url(r'^tedbirlerimiz/(?P<slug>[\w-]+)/az/$', event_detail_az, name='event_detail_az'),
    ################################################
    url(r'^contact-us/en/$',contac_us_eng, name="contact_us_eng"),
    url(r'^bizimle-elaqe/az/$',contac_us_az, name="contact_us_az"),
    # url(r'^payment/', include('payment.urls', namespace="payment"))
    url(r'^rescued/en/$', rescued_animals_eng, name="rescued_eng"),
    url(r'^xilas-etdiklerimiz/az/$', rescued_animals_az, name="rescued_az"),


    url(r'^rescued/(?P<slug>[\w-]+)/en/$', rescued_detail_eng,  name='rescued_detail_eng'),
    url(r'^xilas-etdiklerimiz/(?P<slug>[\w-]+)/az/$', rescued_detail_az, name='rescued_detail_az'),
]