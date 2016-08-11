
from django.conf.urls import url
from .views import (main_window)



urlpatterns = [
    url(r'^', main_window, name="main_window"),
#    url(r'^main/', include(GameList.urls, namespace="main")),
]
