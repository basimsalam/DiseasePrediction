from django.db import models

# Create your models here.
class login_table(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class expert_table(models.Model):
    LOGIN = models.ForeignKey(login_table,on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    phoneno=models.BigIntegerField()
    email=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.IntegerField()
    dob=models.DateField()
    image=models.FileField()

class doctor_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    phoneno = models.BigIntegerField()
    email = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.IntegerField()
    dob = models.DateField()
    image = models.FileField()
    gender=models.CharField(max_length=100)
    specialization=models.CharField(max_length=100)
    consultfee=models.IntegerField()
    certificate = models.FileField()

class user_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    phoneno = models.BigIntegerField()
    email = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.IntegerField()
    age = models.CharField(max_length=20)


class doubt_table(models.Model):
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    EXPERT = models.ForeignKey(expert_table, on_delete=models.CASCADE)
    doubt = models.CharField(max_length=500)
    date = models.DateField()
    reply = models.CharField(max_length=500)

class tip_table(models.Model):
    tip= models.CharField(max_length=500)
    EXPERT = models.ForeignKey(expert_table, on_delete=models.CASCADE)

class feedback_table(models.Model):
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    date = models.DateField()
    feedback = models.CharField(max_length=500)

class schedule_table(models.Model):
    DOCTOR = models.ForeignKey(doctor_table, on_delete=models.CASCADE)
    date = models.DateField()
    fromtime =  models.TimeField()
    totime = models.TimeField()

class booking_table(models.Model):
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    SCHEDULE = models.ForeignKey(schedule_table, on_delete=models.CASCADE)
    date = models.DateField()

class prescription_table(models.Model):
    BOOKING = models.ForeignKey(booking_table, on_delete=models.CASCADE)
    prescription = models.CharField(max_length=500)
    report = models.FileField()
    date = models.DateField()

class complaint_table(models.Model):
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=500)
    reply = models.CharField(max_length=500)
    date = models.DateField()




class department(models.Model):
    dep_name = models.CharField(max_length=500)




class disease(models.Model):
    disease = models.CharField(max_length=500)
    treatment = models.CharField(max_length=500)
    preventive_measure = models.CharField(max_length=500)
    did = models.ForeignKey(department,on_delete=models.CASCADE)


class symptoms(models.Model):
    disease_id = models.ForeignKey(disease,on_delete=models.CASCADE)
    symptom = models.CharField(max_length=500)

class chat_table(models.Model):
    FROMID = models.ForeignKey(login_table, on_delete=models.CASCADE,related_name="ft")
    TOID = models.ForeignKey(login_table, on_delete=models.CASCADE,related_name="tt")
    message = models.CharField(max_length=1000)
    date = models.DateField()
    time = models.TimeField()

