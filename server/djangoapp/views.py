from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .populate import initiate
from .models import CarMake, CarModel
from .restapis import get_request, analyze_review_sentiments, post_review, searchcars_request

# Get an instance of a logger
logger = logging.getLogger(__name__)


def get_cars(request):
    count = CarMake.objects.count()
    print(count)
    if count == 0:
        initiate()
    car_models = CarModel.objects.select_related("car_make")
    cars = [
        {"CarModel": car.name, "CarMake": car.car_make.name}
        for car in car_models
    ]
    return JsonResponse({"CarModels": cars})


def get_inventory(request, dealer_id):
    data = request.GET
    if dealer_id:
        if 'year' in data:
            endpoint = "/carsbyyear/" + str(dealer_id) + "/" + data['year']
        elif 'make' in data:
            endpoint = "/carsbymake/" + str(dealer_id) + "/" + data['make']
        elif 'model' in data:
            endpoint = "/carsbymodel/" + str(dealer_id) + "/" + data['model']
        elif 'mileage' in data:
            endpoint = "/carsbymaxmileage/" + str(dealer_id) + "/" + data['mileage']
        elif 'price' in data:
            endpoint = "/carsbyprice/" + str(dealer_id) + "/" + data['price']
        else:
            endpoint = "/cars/" + str(dealer_id)

        cars = searchcars_request(endpoint)
        return JsonResponse({"status": 200, "cars": cars})

    return JsonResponse({"status": 400, "message": "Bad Request"})


# Create a `login_request` view to handle sign-in request
@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data["userName"]
    password = data["password"]

    # Authenticate user
    user = authenticate(username=username, password=password)
    response_data = {"userName": username}

    if user is not None:
        login(request, user)
        response_data["status"] = "Authenticated"

    return JsonResponse(response_data)


# Create a `logout_request` view to handle sign-out request
def logout_request(request):
    return JsonResponse({"userName": ""})


# Create a `registration` view to handle sign-up request
@csrf_exempt
def registration(request):
    data = json.loads(request.body)
    username = data["userName"]
    password = data["password"]
    first_name = data["firstName"]
    last_name = data["lastName"]
    email = data["email"]

    username_exist = User.objects.filter(username=username).exists()

    if not username_exist:
        # Create user
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email,
        )
        login(request, user)
        return JsonResponse({"userName": username, "status": "Authenticated"})

    return JsonResponse({"userName": username, "error": "Already Registered"})


# Update the `get_dealerships` render list of dealerships all by default,
# particular state if state is passed
def get_dealerships(request, state="All"):
    endpoint = "/fetchDealers" if state == "All" else "/fetchDealers/" + state
    dealerships = get_request(endpoint)
    return JsonResponse({"status": 200, "dealers": dealerships})


def get_dealer_details(request, dealer_id):
    if dealer_id:
        endpoint = "/fetchDealer/" + str(dealer_id)
        dealership = get_request(endpoint)
        return JsonResponse({"status": 200, "dealer": dealership})

    return JsonResponse({"status": 400, "message": "Bad Request"})


def get_dealer_reviews(request, dealer_id):
    if dealer_id:
        endpoint = "/fetchReviews/dealer/" + str(dealer_id)
        reviews = get_request(endpoint)

        for review_detail in reviews:
            response = analyze_review_sentiments(review_detail["review"])
            print(response)
            review_detail["sentiment"] = response["sentiment"]

        return JsonResponse({"status": 200, "reviews": reviews})

    return JsonResponse({"status": 400, "message": "Bad Request"})


def add_review(request):
    if not request.user.is_anonymous:
        data = json.loads(request.body)
        try:
            post_review(data)
            return JsonResponse({"status": 200})
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return JsonResponse(
                {"status": 401, "message": "Error in posting review"}
            )

    return JsonResponse({"status": 403, "message": "Unauthorized"})
