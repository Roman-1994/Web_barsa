from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .forms import UserForm, UserForm_2
from django.template.response import TemplateResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from barsa_app.models import *
from barsa_app.serializers import EmployeeSerializer


class EmployeeViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    """
    Employee CRUD methods.
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    permission_classes = [AllowAny]


def index(request):
    header = "Персональные данные"  # обычная переменная
    langs = ["Английский", "Немецкий", "Испанский"]  # массив
    user = {"name": "Максим,", "age": 30}  # словарь
    addr = ("Виноградная", 23, 45)  # кортеж
    data = {"header": header, "langs": langs, "user": user, "address": addr}
    #return TemplateResponse(request, 'main_list.html')
    return render(request, 'barsa_app/second_list.html', context=data)

def about(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        basket = request.POST.get('basket')
        data = request.POST.get('data')
        sity = request.POST.get('sity')
        commy = request.POST.get('commy')
        if basket:
            output = '<h2>Пользователь</h2><h3>Имя - {0}, Возраст - {1}, Отправлено - {2}, Город - {3}</h3><h3>Комментарий</h3><p>{4}</p>'.format(name, age, data, sity, commy)
        else:
            output = 'Вы ввели свои данные!'
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, 'barsa_app/main_list.html', {'form': userform})

def get_game_calendar(request):
    game_calendar = GameCalendar.objects.all()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request, 'barsa_app/game_calendar.html', {'game_calendar': game_calendar, 'num_visits': num_visits})

def get_footballers(request):
    footballer = Footballers.objects.all()
    return render(request, 'barsa_app/footballers.html', {'footballer': footballer})

def get_employee(request):
    '''Получение списка сотрудников'''
    employee = Employee.objects.all()
    return render(request, 'barsa_app/employee.html', {'employee': employee})

def create_employee(request):
    '''Сохранение нового сотрудника и переход к списку'''
    if request.method == 'POST':
        employee = Employee()
        employee.name = request.POST.get('name')
        employee.phone = request.POST.get('phone')
        employee.age = request.POST.get('age')
        employee.date_birth = request.POST.get('date_birth')
        employee.save()
    return HttpResponseRedirect('/')

def update_employee(request, id):
    '''Изменение данных сотрудника'''
    try:
        employee = Employee.objects.get(id=id)
        if request.method == 'POST':
            employee.name = request.POST.get('name')
            employee.phone = request.POST.get('phone')
            employee.age = request.POST.get('age')
            employee.date_birth = request.POST.get('date_birth')
            employee.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'barsa_app/up_employee.html', {'employee': employee})
    except Employee.DoesNotExist:
        return HttpResponseNotFound('<h2>Сотрудник не найден</h2>')

def delete_employee(request, id):
    '''Удаление сотрудника'''
    try:
        employee = Employee.objects.get(id=id)
        employee.delete()
        return HttpResponseRedirect('/')
    except Employee.DoesNotExist:
        return HttpResponseNotFound('<h2>Сотрудник не найден</h2>')

class TeamsListView(generic.ListView):
    model = Teams
    paginate_by = 2

class TeamsDetailView(generic.DetailView):
    model = Teams

class CoachListViev(generic.ListView):
    model = Coach
    paginate_by = 3

class CoachDetailView(generic.DetailView):
    model = Coach

class ContractListView(generic.ListView):
    model = Contract

class ContractDetailView(generic.DetailView):
    model = Contract

class TicketsByUserListView(LoginRequiredMixin, generic.ListView):
    model = Tickets
    template_name = 'barsa_app/tickets_list.html'

    def get_queryset(self):
        return Tickets.objects.filter(buyer=self.request.user)