from django.db import models


# Create your models here.
class portalUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=255, null=False)
    phone_number = models.IntegerField()
    password = models.CharField(max_length=255, null=False)
    dob = models.DateField()
    name = models.CharField(max_length=255)


class policeDepartment(models.Model):
    dept_id = models.IntegerField(primary_key=True)
    district = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    cnn = models.IntegerField()
    telephone = models.IntegerField()
    supervisor = models.CharField(max_length=255)


class policeOfficial(models.Model):
    user_id = models.ForeignKey(portalUser, on_delete=models.CASCADE)
    dept_id = models.ForeignKey(policeDepartment, on_delete=models.CASCADE)
    official_rank = models.CharField(max_length=255)


class incidents(models.Model):
    incident_id = models.IntegerField(primary_key=True)
    dept_id = models.ForeignKey(policeDepartment, on_delete=models.CASCADE)
    incident_date = models.DateField()
    incident_time = models.TimeField()
    incident_year = models.IntegerField()


class complainant(models.Model):
    user_id = models.ForeignKey(incidents, on_delete=models.CASCADE)
    incident_id = models.ForeignKey(portalUser, on_delete=models.CASCADE)


class report(models.Model):
    report_id = models.IntegerField(primary_key=True)
    dept_id = models.ForeignKey(policeDepartment, on_delete=models.CASCADE)
    incident_id = models.ForeignKey(incidents, on_delete=models.CASCADE)
    incident_category = models.CharField(max_length=255)
    incident_subcategory = models.CharField(max_length=255)
    resolution = models.CharField(max_length=255)
    report_type = models.CharField(max_length=255)


# class location(models.Model):
#     incident_id = models.ForeignKey(incidents, on_delete=models.CASCADE)
#     longitude = models.DecimalField(max_digits=500)
#     latitude = models.DecimalField(max_digits=500)
#     intersection = models.CharField(max_length=255)
