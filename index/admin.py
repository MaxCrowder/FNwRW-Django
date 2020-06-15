from django.contrib import admin
from . models import Podcast, Donation, Email


admin.site.site_header = 'Flash News with River Waters'
admin.site.index_title = 'Admin'
admin.site.site_title = 'FNwRW'


class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'email', 'date')
    index_title = 'Donations'


class PodcastAdmin(admin.ModelAdmin):
    list_display = ('titleText', 'streamUrl', 'uid')


class EmailAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')


admin.site.register(Podcast, PodcastAdmin)


admin.site.register(Donation, DonationAdmin)


admin.site.register(Email, EmailAdmin)
