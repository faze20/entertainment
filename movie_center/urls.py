from django.urls import path


from .views import (
    HomePageView,
    MovieListView,
    MovieDetailView,
    ContactUsPageView,
    ThankYouPageView,
    ManagerCreateView,
    ManagerUpdateView,
    ManagerDeleteView,
)

#enter path here
urlpatterns = [
    path('' , HomePageView.as_view(), name='home'),
    path('movie/', MovieListView.as_view(), name='movie'),
    path('contact_us/', ContactUsPageView.as_view(), name='contact'),
    path('thank_you/', ThankYouPageView.as_view(), name='thank-you'),
    path('new/', ManagerCreateView.as_view(), name='new_movie'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('<int:pk>/edit/', ManagerUpdateView.as_view(), name='movie_edit'),
    path('<int:pk>/delete/', ManagerDeleteView.as_view(), name='movie_delete'),
]

