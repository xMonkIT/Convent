from django.contrib import admin
from ppt_viewer.models import Section, Slide, Thesis

# Register your models here.
admin.site.register(Section)
admin.site.register(Thesis)
admin.site.register(Slide)
