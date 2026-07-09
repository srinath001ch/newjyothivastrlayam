from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Saree, Category, ContactMessage
from .forms import SareeForm, SareeImageFormSet, CategoryForm, ContactForm


# ----------------------------------------------------------------------
# PUBLIC WEBSITE VIEWS
# ----------------------------------------------------------------------

def home(request):
    featured_sarees = Saree.objects.filter(is_active=True, is_featured=True)[:8]
    latest_sarees = Saree.objects.filter(is_active=True)[:8]
    categories = Category.objects.all()[:6]
    context = {
        'featured_sarees': featured_sarees,
        'latest_sarees': latest_sarees,
        'categories': categories,
        'active_page': 'home',
    }
    return render(request, 'shop/home.html', context)


def collection(request):
    sarees = Saree.objects.filter(is_active=True)
    categories = Category.objects.all()

    category_slug = request.GET.get('category')
    query = request.GET.get('q')

    active_category = None
    if category_slug:
        active_category = get_object_or_404(Category, slug=category_slug)
        sarees = sarees.filter(category=active_category)

    if query:
        sarees = sarees.filter(Q(name__icontains=query) | Q(description__icontains=query))

    sort = request.GET.get('sort')
    if sort == 'price_low':
        sarees = sarees.order_by('price')
    elif sort == 'price_high':
        sarees = sarees.order_by('-price')
    elif sort == 'name':
        sarees = sarees.order_by('name')

    paginator = Paginator(sarees, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'sarees': page_obj.object_list,
        'categories': categories,
        'active_category': active_category,
        'query': query or '',
        'sort': sort or '',
        'active_page': 'collection',
    }
    return render(request, 'shop/collection.html', context)


def product_detail(request, slug):
    saree = get_object_or_404(Saree, slug=slug, is_active=True)
    related_sarees = Saree.objects.filter(
        is_active=True, category=saree.category
    ).exclude(pk=saree.pk)[:4]
    context = {
        'saree': saree,
        'related_sarees': related_sarees,
        'active_page': 'collection',
    }
    return render(request, 'shop/product_detail.html', context)


def about(request):
    return render(request, 'shop/about.html', {'active_page': 'about'})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Your message has been sent. We will contact you soon.")
            return redirect('shop:contact')
    else:
        form = ContactForm()
    return render(request, 'shop/contact.html', {'form': form, 'active_page': 'contact'})


# ----------------------------------------------------------------------
# DASHBOARD (CUSTOM ADMIN) VIEWS
# ----------------------------------------------------------------------

def dashboard_login(request):
    if request.user.is_authenticated:
        return redirect('shop:dashboard_home')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('shop:dashboard_home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'dashboard/login.html', {'form': form})


@login_required
def dashboard_logout(request):
    logout(request)
    return redirect('shop:dashboard_login')


@login_required
def dashboard_home(request):
    sarees = Saree.objects.all().order_by('-created_at')
    context = {
        'total_sarees': sarees.count(),
        'active_sarees': sarees.filter(is_active=True).count(),
        'featured_sarees': sarees.filter(is_featured=True).count(),
        'total_categories': Category.objects.count(),
        'recent_sarees': sarees[:6],
        'recent_messages': ContactMessage.objects.all()[:5],
    }
    context['active'] = 'home'
    return render(request, 'dashboard/dashboard_home.html', context)


@login_required
def dashboard_saree_list(request):
    sarees = Saree.objects.all().order_by('-created_at')
    query = request.GET.get('q')
    if query:
        sarees = sarees.filter(Q(name__icontains=query))
    return render(request, 'dashboard/saree_list.html', {'sarees': sarees, 'query': query or '', 'active': 'sarees'})


@login_required
def dashboard_saree_add(request):
    if request.method == 'POST':
        form = SareeForm(request.POST)
        if form.is_valid():
            saree = form.save()
            formset = SareeImageFormSet(request.POST, request.FILES, instance=saree)
            if formset.is_valid():
                formset.save()
                # ensure at least one image is primary
                if saree.images.exists() and not saree.images.filter(is_primary=True).exists():
                    first_img = saree.images.first()
                    first_img.is_primary = True
                    first_img.save()
                messages.success(request, f'"{saree.name}" was added successfully.')
                return redirect('shop:dashboard_saree_list')
            else:
                saree.delete()
        else:
            formset = SareeImageFormSet(request.POST, request.FILES)
    else:
        form = SareeForm()
        formset = SareeImageFormSet()
    return render(request, 'dashboard/saree_form.html', {
        'form': form, 'formset': formset, 'title': 'Add New Saree', 'is_edit': False, 'active': 'sarees',
    })


@login_required
def dashboard_saree_edit(request, pk):
    saree = get_object_or_404(Saree, pk=pk)
    if request.method == 'POST':
        form = SareeForm(request.POST, instance=saree)
        formset = SareeImageFormSet(request.POST, request.FILES, instance=saree)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            if saree.images.exists() and not saree.images.filter(is_primary=True).exists():
                first_img = saree.images.first()
                first_img.is_primary = True
                first_img.save()
            messages.success(request, f'"{saree.name}" was updated successfully.')
            return redirect('shop:dashboard_saree_list')
    else:
        form = SareeForm(instance=saree)
        formset = SareeImageFormSet(instance=saree)
    return render(request, 'dashboard/saree_form.html', {
        'form': form, 'formset': formset, 'title': f'Edit "{saree.name}"', 'is_edit': True, 'saree': saree, 'active': 'sarees',
    })


@login_required
def dashboard_saree_delete(request, pk):
    saree = get_object_or_404(Saree, pk=pk)
    if request.method == 'POST':
        name = saree.name
        saree.delete()
        messages.success(request, f'"{name}" was deleted.')
        return redirect('shop:dashboard_saree_list')
    return render(request, 'dashboard/confirm_delete.html', {
        'object': saree, 'title': f'Delete "{saree.name}"', 'cancel_url': 'shop:dashboard_saree_list', 'active': 'sarees',
    })


@login_required
def dashboard_category_list(request):
    categories = Category.objects.all()
    return render(request, 'dashboard/category_list.html', {'categories': categories, 'active': 'categories'})


@login_required
def dashboard_category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            messages.success(request, f'Category "{category.name}" was added.')
            return redirect('shop:dashboard_category_list')
    else:
        form = CategoryForm()
    return render(request, 'dashboard/category_form.html', {'form': form, 'title': 'Add Category', 'is_edit': False, 'active': 'categories'})


@login_required
def dashboard_category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, f'Category "{category.name}" was updated.')
            return redirect('shop:dashboard_category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'dashboard/category_form.html', {
        'form': form, 'title': f'Edit "{category.name}"', 'is_edit': True, 'active': 'categories',
    })


@login_required
def dashboard_category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        name = category.name
        category.delete()
        messages.success(request, f'Category "{name}" was deleted.')
        return redirect('shop:dashboard_category_list')
    return render(request, 'dashboard/confirm_delete.html', {
        'object': category, 'title': f'Delete "{category.name}"', 'cancel_url': 'shop:dashboard_category_list', 'active': 'categories',
    })


@login_required
def dashboard_messages(request):
    contact_messages = ContactMessage.objects.all()
    return render(request, 'dashboard/messages.html', {'contact_messages': contact_messages, 'active': 'messages'})
