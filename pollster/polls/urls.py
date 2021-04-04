# this is in the polls folder will need to bring into the 
# main one in the pollster folder too 
from django.urls import path
# from "all" import views 
from . import views
#creating name space here
app_name = 'polls'

urlpatterns = [
    # basicaly creating a route here
    # / polls  
    # this points to polls/index.html
    path('', views.index,name='index'),
    #using angle brackets to pass in a paramiter
    path('<int:question_id>/', views.detail, name='detail'),
    #resutls 
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]