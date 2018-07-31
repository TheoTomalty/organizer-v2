from django.conf.urls import url
import organizer.views as v


urlpatterns = [url(r'^$', v.TestView.as_view(), name='index')]