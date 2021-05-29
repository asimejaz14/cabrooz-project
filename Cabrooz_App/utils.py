from math import sin, cos, sqrt, atan2, radians
from geopy.distance import geodesic


def create_message(status=None, message=None, data=None):
    if status:
        pass
    elif not status:
        status = 500
    return {"status": status, "message": message, "data": data}


def get_default_param(request, key, default):
    key = request.query_params.get(key, request.data.get(key, default))
    return key or default


#
# def get_distance(first_lat, first_long, second_lat, second_long):
#     """ Returns distance between 2 points with latitude and longitude """
#     r = 6373.0
#
#     lat1 = radians(52.2296756)
#     lon1 = radians(21.0122287)
#     lat2 = radians(52.406374)
#     lon2 = radians(16.9251681)
#
#     dlon = lon2 - lon1
#     dlat = lat2 - lat1
#
#     a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
#     c = 2 * atan2(sqrt(a), sqrt(1 - a))
#
#     distance = r * c
#
#     return distance


def get_distance(first_lat=52.2296756, first_long=21.0122287, second_lat=52.406374, second_long=16.9251681):
    coords_1 = (52.2296756, 21.0122287)
    coords_2 = (52.406374, 16.9251681)

    return geodesic(coords_1, coords_2).meters or 0
