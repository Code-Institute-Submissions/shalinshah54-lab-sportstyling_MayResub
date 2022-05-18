from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect

from products.models import Product
from wishlist.models import Wishlist, WishlistItem


# Defining a new custome message level
SUCCESS_NO_BAG = 50


# Source: modified from a slack thread, between Joe2308 and ckz8780
@login_required()
def view_wishlist(request):
    """ A view that renders the favorites contents page """

    wishlist = None
    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        pass

    products = Wishlist.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'wishlist/wishlist.html', context=context)


@login_required()
def add_to_wishlist(request, item_id):
    """ Add a specified product to the wishlist """

    product = get_object_or_404(Product, pk=item_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    if WishlistItem.objects.filter(
        wishlist=wishlist, product=product
    ).exists():
        messages.error(request, f'{product.name} is already in your wishlist')
        return render(request, 'wishlist/wishlist.html', context)

    else:
        Wishlist.products.add(product)
        messages.add_message(request, SUCCESS_NO_BAG,
                             f'{product.name} is added to your wishlist')
        return render(request, 'wishlist/wishlist.html', context)


@login_required()
def remove_from_wishlist(request, item_id):
    """ Remove a specified product to the favorites """

    product = get_object_or_404(Product, pk=item_id)
    wishlist = Wishlist.objects.get(user=request.user)

    wishlist.products.remove(product)
    messages.add_message(request, SUCCESS_NO_BAG,
                         f'{product.name} is removed from your wishlist')
    return render(request, 'wishlist/wishlist.html', context)