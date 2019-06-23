from django.contrib import admin
from .models import Menu, Languages, Home, Event,Report, Volunteer,Donor_review,Donor_Details,Animal_need_help,Contacts,Message,Report

class MenuAdmin(admin.ModelAdmin):
    list_display = ['language','home','events','about','rescued','contact']
    list_display_links = ['language']
    # list_filter = ['publishing_date']
    # search_fields = ["title"]

    class Meta:
        model = Menu
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ['language_name','language_short_name']
    list_display_links = ['language_name']
    class Meta:
        model =Languages

class EventAdmin(admin.ModelAdmin):
    list_display = ['title_in_eng','title_in_az', 'date']
    list_display_links = ['title_in_eng','title_in_az']
    search_fields = ['date','title_in_eng','title_in_az','details_in_eng','details_in_az']
	
    class Meta:
        model = Event

class HomeAdmin(admin.ModelAdmin):
    list_display = ['language']
    list_display_links = ['language']

    # list_filter = ['publishing_date']
    # search_fields = ["title"]

    class Meta:
        model = Home

		
class ReportAdmin(admin.ModelAdmin):
	list_display=['donor_name','amount']
	list_display_links = ['donor_name','amount']
	search_fields =  ['donor_name','amount']
	
	class Meta:
		model = Report
	
admin.site.register(Donor_Details)
admin.site.register(Animal_need_help)
admin.site.register(Menu,MenuAdmin)
admin.site.register(Languages,LanguagesAdmin)
admin.site.register(Donor_review)
admin.site.register(Home,HomeAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Volunteer)
admin.site.register(Contacts)
admin.site.register(Message)
admin.site.register(Report,ReportAdmin)
