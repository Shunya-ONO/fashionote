from django.shortcuts import render, redirect
from .models import Brand
from django.contrib.auth.decorators import login_required
from .forms import BrandForm
from django.db import models

# Create your views here.

def home(request):
    return render(request, 'fashionote/home.html', {})

@login_required
def index(request):
    """一覧画面"""
    brand = Brand.objects.filter(create_user=request.user)
    data = {'brand':brand}
    return render(request,'fashionote/index.html',data)

@login_required
def detail(request,brand_id):
    """詳細画面"""
    brand = Brand.objects.filter(pk=brand_id).first()
    data = {'brand':brand}
    return render(request,'fashionote/detail.html',data)

@login_required
def create(request):
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            tags = form.cleaned_data['tags']
            test = form.save(commit=False)
            test.create_user = request.user
            test.save()
            for tag in tags:
                test.tags.add(tag)
            return redirect('/detail/'+str(test.id))
        else:
            params['message'] = '再入力して下さい'
            params['form'] = form
    else:
        params['form'] = BrandForm()
    return render(request, 'fashionote/create.html', params)

@login_required
def update(request, brand_id):
    """更新"""
    brand = Brand.objects.filter(pk=brand_id).first()
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('/detail/'+str(brand.id))
    else:
        form = BrandForm(instance=brand)
        return render(request, 'fashionote/update.html', {'form':form, 'brand':brand})
@login_required
def delete(request, brand_id):
    """削除"""
    brand = Brand.objects.filter(pk=brand_id).first()
    brand.delete()
    return redirect('/index')
