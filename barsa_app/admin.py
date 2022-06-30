from django.contrib import admin
from .models import Employee, Contract, Posts, Footballers, Coach, Teams, Cities, Stadiums, GameCalendar, Tickets

#admin.site.register(Contract)
admin.site.register(Posts)
#admin.site.register(Employee)
#admin.site.register(Footballers)
admin.site.register(Coach)
#admin.site.register(Teams)
admin.site.register(Cities)
admin.site.register(Stadiums)
admin.site.register(GameCalendar)

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_sign', 'end_date', 'salary')
    fields = ['name', ('date_sign', 'end_date'), 'salary']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_post')
    search_fields = ('name', )
    list_filter = ('post', 'contract')

@admin.register(Footballers)
class FootballersAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    exclude = ('phone',)
    fieldsets = (
        ('Имя и контракт', {
            'fields': ('name', 'contract')
        }),
        ('Возраст и дата рождения', {
            'fields': ('age', 'date_birth')
        }),
    )

class TeamGameCalendarInline(admin.TabularInline):
    model = GameCalendar

@admin.register(Teams)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [TeamGameCalendarInline]

@admin.register(Tickets)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('game', 'buyer')
    fields = ('game', 'buyer', 'num_tickets', 'date')
    list_filter = ('game', 'buyer', 'num_tickets')

# Register your models here.
