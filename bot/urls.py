from django.conf.urls import url
from .views import (
    startChat,
    get_answer,
)

urlpatterns = [
    url(r'^$', startChat, name="chat"),
    url(r'^answer/$', get_answer, name="answer"),
]