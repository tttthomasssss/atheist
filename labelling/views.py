from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import ListView, View

from .models import TwitterUser, Labelling, UserLabelling


class SaveLabelsView(View):
	def post(self, request):
		for key in filter(lambda k: True if k.startswith('label') else False, request.POST.keys()):
			user = TwitterUser.objects.get(pk=int(key.split('_')[1]))
			label = Labelling.objects.get(label_group_name='Gender Classification', label=int(request.POST[key]))

			UserLabelling.objects.update_or_create(user=user, label=label)

		return HttpResponse('Geh Scheissen!')


class ImageDescriptionLabellingView(ListView):
	template_name = 'image_description_labelling.html'
	context_object_name = 'users'

	def get_queryset(self):
		return TwitterUser.objects.filter(~Q(description=''), ~Q(description=None), ~Q(description='NULL'), description_length__gt=50, profile_image_width__gt=0, profile_image_height__gt=0, profile_image__contains='.').order_by('?')[:100]

	def get_context_data(self, **kwargs):
		context = super(ImageDescriptionLabellingView, self).get_context_data(**kwargs)
		context['labelling'] = Labelling.objects.filter(label_group_name='Gender Classification').order_by('label')
		return context