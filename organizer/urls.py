from django.conf.urls import url
import organizer.views as v


urlpatterns = [url(r'^$', v.Home.as_view(), name='index')]