from django.contrib import admin
from .models.Company import Company
from .models.User import User
from .models.Role import Role
from .models.Subdivision import Subdivision

admin.site.register(Company)
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Subdivision)
