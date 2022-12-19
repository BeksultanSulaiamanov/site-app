from django.contrib import admin
from.models import Elektro, Acsessuar, Nout

admin.site.register(Elektro)
admin.site.register(Nout)
admin.site.register(Acsessuar)

# @admin.register(Articles)
# class ArticlesAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'anons', 'date']

