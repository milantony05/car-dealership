from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "djangoapp"

urlpatterns = [
    # Path for registration
    path("register", views.registration, name="registration"),
    # Path for login
    path("login", views.login_user, name="login"),
    # Path for logout
    path("logout", views.logout_request, name="logout"),
    # Path for get cars
    path("get_cars", views.get_cars, name="getcars"),
    # Path for get dealers
    path("get_dealers", views.get_dealerships, name="get_dealers"),
    path(
        "get_dealers/<str:state>",
        views.get_dealerships,
        name="get_dealers_by_state",
    ),
    # Path for dealer details view
    path(
        "dealer/<int:dealer_id>",
        views.get_dealer_details,
        name="dealer_details",
    ),
    # Path for dealer reviews view
    path(
        "reviews/dealer/<int:dealer_id>",
        views.get_dealer_reviews,
        name="dealer_details",
    ),
    # Path for add a review view
    path("add_review", views.add_review, name="add_review"),
    # Path for get inventory
    path(route='get_inventory/<int:dealer_id>', view=views.get_inventory, name='get_inventory'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
