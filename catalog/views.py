from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from catalog.forms import ProductForm
from catalog.models import Product, Contact
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def home(request):
    search_query = request.GET.get('q', '')
    if search_query:
        products_list = Product.objects.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    else:
        products_list = Product.objects.all()

    context = {
        'products_list': products_list,
        'search_query': search_query,
    }
    print(f"Query: {search_query}")
    print(f"Products: {products_list}")
    return render(request, 'home.html', context)


def product_info(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_info.html", context)


def contacts(request):
    contacts_data = Contact.objects.all()
    latest_products = Product.objects.all().order_by("-created_at")[:5]

    if request.method == 'POST':
        name = request.POST.get('name')
        telephone = request.POST.get('phone')
        message = request.POST.get('message')

        return HttpResponse(f"Спасибо {name} за отзыв! Ваше сообщение получено")

    return render(
        request,
        "contacts.html",
        {"contacts": contacts_data, "latest_products": latest_products},
    )


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:home')
        else:
            print(form.errors)  # Выведет ошибки формы в консоль
    else:
        form = ProductForm()

    return render(request, "add_product.html", {'form': form})

@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('catalog:home')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})
