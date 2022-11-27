from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from store.models import Customer
from store.models import Collection
from store.models import Order
from store.models import OrderItem

def say_hello(request):

    Customer_with_com = Customer.objects.filter(email__iendswith='.com')

    col_featured = Collection.objects.filter(featured_product_id__isnull=True)

    product_low_inventory = Product.objects.filter(inventory__lt=20)

    order_by1 = Order.objects.filter(customer_id=1)

    item_in_col3 = OrderItem.objects.filter(product__collection_id=3)


    return render(request, 'hello.html', {'name': 'Malo',
                                          'product_with_com': list(Customer_with_com),
                                          'col_featured': list(col_featured),
                                          'product_low_inventory':list(product_low_inventory),
                                          'order_by1':list(order_by1),
                                          'item_in_col3':list(item_in_col3),})
