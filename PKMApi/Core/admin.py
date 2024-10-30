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
from .models import ShiftDay
from .models import ShiftWorkingDayMode
from .models import ShiftMode
from .models import ShiftCalendar

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
