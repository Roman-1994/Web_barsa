from datetime import date

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Contract(models.Model):
    name = models.CharField(max_length=20, default='1')
    terms_contract = models.CharField(max_length=100)
    date_sign = models.DateField()
    end_date = models.DateField()
    salary = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contract-detail', args=[str(self.id)])

class Posts(models.Model):
    title = models.CharField(max_length=20)
    duties = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Employee(models.Model):
    name = models.CharField(max_length=50, verbose_name='ФИО сотрудника')
    phone = models.CharField(max_length=11)
    age = models.IntegerField()
    date_birth = models.DateField()
    post = models.ManyToManyField(Posts)
    contract = models.ForeignKey(Contract, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_post(self):
        return ', '.join([post.title for post in self.post.all()])

    get_post.short_description = 'Должности'

class Footballers(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    age = models.IntegerField()
    date_birth = models.DateField()
    contract = models.ForeignKey(Contract, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Coach(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    age = models.IntegerField()
    date_birth = models.DateField()
    contract = models.ForeignKey(Contract, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('coach-detail', args=[str(self.id)])

class Teams(models.Model):
    title = models.CharField(max_length=20)
    footballer = models.ManyToManyField(Footballers)
    coach = models.ManyToManyField(Coach)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('teams-detail', args=[str(self.id)])

class Cities(models.Model):
    name = models.CharField(max_length=20)
    distance = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Stadiums(models.Model):
    name = models.CharField(max_length=30)
    city = models.ForeignKey(Cities, on_delete=models.DO_NOTHING)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class GameCalendar(models.Model):
    date = models.DateField(null=True)
    city = models.ForeignKey(Cities, on_delete=models.SET_NULL, null=True)
    stadium = models.ForeignKey(Stadiums, on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey(Teams, on_delete=models.DO_NOTHING)
    coach = models.ManyToManyField(Coach)
    footballer = models.ManyToManyField(Footballers)

    def __str__(self):
        return '%s %s %s %s' % (self.city, self.stadium, self.team, self.date)


class Tickets(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    num_tickets = models.PositiveIntegerField(default=0)
    game = models.ForeignKey(GameCalendar, on_delete=models.SET_NULL, null=True)
    date = models.DateField(null=True)

    @property
    def is_overdue(self):
        if self.date and date.today() > self.date:
            return True
        return False


