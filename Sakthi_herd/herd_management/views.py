from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            return redirect("signin")
    else:
        return render(request, "signin.html")

@login_required(login_url="error_page")
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,
                                        last_name=last_name)
        user.save()
        print('user created')
        return redirect("signin")
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect("signin")

def error_page(request):
    return JsonResponse({'error': 'The resource was not found'}, status=404)

@login_required(login_url="error_page")
def bull(request):
    return render(request,'bull.html')

@login_required(login_url="error_page")
def buffalo_bull(request):
    return render(request,'bullbuffalo.html')

@login_required(login_url="error_page")
def cow(request):
    return render(request,'cow.html')

@login_required(login_url="error_page")
def buffalo_cow(request):
    return render(request,'cowbuffalo.html')

@login_required(login_url="error_page")
def cow_calf(request):
    return render(request,'cowcalf.html')

@login_required(login_url="error_page")
def buffalo_calf(request):
    return render(request,'buffalocalf.html')

@login_required(login_url="error_page")
def bull_or_buffalo_entry(request):
    return render(request,'bullandbullbuffalo.html')

@login_required(login_url="error_page")
def cow_or_buffalo_cow_entry(request):
    return render(request,'cowandcowbuffalo.html')

@login_required(login_url="error_page")
def cow_calf_or_buffalo_calf_entry(request):
    return render(request,'cowcalfandbullcalf.html')

@login_required(login_url="error_page")
def add_feed(request):
    return render(request,'addfeed.html')

@login_required(login_url="error_page")
def cattle_page_cow_profile(request):
    return render(request,'cattle_page_cow_profile.html')

@login_required(login_url="error_page")
def cattle_page_treatment(request):
    return render(request,'cattle_page_treatment.html')

@login_required(login_url="error_page")
def cattle_page_edit(request):
    return render(request,'cattle_page_edit.html')

@login_required(login_url="error_page")
def cattle_page_milk_report(request):
    return render(request,'cattle_page_milk_report.html')

@login_required(login_url="error_page")
def milk_data_entry(request):
    return render(request,'milk_reg.html')

@login_required(login_url="error_page")
def milk_data_overall_report(request):
    return render(request,'milk_report.html')

@login_required(login_url="error_page")
def insemination_entry(request):
    return render(request,'insemination.html')

@login_required(login_url="error_page")
def calving_entry(request):
    return render(request,'calving.html')

@login_required(login_url="error_page")
def deworming_entry(request):
    return render(request,'deworming.html')

@login_required(login_url="error_page")
def breeding_report(request):
    return render(request,'breed_report.html')

@login_required(login_url="error_page")
def treatment_entry(request):
    return render(request,'treatment.html')

@login_required(login_url="error_page")
def vaccination_entry(request):
    return render(request,'vaccination.html')

@login_required(login_url="error_page")
def reminder_alarm_IInd_heat(request):
    return render(request,'reminder_alarm.html')

@login_required(login_url="error_page")
def reminder_alarm_IIIrd_heat(request):
    return render(request,'reminder_alarm_IIIrd_heat.html')

@login_required(login_url="error_page")
def reminder_alarm_pregnancy_diagnosis(request):
    return render(request,'reminder_alarm_pregnancy_diagnosis.html')

@login_required(login_url="error_page")
def reminder_alarm_next_vaccination(request):
    return render(request,'reminder_alarm_next_vaccination.html')

@login_required(login_url="error_page")
def reminder_alarm_deworming(request):
    return render(request,'reminder_alarm_deworming.html')

@login_required(login_url="error_page")
def reminder_alarm_next_deworming(request):
    return render(request,'reminder_alarm_next_deworming.html')






