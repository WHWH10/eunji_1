from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^keyboard$', views.keyboardpage),
    url(r'^friend$', views.friendpage),
    #url(r'^keyboard$', views.on_init),
    url(r'^chat_room$', views.chatroompage),
    url(r'^message$', views.messagepage),
]
