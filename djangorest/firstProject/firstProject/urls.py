"""
URL configuration for firstProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from firstApp import views as first_views
from fbvApp import views as fbv_views
from cbvApp import views as cbv_views
from nsApp import views as ns_views
from rest_framework.routers import DefaultRouter
from flightApp import views as flight_views
from rest_framework.authtoken.views import obtain_auth_token
'''
#? Only for viewSets
router = DefaultRouter()
router.register('students', cbv_views.StudentViewSet, basename='student')
urlpatterns = [
    path("", include(router.urls)),
]
'''
# '''
#? Only for flightApp
router = DefaultRouter()
router.register('flights', flight_views.FlightViewSet, basename='flight')
router.register('passengers', flight_views.PassengerViewSet, basename='passenger')
router.register('reservations', flight_views.ReservationViewSet, basename='reservation')
urlpatterns = [
    path('admin/', admin.site.urls),
    path("flgihtServices/", include(router.urls)),
    path("flgihtServices/findFlights/", flight_views.find_flights),
    path("flgihtServices/bookFlights/", flight_views.save_reservation),
    path("token/", obtain_auth_token, name="token"),
]
# '''


# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("", first_views.employeeView),
#     # path("students", fbv_views.student_list),
#     # path("students/<int:pk>", fbv_views.student_detail),
#     # path("students", cbv_views.StudentList.as_view()),
#     # path("students/<int:pk>", cbv_views.StudentDetail.as_view()),
#     path("authors", ns_views.AuthorListView.as_view()),
#     path("authors/<int:pk>", ns_views.AuthorDetailView.as_view()),
#     path("book", ns_views.BookListView.as_view()),
#     path("book/<int:pk>", ns_views.BookDetailView.as_view()),
# ]
