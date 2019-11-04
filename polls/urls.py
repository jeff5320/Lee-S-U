from django.urls import path
from polls import views


app_name = 'polls'
urlpatterns = [
    path('', views.indexView.as_view(), name='index'),      # /polls/
    path('<int:question_id>/', views.detailview.as_view(), name='detail'),
    path('<int:question_id>/results/', views.resultsview.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]