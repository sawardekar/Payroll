from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.cache import cache_page
from staff import models
# Create your views here.

@login_required
def index(request):
    """
    Index method to check staff current status
    :param request:
    :return:
    """
    try:
        print(">>>>>>>",request.user.is_active)
        if request.user.is_active:

            return HttpResponseRedirect(reverse('emp'))
        else:
            return HttpResponseRedirect(reverse('login'))
    except:
        return HttpResponseRedirect(reverse('login'))


def user_login(request):
    """
    user_login method define to check Current login user is Authorize or not
    :param request:
    :return:
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                print(">>>>>>>>>>>>>", user.is_active)
                login(request, user)
                return HttpResponseRedirect(reverse('emp'))
            else:
                error_msg = "Your account was inactive."
                return render(request, 'staff/login.html', {'error': error_msg,'login_menu':True})
        else:
            error_msg = "Wrong username or password!, please try again with correct credentials"
            return render(request, 'staff/login.html', {'error': error_msg,'login_menu':True})
    else:
        return render(request, 'staff/login.html', {'error': '','login_menu':True})


def user_logout(request):
    logout(request)
    return render(request, 'staff/login.html', {'error': '','login_menu':True})

@login_required
@cache_page(60*15,key_prefix="cameras")
def emp(request):
    # location_count = models.StoreUnit.objects.filter(customer=customer).count()
    # area_count = models.StoreArea.objects.filter(store_id__customer=customer).count()
    # camera_count = models.StoreCamera.objects.filter(area__store_id__customer=customer).count()
    emp_obj = models.Employee.objects.filter().order_by('-id')
    emp_count = len(emp_obj)
    search = request.GET.get('emp_search', '')
    if search:
        emp_obj = emp_obj.filter(name__icontains=search)
    emp_data = []
    if emp_obj:
        page = request.GET.get('camera_page', 1)
        paginator = Paginator(emp_obj, 5)
        try:
            emp_data = paginator.page(page)
        except PageNotAnInteger:
            emp_data = paginator.page(1)
        except EmptyPage:
            emp_data = paginator.page(paginator.num_pages)

    return render(request, 'staff/emp.html',
                  {"emp_count": emp_count, "emp_data": emp_data, 'emp_menu': True})