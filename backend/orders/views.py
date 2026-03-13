from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomerOrder
from .serializers import CustomerOrderSerializer
from django.http import HttpResponse

@api_view(['GET'])
def order_list(request):
    orders = CustomerOrder.objects.all()
    serializer = CustomerOrderSerializer(orders, many=True)
    return Response(serializer.data)


def home(request):
    return HttpResponse("Halleyx Dashboard Project Running Successfully")