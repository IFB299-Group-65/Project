from django.db import models

# Create your models here.
class Carservice(models.Model):
	service_id = models.IntegerField(db_column='Service_ID', primary_key=True)
	car_id = models.IntegerField(db_column='Car_ID')
	service_date = models.DateField(db_column='Service_Date')
	service_location = models.CharField(db_column='Service_Location', max_length=45, blank=True, null=True)
	service_price = models.IntegerField(db_column='Service_Price', blank=True, null=True)
	service_issue = models.CharField(db_column='Service_Issue', max_length=45, blank=True, null=True)

	
	class Meta:
		managed = True
		db_table = 'carservice'
