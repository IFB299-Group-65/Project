from django.db import modelsclass AuthGroup(models.Model):    name = models.CharField(unique=True, max_length=80)    class Meta:        managed = False        db_table = 'auth_group'class AuthGroupPermissions(models.Model):    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)    class Meta:        managed = False        db_table = 'auth_group_permissions'        unique_together = (('group', 'permission'),)class AuthPermission(models.Model):    name = models.CharField(max_length=255)    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)    codename = models.CharField(max_length=100)    class Meta:        managed = False        db_table = 'auth_permission'        unique_together = (('content_type', 'codename'),)class AuthUser(models.Model):    password = models.CharField(max_length=128)    last_login = models.DateTimeField(blank=True, null=True)    is_superuser = models.IntegerField()    username = models.CharField(unique=True, max_length=150)    first_name = models.CharField(max_length=30)    last_name = models.CharField(max_length=150)    email = models.CharField(max_length=254)    is_staff = models.IntegerField()    is_active = models.IntegerField()    date_joined = models.DateTimeField()    class Meta:        managed = False        db_table = 'auth_user'class AuthUserGroups(models.Model):    user = models.ForeignKey(AuthUser, models.DO_NOTHING)    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)    class Meta:        managed = False        db_table = 'auth_user_groups'        unique_together = (('user', 'group'),)class AuthUserUserPermissions(models.Model):    user = models.ForeignKey(AuthUser, models.DO_NOTHING)    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)    class Meta:        managed = False        db_table = 'auth_user_user_permissions'        unique_together = (('user', 'permission'),)class Car(models.Model):    car_id = models.IntegerField(db_column='Car_ID', primary_key=True)    car_makename = models.CharField(db_column='Car_MakeName', max_length=45, blank=True, null=True)    car_model = models.CharField(db_column='Car_Model', max_length=45, blank=True, null=True)    car_series = models.CharField(db_column='Car_Series', max_length=45, blank=True, null=True)    car_seriesyear = models.IntegerField(db_column='Car_SeriesYear', blank=True, null=True)    car_pricenew = models.IntegerField(db_column='Car_PriceNew', blank=True, null=True)    car_enginesize = models.CharField(db_column='Car_EngineSize', max_length=45, blank=True, null=True)    car_fuelsystem = models.CharField(db_column='Car_FuelSystem', max_length=45, blank=True, null=True)    car_tankcapacity = models.CharField(db_column='Car_TankCapacity', max_length=45, blank=True, null=True)    car_power = models.CharField(db_column='Car_Power', max_length=45, blank=True, null=True)    car_seatingcapacity = models.IntegerField(db_column='Car_SeatingCapacity', blank=True, null=True)    car_standardtransmission = models.CharField(db_column='Car_StandardTransmission', max_length=45, blank=True, null=True)    car_bodytype = models.CharField(db_column='Car_BodyType', max_length=45, blank=True, null=True)    car_drive = models.CharField(db_column='Car_Drive', max_length=45, blank=True, null=True)    car_wheelbase = models.CharField(db_column='Car_Wheelbase', max_length=45, blank=True, null=True)		#return cars where location, power, price and seats match/are close to (inputs)		#return model, price, power, seating, bodytype		#return all()    class Meta:        managed = True        db_table = 'car'class Carservice(models.Model):    service_id = models.IntegerField(db_column='Service_ID', primary_key=True)    car_id = models.IntegerField(db_column='Car_ID', blank=True, null=True)	#TODO service_date    service_location = models.CharField(db_column='Service_Location', max_length=45, blank=True, null=True)    service_price = models.IntegerField(db_column='Service_Price', blank=True, null=True)    service_issue = models.CharField(db_column='Service_Issue', max_length=45, blank=True, null=True)		#return > service date where carid = (input)    class Meta:        managed = True        db_table = 'carservice'class Customer(models.Model):    customer_id = models.IntegerField(db_column='Customer_ID', primary_key=True)    customer_name = models.CharField(db_column='Customer_Name', max_length=45, blank=True, null=True)    customer_phone = models.CharField(db_column='Customer_Phone', max_length=45, blank=True, null=True)    customer_addresss = models.CharField(db_column='Customer_Addresss', max_length=45, blank=True, null=True)    customer_brithday = models.DateField(db_column='Customer_Brithday', blank=True, null=True)    customer_occupation = models.CharField(db_column='Customer_Occupation', max_length=45, blank=True, null=True)    customer_gender = models.CharField(db_column='Customer_Gender', max_length=45, blank=True, null=True)		#login with password	    class Meta:        managed = True        db_table = 'customer'class DjangoAdminLog(models.Model):    action_time = models.DateTimeField()    object_id = models.TextField(blank=True, null=True)    object_repr = models.CharField(max_length=200)    action_flag = models.PositiveSmallIntegerField()    change_message = models.TextField()    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)    user = models.ForeignKey(AuthUser, models.DO_NOTHING)    class Meta:        managed = False        db_table = 'django_admin_log'class DjangoContentType(models.Model):    app_label = models.CharField(max_length=100)    model = models.CharField(max_length=100)    class Meta:        managed = False        db_table = 'django_content_type'        unique_together = (('app_label', 'model'),)class DjangoMigrations(models.Model):    app = models.CharField(max_length=255)    name = models.CharField(max_length=255)    applied = models.DateTimeField()    class Meta:        managed = False        db_table = 'django_migrations'class DjangoSession(models.Model):    session_key = models.CharField(primary_key=True, max_length=40)    session_data = models.TextField()    expire_date = models.DateTimeField()    class Meta:        managed = False        db_table = 'django_session'class Lostproperty(models.Model):    lostp_id = models.IntegerField(db_column='LostP_ID', primary_key=True)    lostp_order_id = models.IntegerField(db_column='LostP_Order_ID', blank=True, null=True)    lostp_description = models.CharField(db_column='LostP_Description', max_length=45, blank=True, null=True)    class Meta:        managed = True        db_table = 'lostproperty'class Orders(models.Model):    order_id = models.IntegerField(db_column='Order_ID', primary_key=True)    order_createdate = models.DateField(db_column='Order_CreateDate', blank=True, null=True)    order_pickupdate = models.DateField(db_column='Order_PickupDate', blank=True, null=True)    order_pickupstore = models.IntegerField(db_column='Order_PickupStore', blank=True, null=True)    order_returndate = models.DateField(db_column='Order_ReturnDate', blank=True, null=True)    customer_id = models.IntegerField(db_column='Customer_ID', blank=True, null=True)    car_id = models.IntegerField(db_column='Car_ID', blank=True, null=True)		#count of cars (location date /switch for pickup/drop off.)	#return count    class Meta:        managed = True        db_table = 'orders'class Staff(models.Model):    staff_id = models.IntegerField(db_column='Staff_ID', primary_key=True)    staff_name = models.CharField(db_column='Staff_Name', max_length=45, blank=True, null=True)    staff_phone = models.CharField(db_column='Staff_Phone', max_length=45, blank=True, null=True)    staff_address = models.CharField(db_column='Staff_Address', max_length=45, blank=True, null=True)    staff_birthday = models.DateField(db_column='Staff_Birthday', blank=True, null=True)    staff_position = models.CharField(db_column='Staff_Position', max_length=45, blank=True, null=True)    staff_gender = models.CharField(db_column='Staff_Gender', max_length=45, blank=True, null=True)	#access granted based on staff_position	    class Meta:        managed = True        db_table = 'staff'class Store(models.Model):    store_id = models.IntegerField(db_column='Store_ID', primary_key=True)    store_name = models.CharField(db_column='Store_Name', max_length=45, blank=True, null=True)    store_address = models.CharField(db_column='Store_Address', max_length=45, blank=True, null=True)    store_phone = models.CharField(db_column='Store_Phone', max_length=45, blank=True, null=True)    store_city = models.CharField(db_column='Store_City', max_length=45, blank=True, null=True)    store_state_name = models.CharField(db_column='Store_State_Name', max_length=45, blank=True, null=True)    class Meta:        managed = True        db_table = 'store'