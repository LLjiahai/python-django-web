from django.conf.urls import url
from temp_app import views


urlpatterns = {
    url(r'^temp_app$', views.Temp_Home.temp, name='template'),
}
