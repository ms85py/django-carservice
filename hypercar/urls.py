
from django.urls import path
from django.urls import re_path

from tickets.views import WelcomeView
from tickets.views import MenuView
from tickets.views import TicketView
from tickets.views import ProcessingView
from tickets.views import NextTicketView

urlpatterns = [
    path('', MenuView.as_view()),  # added after solving the task
    path('welcome/', WelcomeView.as_view()),
    path('menu/', MenuView.as_view()),
    path('get_ticket/<str:link>', TicketView.as_view()),
    re_path('processing/?', ProcessingView.as_view()),
    re_path('next/?', NextTicketView.as_view())
]
