from django.urls import path
from . import views

app_name = 'choose'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.detail, name='detail'),
    path('create', views.create, name='create'),
    path('random', views.myRandom, name='random'),
    path('<int:question_id>/comment/<int:id>/reply', views.reply, name='reply'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/comment/', views.comment_create, name='comment_create'),
    path('<int:id>/comment/<int:comment_id>/delete', views.comment_delete, name='comment_delete'),

]