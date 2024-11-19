from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models.About import About
from .models.Company import Company
from .models.Device import Device
from .models import User

from .models.Subdivision import Subdivision
from .models.MachineStyle import MachineStyle
from .models.MachineGroup import MachineGroup
from .models.MachineType import MachineType
from .models.MachineName import MachineName
from .models.MachineControlMethod import MachineControlMethod
from .models.ShiftDay import ShiftDay
from .models.ShiftWorkingDayMode import ShiftWorkingDayMode
from .models.ShiftMode import ShiftMode
from .models.ShiftCalendar import ShiftCalendar
from .models.Area import Area
from .models.Platform import Platform
from .models.Department import Department
from .models.Brigade import Brigade
from django import forms

admin.site.register(About)
admin.site.register(Company)
admin.site.register(Device)

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data.get('password'):
            user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Персональная информация', {'fields': ('first_name', 'last_name', 'email', 'surname', 'profile_picture')}),
        ('Организация', {'fields': ('company', 'subdivision', 'position')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'session')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)





admin.site.register(Subdivision)

admin.site.register(MachineStyle)
admin.site.register(MachineGroup)
admin.site.register(MachineType)
admin.site.register(MachineName)
admin.site.register(MachineControlMethod)

admin.site.register(ShiftDay)
admin.site.register(ShiftWorkingDayMode)
admin.site.register(ShiftCalendar)
admin.site.register(ShiftMode)

admin.site.register(Platform)
admin.site.register(Department)
admin.site.register(Area)

admin.site.register(Brigade)