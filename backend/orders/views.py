from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomerOrder
from .serializers import CustomerOrderSerializer
from django.http import HttpResponse

from django.db.models import Sum, Avg, Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomerOrder

from django.db.models import Count

@api_view(['GET'])
def order_list(request):
    orders = CustomerOrder.objects.all()
    serializer = CustomerOrderSerializer(orders, many=True)
    return Response(serializer.data)


def home(request):
    return HttpResponse("Halleyx Dashboard Project Running Successfully")



@api_view(['GET'])
def dashboard_kpi(request):

    total_revenue = CustomerOrder.objects.aggregate(
        Sum('total_amount')
    )['total_amount__sum'] or 0

    total_orders = CustomerOrder.objects.aggregate(
        Count('id')
    )['id__count']

    avg_order_value = CustomerOrder.objects.aggregate(
        Avg('total_amount')
    )['total_amount__avg'] or 0

    data = {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "average_order_value": round(avg_order_value, 2)
    }

    return Response(data)

@api_view(['GET'])
def product_revenue(request):

    data = (
        CustomerOrder.objects
        .values('product')
        .annotate(total_revenue=Sum('total_amount'))
        .order_by('-total_revenue')
    )

    return Response(data)



@api_view(['GET'])
def order_status_distribution(request):

    data = (
        CustomerOrder.objects
        .values('status')
        .annotate(count=Count('id'))
        .order_by('-count')
    )

    return Response(data)