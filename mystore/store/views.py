
from .models import product
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .category import Category

from .customer import customer


# # Create your views here.


def home(request):
    products = product.objects.all()
    categories = Category.objects.all()
    category_ID = request.GET.get('category')
    if category_ID:
        products = product.get_category_id(category_ID)
    else:
        products = product.objects.all()

    data = {'products': products, 'categories': categories}
    return render(request, 'index.html', data)


def signup(request):
    if request.method == 'GET':
        return render(request, "signup.html")
    else:
        fn = request.POST['fn']
        ln = request.POST['ln']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        error_masg = None
        success_msg = None

        uservalues = {
            'fn': fn,
            'ln': ln,
            'email': email,
            'mobile': mobile
        }

        # Validate inputs
        if not fn:
            error_masg = "First name cannot be empty"
        elif not ln:
            error_masg = "Last name cannot be empty"
        elif not email:
            error_masg = "Email cannot be empty"
        elif not mobile:
            error_masg = "Mobile number cannot be empty"
        elif not password:
            error_masg = "Password cannot be empty"
        elif customer.objects.filter(email=email).exists():
            error_masg = "Email already exists"

        if not error_masg:
            # Hash the password
            password = make_password(password)

            # Save the customer data
            customerdata = customer(
                first_name=fn, last_name=ln, email=email, mobile=mobile, password=password)
            customerdata.save()
            success_msg = "Account created successfully"
            return render(request, 'signup.html', {'success': success_msg})
        else:
            msg = {'error': error_masg, 'values': uservalues}
            return render(request, 'signup.html', msg)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST['email']
        password = request.POST['password']
        error_msg = None

        user = customer.getmail(email)
        if user:
            if check_password(password, user.password):
                return redirect('/')
            else:
                error_msg = "Password is incorrect"
        else:
            error_msg = "Email is incorrect"

        return render(request, 'login.html', {'error': error_msg})




# # testing cart 
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required


# @login_required
# def add_to_cart(request, product_id):
#     product = get_object_or_404(product, id=product_id)
#     cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)

#     if not created:
#         cart_item.quantity += 1
#     else:
#         cart_item.quantity = 1

#     cart_item.save()

#     return redirect('cart')

# @login_required
# def cart(request):
#     cart_items = CartItem.objects.filter(user=request.user)
#     cart_items_with_totals = []
#     total_price = 0

#     for item in cart_items:
#         item_total = item.product.price * item.quantity
#         cart_items_with_totals.append({
#             'item': item,
#             'total': item_total,
#         })
#         total_price += item_total

#     return render(request, 'cart.html', {'cart_items_with_totals': cart_items_with_totals, 'total_price': total_price})

# @login_required
# def remove_from_cart(request, item_id):
#     cart_item = CartItem.objects.get(id=item_id)
#     cart_item.delete()
#     return redirect('cart')
 












# def cart(request):
#     cart_items = CartItem.objects.filter(user=request.user)
#     cart_items_with_totals = []
#     total_price = 0

#     for item in cart_items:
#         item_total = item.product.price * item.quantity
#         cart_items_with_totals.append({
#             'item': item,
#             'total': item_total,
#         })
#         total_price += item_total

#     return render(request, 'cart.html', {'cart_items_with_totals': cart_items_with_totals, 'total_price': total_price})


# def add_to_cart(request, product_id):
#     product_item = get_object_or_404(product, id=product_id)
#     cart_item, created = CartItem.objects.get_or_create(
#         product=product_item, user=request.user)

#     # Increment quantity by 1 when adding to cart
#     if not created:
#         cart_item.quantity += 1
#     else:
#         cart_item.quantity = 1  # Set quantity to 1 for newly created item

#     cart_item.save()

#     return redirect('cart')


# def remove_from_cart(request, item_id):
#     cart_item = CartItem.objects.get(id=item_id)
#     cart_item.delete()
#     return redirect('cart')

