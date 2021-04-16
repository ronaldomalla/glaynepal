from django.contrib import admin
from . models import Contact,Products,Dealership,glay_gallery

# Register your models here.
admin.site.register(Contact),
admin.site.register(Products),
admin.site.register(Dealership),
admin.site.register(glay_gallery)


