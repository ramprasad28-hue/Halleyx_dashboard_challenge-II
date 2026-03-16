import csv
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
from django.shortcuts import redirect
from django.http import JsonResponse
from .models import CustomerOrder

from datetime import timedelta
from django.utils import timezone


from django.shortcuts import render
from .models import CustomerOrder


@api_view(['GET'])
def order_list(request):
    orders = CustomerOrder.objects.all()
    serializer = CustomerOrderSerializer(orders, many=True)
    return Response(serializer.data)

from django.views.decorators.csrf import csrf_exempt
import json
from .models import DashboardLayout


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

    range_value=request.GET.get("range","all")

    orders = CustomerOrder.objects.all()
    if range_value=="today":
        orders=orders.filter(created_at__date=timezone.now().date())
    elif range_value=="7":
        orders=orders.filter(created_at__gte=timezone.now()-timedelta(days=7))
    elif range_value=="30":
        orders=orders.filter(created_at__gte=timezone.now()-timedelta(days=30))
    elif range_value=="90":
        orders=orders.filter(created_at__gte=timezone.now()-timedelta(days=90))


    data = (
        orders
        .values('product')
        .annotate(total_revenue=Sum('total_amount'))
        .order_by('-total_revenue')
    )

    return Response(data)



@api_view(['GET'])
def order_status_distribution(request):

    range_value=request.GET.get("range","all")

    orders = CustomerOrder.objects.all()
    if range_value=="today":
        orders=orders.filter(created_at__date=timezone.now().date())
    elif range_value=="7":
        orders=orders.filter(created_at__gte=timezone.now()-timedelta(days=7))
    elif range_value=="30":
        orders=orders.filter(created_at__gte=timezone.now()-timedelta(days=30))
    elif range_value=="90":
        orders=orders.filter(created_at__gte=timezone.now()-timedelta(days=90))


    data = (
        orders
        .values('status')
        .annotate(count=Count('id'))
        .order_by('-count')
    )

    return Response(data)



def dashboard(request):
    return render(request,"dashboard.html")



def upload_orders_csv(request):
    if request.method == "POST":

        csv_file = request.FILES['file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        for row in reader:
            CustomerOrder.objects.create(
                first_name=row['first_name'],
                last_name=row['last_name'],
                email=row['email'],
                phone=row['phone'],
                country=row['country'],
                product=row['product'],
                quantity=int(row['quantity']),
                unit_price=float(row['unit_price']),
                total_amount=float(row['quantity']) * float(row['unit_price']),
                status=row['status']
            )

        if 'admin' in request.META.get('HTTP_REFERER', ''):
            return redirect('/admin/orders/customerorder/')
        return redirect('/orders/')
    return JsonResponse({"error": "Invalid request"}, status=400)

def orders_page(request):

    orders = CustomerOrder.objects.all()

    return render(request,"orders.html",{"orders":orders})


@csrf_exempt
def save_layout(request):

    if request.method == "POST":

        data = json.loads(request.body)

        DashboardLayout.objects.all().delete()

        DashboardLayout.objects.create(layout=data)

        return JsonResponse({"message":"layout saved"})
    

def load_layout(request):

    layout = DashboardLayout.objects.first()

    if layout:
        return JsonResponse(layout.layout, safe=False)

    return JsonResponse([],safe=False)

@api_view(['POST'])
def order_create(request):
    serializer=CustomerOrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=201)
    return Response(serializer.errors,status=400)
@api_view(['PUT','PATCH'])
def order_update(request,pk):
    try:
        order=CustomerOrder.objects.get(pk=pk)
    except CustomerOrder.DoesNotExist:
        return Response({"error":"Not found"},status=404)
    
    serializer=CustomerOrderSerializer(order,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=400)
@api_view(['DELETE'])
def order_delete(request,pk):
    try:
        order=CustomerOrder.objects.get(pk=pk)
    except CustomerOrder.DoesNotExist:
        return Response({"error":"Not found"},status=404)
    
    order.delete()
    return Response({'message':'Deleted'},status=204)
def configure_page(request):
    return render(request,"configure.html")