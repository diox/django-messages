from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

from django_messages.views import *

urlpatterns = patterns('',
    url(r'^$', redirect_to, {'url': 'inbox/'}, name="messages_index"),
    url(r'^inbox/$', inbox, name='messages_inbox'),
    url(r'^outbox/$', outbox, name='messages_outbox'),
    url(r'^compose/$', compose, name='messages_compose'),
    url(r'^compose/(?P<recipient>[\w.@+-]+)/$', compose, name='messages_compose_to'),
    url(r'^reply/(?P<message_id>[\d]+)/$', reply, name='messages_reply'),
    url(r'^view/(?P<conversation_id>[\d]+)/$', view, name='messages_detail'),
    url(r'^delete$', delete, name='messages_delete'),
    url(r'^undelete$', undelete, name='messages_undelete'),
    url(r'^trash/$', trash, name='messages_trash'),
)
