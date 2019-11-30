from django.db import models


# Create your models here.


class incident(models.Model):
    incident_category = models.CharField(max_length=128)
    incident_subcategory = models.CharField(max_length=128)
    incident_code = models.IntegerField(null = False)


class reports(models.Model):
    incident_id = models.IntegerField()
    incident_number = models.IntegerField()
    cad_number = models.IntegerField(null=True)
    report_type_code = models.CharField(max_length=26)
    report_type_description = models.CharField(max_length=26)
    field_online = models.CharField(max_length=26)
    resolution = models.CharField(max_length=26)


class salary(models.Model):
    year_type = models.CharField(max_length=26)
    year = models.IntegerField()
    organisation_group_code = models.IntegerField()
    organisation_group = models.CharField(max_length=128)
    union = models.CharField(max_length=128)
    job_family_code = models.CharField(max_length=128)
    job = models.CharField(max_length=128)
    employee_identifier = models.IntegerField()
    salaries = models.IntegerField()
    other_salaries = models.IntegerField()
    total_salary = models.IntegerField()
    quarter = models.CharField(max_length=5)


class main(models.Model):
    row_id = models.IntegerField()
    incident_datetime = models.DateField()
    incident_day_of_week = models.CharField(max_length=26)
    report_datetime = models.DateField()
    incident_id = models.IntegerField()
    incident_number = models.IntegerField()
    incident_code = models.IntegerField()
    cnn = models.IntegerField()

class incident_address(models.Model):
    supervisor_district = models.IntegerField()
    analysis_neighborhood = models.IntegerField()
    cnn = models.IntegerField()
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    intersection = models.CharField(max_length=128)


class business_locations(models.Model):
    location_id = models.CharField(max_length=26)
    business_account_number = models.IntegerField()
    ownership_name = models.CharField(max_length=128)
    dba_name = models.CharField(max_length=128)
    street_address = models.CharField(max_length=128)
    source_zipcode = models.IntegerField()
    business_start_date = models.DateField()
    business_end_date = models.DateField()
    location_start_date = models.DateField()
    location_end_date = models.DateField()
    supervisor_district = models.IntegerField()
    analysis_neighborhood = models.CharField(max_length=128)
    business_corridor = models.CharField(max_length=26)
    business_location = models.CharField(max_length=26)