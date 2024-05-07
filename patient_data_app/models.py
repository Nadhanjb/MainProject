from django.db import models

# Create your models here.
class login_table(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=20)


class hospital_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    hosp_name=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    pin = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=50)
    license_no= models.CharField(max_length=30)
    proof=models.FileField()
    status=models.CharField(max_length=30)

class dept_table(models.Model):
    dept_name=models.CharField(max_length=50)
    details=models.TextField()
    HOSPITAL=models.ForeignKey(hospital_table,on_delete=models.CASCADE)


class doctor_table(models.Model):
    LOGIN = models.ForeignKey(login_table,on_delete=models.CASCADE)
    DEPARTMENT = models.ForeignKey(dept_table, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    gender=models.CharField(max_length=35)
    dob=models.DateField()
    place=models.CharField(max_length=50)
    pin=models.BigIntegerField()
    post=models.CharField(max_length=30)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=50)
    qualification=models.TextField()
    specialization=models.CharField(max_length=100)
    experience=models.CharField(max_length=100)
    photo=models.FileField()


class patient_table(models.Model):
    LOGIN = models.ForeignKey(login_table,on_delete=models.CASCADE)
    health_id=models.CharField(max_length=10)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    gender=models.CharField(max_length=35)
    dob=models.DateField()
    place=models.CharField(max_length=50)
    pin=models.BigIntegerField()
    post=models.CharField(max_length=30)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=50)
    photo=models.FileField()

class medical_record_table(models.Model):
    PATIENT=models.ForeignKey(patient_table,on_delete=models.CASCADE)
    DOCTOR=models.ForeignKey(doctor_table,on_delete=models.CASCADE)
    disease = models.CharField(max_length=50)
    test_name = models.CharField(max_length=30)
    test_result = models.FileField()
    test_result_conclusion = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    date=models.DateField()

class appointment_table(models.Model):
    PATIENT = models.ForeignKey(patient_table, on_delete=models.CASCADE)
    DOCTOR = models.ForeignKey(doctor_table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.CharField(max_length=100)
    status=models.CharField(max_length=30)
    otp=models.BigIntegerField()
