from django.utils import timezone

from .models import RideRequest


def process_active_ride_request():
    try:
        active_rides = RideRequest.objects.filter(is_alive=True)
        for ride in active_rides:
            if ride.expiry_time >= timezone.now():
                ride.is_alive = False
                ride.save()
                print("Ride", ride.id, 'Deactivated')
    except Exception as e:
        print("CRON JOB RIDE REQUEST EXCEPTION", e)