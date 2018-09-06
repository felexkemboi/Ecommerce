from django.contrib import admin
from . models import Album,Song

"""
# Register your models here.
from . models import profile

class profileAdmin(admin.ModelAdmin):
	class Meta:
		model = profile

admin.site.register(profile, profileAdmin)"""
admin.site.register(Album)
admin.site.register(Song)