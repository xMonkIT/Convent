from django.contrib import admin
from ppt_viewer.models import Section, Slide, Thesis

# Register your models here.

class SlideInline(admin.TabularInline):
	model = Slide
	fields = ['num', 'image']
	ordering = ['num']
	extra = 1


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
	search_fields = ['title']


@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
	fields = ['section', 'title']
	search_fields = ['title']
	inlines = [SlideInline]
	list_display = ('title', 'section')
