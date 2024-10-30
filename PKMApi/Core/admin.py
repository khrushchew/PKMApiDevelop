from django.contrib import admin

from .models.About import About
from .models.Company import Company
from .models.User import User
from .models.Role import Role
from .models.Subdivision import Subdivision
from .models.MachineStyle import MachineStyle
from .models.MachineGroup import MachineGroup
from .models.MachineType import MachineType
from .models.MachineName import MachineName
from .models.ShiftDay import ShiftDay
from .models.ShiftWorkingDayMode import ShiftWorkingDayMode
from .models.ShiftMode import ShiftMode
from .models.ShiftCalendar import ShiftCalendar
from .models.Area import Area
from .models.Platform import Platform
from .models.Department import Department



admin.site.register(About)
admin.site.register(Company)
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Subdivision)

admin.site.register(MachineStyle)
admin.site.register(MachineGroup)
admin.site.register(MachineType)
admin.site.register(MachineName)

admin.site.register(ShiftDay)
admin.site.register(ShiftWorkingDayMode)
admin.site.register(ShiftCalendar)
admin.site.register(ShiftMode)

admin.site.register(Platform)
admin.site.register(Department)
admin.site.register(Area)