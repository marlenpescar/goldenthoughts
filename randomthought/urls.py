from django.urls import path

from randomthought import views

urlpatterns = [
    path('thought/', views.ThoughtView),
    path('thought/<str:data>/', views.ThoughtView),

]