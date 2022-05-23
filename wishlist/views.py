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
    """ A view that renders the wishlist contents page """

    products = Wishlist.objects.get(user=request.user)
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               ("You didn't enter any search criteria!"))
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'wishlist': view_wishlist,
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required()
def add_to_wishlist(request, item_id):
    """ Add a specified product to the wishlist """
    
    wishlist = None
    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        pass

    product = get_object_or_404(Product, pk=item_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    if WishlistItem.objects.filter(
        wishlist=wishlist, product=product
    ).exists():
        
        for i in wishlist.products.all():
            print(i)
            
        messages.error(request, f'{product.name} is already in your wishlist')
        return render(request, 'wishlist/wishlist.html', {"wishlist": wishlist})

    else:
        wishlist.products.add(product)
        wishlist.save()
        
        for i in wishlist.products.all():
            print(i)
            
        messages.add_message(request, SUCCESS_NO_BAG,
                             f'{product.name} is added to your wishlist')
        return render(request, 'wishlist/wishlist.html', {"wishlist": wishlist})


@login_required()
def remove_from_wishlist(request, item_id):
    """ Remove a specified product to the favorites """

    product = get_object_or_404(Product, pk=item_id)
    wishlist = Wishlist.objects.get(user=request.user)

    wishlist.products.remove(product)
    messages.add_message(request, SUCCESS_NO_BAG,
                         f'{product.name} is removed from your wishlist')
    return render(request, 'wishlist/wishlist.html')
