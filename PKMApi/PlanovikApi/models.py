from django.db import models

class Order(models.Model):
    number = models.CharField(unique=True, max_length=100)
    date_receipt = models.DateField()
    required_completion_date = models.DateField()
    priority = models.IntegerField(blank=True, null=True)
    order_status = models.ForeignKey('Orderstatus', models.DO_NOTHING, blank=True, null=True)
    calculated_completion_date = models.DateField(blank=True, null=True)
    actual_completion_date = models.DateField(blank=True, null=True)
    company = models.ForeignKey('Company', models.DO_NOTHING, blank=True, null=True)
    customer = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Order'

    def __str__(self):
        return f"Заказ"


class User(models.Model):
    login = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    company = models.ForeignKey('Company', models.DO_NOTHING, blank=True, null=True)
    role = models.ForeignKey('Role', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'

    def __str__(self):
        return f"{self.name}"


class Allocation(models.Model):
    role = models.ForeignKey('Role', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    area = models.ForeignKey('Area', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'allocation'


class Area(models.Model):
    name = models.CharField(max_length=255)
    indent = models.IntegerField(blank=True, null=True)
    department = models.ForeignKey('Department', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Batch(models.Model):
    name = models.CharField(max_length=255)
    count = models.IntegerField(blank=True, null=True)
    code = models.CharField(unique=True, max_length=100, blank=True, null=True)
    technology = models.TextField(blank=True, null=True)
    isready = models.BooleanField(blank=True, null=True)
    order = models.ForeignKey(Order, models.DO_NOTHING, blank=True, null=True)
    bath_archive = models.ForeignKey('Batcharchive', models.DO_NOTHING, blank=True, null=True)
    batch_status = models.ForeignKey('Batchstatus', models.DO_NOTHING, blank=True, null=True)
    rs_number = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batch'


class Batcharchive(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(unique=True, max_length=100)
    technology_number = models.CharField(max_length=100, blank=True, null=True)
    company = models.ForeignKey('Company', models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batcharchive'


class Batchstatus(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'batchstatus'


class Chiefbatch(models.Model):
    bath = models.ForeignKey(Batch, models.DO_NOTHING, blank=True, null=True)
    batch_status = models.ForeignKey(Batchstatus, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chiefbatch'


class Chiefdistribution(models.Model):
    stage = models.ForeignKey('Stage', models.DO_NOTHING, blank=True, null=True)
    operation = models.ForeignKey('Operation', models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    batch = models.ForeignKey(Batch, models.DO_NOTHING, blank=True, null=True)
    unit = models.ForeignKey('Department', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chiefdistribution'


class Chiefoperation(models.Model):
    chief_batch = models.ForeignKey(Chiefbatch, models.DO_NOTHING, blank=True, null=True)
    stage = models.ForeignKey('Stage', models.DO_NOTHING, blank=True, null=True)
    operation = models.ForeignKey('Operation', models.DO_NOTHING, blank=True, null=True)
    is_distributed = models.BooleanField(blank=True, null=True)
    distribution_stage = models.ForeignKey('Stagedistribution', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chiefoperation'


class Company(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=100)
    is_paid = models.BooleanField(blank=True, null=True)
    paid_machines_quantity = models.IntegerField(blank=True, null=True)
    date_of_start = models.DateField()
    date_of_end = models.DateField(blank=True, null=True)
    is_testdrive = models.BooleanField(blank=True, null=True)
    number_of_support_staff = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class Department(models.Model):
    name = models.CharField(max_length=255)
    field = models.ForeignKey('Field', models.DO_NOTHING, blank=True, null=True)
    indent = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    areas_quantity = models.IntegerField(blank=True, null=True)
    machines_quantity = models.IntegerField(blank=True, null=True)
    operators_quantity = models.IntegerField(blank=True, null=True)
    support_stuff_quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class Detailmachinetype(models.Model):
    name = models.CharField(max_length=255)
    first_machine_type = models.ForeignKey('Firstmachinetype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detailmachinetype'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Field(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'field'


class Firstmachinetype(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'firstmachinetype'


class Machine(models.Model):
    invent_number = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=255)
    area = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)
    is_activated = models.BooleanField(blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    shift_schedule = models.ForeignKey('Shiftschedule', models.DO_NOTHING, blank=True, null=True)
    prefix = models.CharField(max_length=50, blank=True, null=True)
    first_machine_type = models.ForeignKey(Firstmachinetype, models.DO_NOTHING, blank=True, null=True)
    second_machine_type = models.ForeignKey('Secondmachinetype', models.DO_NOTHING, blank=True, null=True)
    detail_machine_type = models.ForeignKey(Detailmachinetype, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machine'


class Machinework(models.Model):
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField(blank=True, null=True)
    work_status = models.ForeignKey('Workstatus', models.DO_NOTHING, blank=True, null=True)
    machine = models.ForeignKey(Machine, models.DO_NOTHING, blank=True, null=True)
    batch = models.ForeignKey(Batch, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    shift = models.ForeignKey('Shift', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()
    indent = models.IntegerField(blank=True, null=True)
    time_working = models.DurationField(blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    first_start_batch = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machinework'


class Operation(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, blank=True, null=True)
    time_pz = models.DurationField(blank=True, null=True)
    time_sh = models.DurationField(blank=True, null=True)
    stage = models.ForeignKey('Stage', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operation'


class Operationarchive(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, blank=True, null=True)
    time_pz = models.DurationField(blank=True, null=True)
    time_sh = models.DurationField(blank=True, null=True)
    stage_archive = models.ForeignKey('Stagearchive', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operationarchive'


class Operationoperator(models.Model):
    time_plan = models.DurationField(blank=True, null=True)
    time_first_start = models.DateTimeField(blank=True, null=True)
    time_start = models.DateTimeField(blank=True, null=True)
    time_stop = models.DateTimeField(blank=True, null=True)
    time_working = models.DurationField(blank=True, null=True)
    stage_status = models.ForeignKey('Stagestatus', models.DO_NOTHING, blank=True, null=True)
    batch = models.ForeignKey(Batch, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(Order, models.DO_NOTHING, blank=True, null=True)
    machine = models.ForeignKey(Machine, models.DO_NOTHING, blank=True, null=True)
    operation = models.ForeignKey(Operation, models.DO_NOTHING, blank=True, null=True)
    area = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)
    chief_operation = models.ForeignKey(Chiefoperation, models.DO_NOTHING, blank=True, null=True)
    chief_batch = models.ForeignKey(Chiefbatch, models.DO_NOTHING, blank=True, null=True)
    pause = models.BooleanField(blank=True, null=True)
    optimal_part = models.CharField(max_length=255, blank=True, null=True)
    modific = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    distribution_stage = models.ForeignKey('Stagedistribution', models.DO_NOTHING, blank=True, null=True)
    staff = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operationoperator'


class Orderstatus(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'orderstatus'

    def __str__(self):
        return f"{self.name}"


class Reporttype(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'reporttype'


class Role(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'role'


class Secondmachinetype(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'secondmachinetype'


class Shift(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shift'


class Shiftdistribution(models.Model):
    date = models.DateField()
    change = models.ForeignKey(Shift, models.DO_NOTHING, blank=True, null=True)
    machine = models.ForeignKey(Machine, models.DO_NOTHING, blank=True, null=True)
    staff = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shiftdistribution'


class Shiftschedule(models.Model):
    time_change = models.TimeField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    time_first = models.TimeField(blank=True, null=True)
    days = models.IntegerField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shiftschedule'


class Stage(models.Model):
    name = models.CharField(max_length=255)
    isdistributed = models.BooleanField(blank=True, null=True)
    area = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)
    batch = models.ForeignKey(Batch, models.DO_NOTHING, blank=True, null=True)
    batch_archive = models.ForeignKey(Batcharchive, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stage'


class Stagearchive(models.Model):
    name = models.CharField(max_length=255)
    batch_archive = models.ForeignKey(Batcharchive, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stagearchive'


class Stagedistribution(models.Model):
    stage = models.ForeignKey(Stage, models.DO_NOTHING, blank=True, null=True)
    chief_batch = models.ForeignKey(Chiefbatch, models.DO_NOTHING, blank=True, null=True)
    stage_status = models.ForeignKey('Stagestatus', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stagedistribution'


class Stagestatus(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'stagestatus'


class Transfer(models.Model):
    number = models.IntegerField()
    time_sh = models.DurationField(blank=True, null=True)
    operation = models.ForeignKey(Operation, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transfer'


class Transferarchive(models.Model):
    time_sh = models.DurationField(blank=True, null=True)
    operation_archive = models.ForeignKey(Operationarchive, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transferarchive'


class Transferoperation(models.Model):
    time_first_start = models.DateTimeField(blank=True, null=True)
    time_start = models.DateTimeField(blank=True, null=True)
    time_stop = models.DateTimeField(blank=True, null=True)
    time_working = models.DurationField(blank=True, null=True)
    batch = models.ForeignKey(Batch, models.DO_NOTHING, blank=True, null=True)
    machine = models.ForeignKey(Machine, models.DO_NOTHING, blank=True, null=True)
    operation = models.ForeignKey(Operation, models.DO_NOTHING, blank=True, null=True)
    chief_operation = models.ForeignKey(Chiefoperation, models.DO_NOTHING, blank=True, null=True)
    pause = models.BooleanField(blank=True, null=True)
    staff = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    opt_path = models.TextField(blank=True, null=True)
    transfer = models.ForeignKey(Transfer, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(Order, models.DO_NOTHING, blank=True, null=True)
    operator_operation = models.ForeignKey(Operationoperator, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transferoperation'


class Uploadedreport(models.Model):
    number = models.CharField(max_length=100)
    staff = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    report_type = models.ForeignKey(Reporttype, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uploadedreport'


class Version(models.Model):
    version = models.CharField(max_length=50)
    link_update = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'version'


class Workershift(models.Model):
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    isactive = models.BooleanField(blank=True, null=True)
    change = models.ForeignKey(Shift, models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()
    staff = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workershift'


class Workstatus(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'workstatus'
