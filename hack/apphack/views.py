from django.shortcuts import render
from .models import Register, SignIn, First, Second, third
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.shortcuts import redirect


def reg(request):
    if request.method == 'POST':
        person = Register()
        person1 = SignIn()
        person.name = request.POST.get("name")
        person1.name = request.POST.get("name")

        if len(person.name) == 0 and len(person1.name) == 0:
            return render(request, 'reg.html')

        person.mail = request.POST.get("mail")
        if len(person.mail) == 0:
            return render(request, 'reg.html')

        person.passwd = request.POST.get("passwd")
        person1.passwd = request.POST.get("passwd")
        if len(person.passwd) == 0 and len(person1.passwd) == 0:
            return render(request, 'reg.html')
        person.save()
        person1.save()
        return render(request, 'auth.html', {"person_name": person1.name, "person_passwd": person1.passwd})

    return render(request, 'reg.html')


def reg2(request):
    if request.method == 'POST':
        # список всех пользователей
        for i in SignIn.objects.values_list("name", flat=True):
            if request.POST.get("name") in SignIn.objects.values_list():
                return render(request, "main.html")
    return render(request, "auth.html")


def main(request):
    return render(request, 'main.html')


def profile(request):
    return render(request, "profile.html")


def first(request):
    if request.method == 'POST':
        f1 = First()
        f1.wall_width = request.POST.get("wallWidth")
        f1.room_width = request.POST.get("wallX")
        f1.room_length = request.POST.get("wallY")
        f1.room_height = request.POST.get("wallZ")
        f1.toilet_x_сoordinate = request.POST.get("YnitazX")
        f1.toilet_y_сoordinate = request.POST.get("YnitazY")
        f1.toilet_z_сoordinate = request.POST.get("YnitazZ")
        f1.shell_x_coordinate = request.POST.get("RakovinaX")
        f1.shell_y_coordinate = request.POST.get("RakovinaY")
        f1.shell_z_coordinate = request.POST.get("RakovinaZ")
        f1.save()
        return HttpResponse("<h1>All data save</h1>")

    return render(request, "1.html")


def second(request):
    if request.method == 'POST':
        s2 = Second()
        s2.wall_width = request.POST.get("wall_width")  
        s2.first_room_width = request.POST.get("first_room_width") 
        s2.first_room_length = request.POST.get("first_room_length") 
        s2.first_room_height = request.POST.get("first_room_height") 
        s2.toilet_x_сoordinate = request.POST.get("toilet_x_сoordinate") 
        s2.toilet_y_сoordinate = request.POST.get("toilet_y_сoordinate") 
        s2.toilet_z_сoordinate = request.POST.get("toilet_z_сoordinate") 
        s2.first_shell_x_coordinate = request.POST.get("first_shell_x_coordinate") 
        s2.first_shell_y_coordinate = request.POST.get("first_shell_y_coordinate") 
        s2.first_shell_z_coordinate = request.POST.get("first_shell_z_coordinate") 
        s2.second_room_width = request.POST.get("second_room_width") 
        s2.second_room_length = request.POST.get("second_room_length") 
        s2.second_room_height = request.POST.get("second_room_height") 
        s2.second_shell_x_coordinate = request.POST.get("second_shell_x_coordinate") 
        s2.second_shell_y_coordinate = request.POST.get("second_shell_y_coordinate") 
        s2.second_shell_z_coordinate = request.POST.get("second_shell_z_coordinate") 
        s2.bath_x_сoordinate = request.POST.get("bath_x_сoordinate") 
        s2.bath_y_сoordinate = request.POST.get("bath_y_сoordinate") 
        s2.bath_z_сoordinate = request.POST.get("bath_z_сoordinate")
        s2.save()
        return HttpResponse("<h1>All data save</h1>")

    return render(request, "2.html")


def third(request):
    if request.method == 'POST':
        pass

    return render(request, "3.html")
