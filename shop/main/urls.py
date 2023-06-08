# from django.contrib import admin
from django.urls import path
from . import views
from .views import HomePageView, SearchResultsView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register_request, name='register'),
    path('about-us/', views.about, name='about'),
    path('basket/', views.basket, name='basket'),
    path('account/', views.account, name='account'),
    path('news/', views.news, name='news'),
    path('order/', views.order, name='order'),
    path('store/', views.store, name='store'),
    path('home_search/', HomePageView.as_view(), name='home_search'),
    path('search_results', views.SearchResultsView, name='search_results'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
