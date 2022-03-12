from django.contrib import admin

from users.models import Books, Clothes, Hardware

# Register your models here.
admin.site.register(Clothes)
admin.site.register(Hardware)
admin.site.register(Books)