from django.shortcuts import render, redirect
from .models import CartItem, Product

def Checkout(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        # Retrieve the cart items for the current user
        cart_items = CartItem.objects.filter(user=request.user)

        # Create a payment record or perform any other necessary actions
        # You can access the individual cart items and perform any required logic
        for cart_item in cart_items:
            product = cart_item.product
            quantity = cart_item.quantity
            total_price = cart_item.total_price()

            # Perform payment-related actions here
            # For example, you can create a payment record in your database
            # using the product, quantity, total price, address, and phone

        # Clear the cart after successful payment
        cart_items.delete()

        # Redirect to a success page or any other desired URL
        return redirect('success-page')

    return render(request, 'checkout.html')
