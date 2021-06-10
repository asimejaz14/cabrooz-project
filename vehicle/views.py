
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .vehicle_controller import VehicleController

# Create your views here.
class VehicleAPIView(APIView):
    permission_classes = [IsAuthenticated]
    vehicle_controller_object = VehicleController()

    def get(self, request, id=None):
        return self.vehicle_controller_object.get_vehicle_record(request, id)

    def post(self, request):
        return self.vehicle_controller_object.create_vehicle_record(request)

    def patch(self, request, id=None):
        return self.vehicle_controller_object.update_vehicle_record(request, id)

    def delete(self, request):
        return self.vehicle_controller_object.delete_vehicle_record(request)
