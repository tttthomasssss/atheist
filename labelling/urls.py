__author__ = 'thomas'
from django.conf.urls import patterns, url

from .views import ImageDescriptionLabellingView, SaveLabelsView


urlpatterns = patterns('',
	url(r'^image-description-labelling/', ImageDescriptionLabellingView.as_view(), name='image_description_labelling'),
	url(r'^save-labels/', SaveLabelsView.as_view(), name='save_labels'),
)