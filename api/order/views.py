from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Order
from api.product.models import Product
from .serializers import OrderSerializer


# Add Orders for user
@csrf_exempt
def add(request, uuid):

    if request.method == 'POST':
        user_id = uuid
        product_id = int(request.POST.get("product"))
        product_quantity = int(request.POST.get("quantity"))

        # Get User details
        userModel = get_user_model()
        user = None
        try:
            user = userModel.objects.get(pk=uuid)
        except userModel.DoesNotExist:
            return JsonResponse({"Error": "User does not exists"})

        # Get Product details
        try:
            product = Product.objects.get(id=product_id)
            if product.stock >= product_quantity and product.is_active:
                product.stock -= product_quantity
                total_price = int(product_quantity) * int(product.price)
                order = Order(user=user, product_id=product,
                              total_products=product_quantity, total_amount=total_price)
                product.save()
                order.save()
                return JsonResponse({"Info": "Success, Order Placed successfully....", "transaction_id": order.transaction_id, "product": product.name, "quantity": order.total_products, "total_amount": order.total_amount})
            else:
                return JsonResponse({"Error": "Apologies, We are running out of stock"})
        except Exception as e:
            return JsonResponse({"Error": "Sorry, This product is not in store!!!"})


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
