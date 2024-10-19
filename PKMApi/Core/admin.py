from django.contrib import admin
from .models.Company import Company
from .models.User import User
from .models.Role import Role
from .models.Subdivision import Subdivision
from .models.MachineStyle import MachineStyle
from .models.MachineGroup import MachineGroup
from .models.MachineType import MachineType

admin.site.register(Company)
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Subdivision)
admin.site.register(MachineStyle)
admin.site.register(MachineGroup)
admin.site.register(MachineType)
