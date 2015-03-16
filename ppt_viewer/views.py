from django.shortcuts import render
from django.http import HttpRequest, Http404
from django.template import RequestContext
from ppt_viewer.models import Section, Thesis, Slide


# Create your views here.
def home(request):
	"""Renders the home page."""
	assert isinstance(request, HttpRequest)
	sections = Section.objects.all().order_by('title')
	thesis = Thesis.objects.all()
	return render(request,
								'ppt_viewer/home.html',
								context_instance = RequestContext(request,
																									{
																										'sections': sections,
																										'thesis': thesis,
																									}))


def presentation(request, thesis_id):
	"""Renders the presentation page."""
	assert isinstance(request, HttpRequest)

	try:
		slides = list(Slide.objects.filter(thesis = thesis_id).order_by('num'))
		thesis = Thesis.objects.filter(pk = thesis_id)
	except Slide.DoesNotExist or Thesis.DoesNotExist:
		raise Http404

	for slide in slides:
		slide.before	= slides[slides.index(slide) - 1].num if slides.index(slide) != 0                else slide.num
		slide.after		= slides[slides.index(slide) + 1].num if slides.index(slide) != len(slides) - 1  else slide.num

	return render(request,
								'ppt_viewer/presentation.html',
								context_instance = RequestContext(request,
																									{
																										'slides': slides,
																										'thesis': thesis.first(),
																									}))

def thesis_list(request, section_id):
	"""Renders the xml list of thesis."""
	assert isinstance(request, HttpRequest)

	try:
		thesis = Thesis.objects.filter(section = section_id).order_by('title')
	except Thesis.DoesNotExist:
		raise Http404

	return render(request,
								'ppt_viewer/thesis_list.html',
								context_instance = RequestContext(request,
																									{
																										'thesis': thesis,
																									}))
