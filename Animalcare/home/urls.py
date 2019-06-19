from .views import homeinenglish,homeinaze,redirect_to_homeen,event_detail_az,about_us_eng,about_us_az,contac_us_az,event_detail_eng,events_eng,contac_us_eng,events_aze
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
    url(r'^about-us/az/$', about_us_az , name="about_us_az"),
    ################################################
    url(r'^events/en/$', events_eng, name="events_eng"),
    url(r'^events/az/$', events_aze, name="events_az"),
    ################################################
    url(r'^event/(?P<slug>[\w-]+)/en/$', event_detail_eng, name='event_detail_eng'),
    url(r'^event/(?P<slug>[\w-]+)/az/$', event_detail_az, name='event_detail_az'),
    ################################################
    url(r'^contact-us/en/$',contac_us_eng, name="contact_us_eng"),
    url(r'^contact-us/az/$',contac_us_az, name="contact_us_az"),
    # url(r'^payment/', include('payment.urls', namespace="payment"))
]