from django.urls import path
from .views import quiz_top_view, quiz_chapter_view, quiz_view, result_view


urlpatterns = [
    path('', quiz_top_view, name="quiz_top"),
    path('<int:chapter>/', quiz_chapter_view, name="chapter"),
    path('<int:chapter>/<int:number>/', quiz_view, name="quiz"),
    path('<int:chapter>/<int:number>/result', result_view, name="result"),
]
