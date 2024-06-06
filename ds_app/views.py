
# Create your views here.
import json
import smtplib
from datetime import datetime
from email.mime.text import MIMEText

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .myknn import prep
from ds_app.models import *
import pymysql
from .prediction_code import predictfn

def docreg(request):
    return render(request,"doctor/doctorregindex.html")


def login(request):
    return render(request,'login_index.html')

def doc_reg(request):
    return render(request, 'expert_reg.html')
def doctor_code(request):
    fn = request.POST['textfield']
    ln = request.POST['textfield2']
    ph = request.POST['textfield3']
    em = request.POST['textfield4']
    ql = request.POST['textarea']
    pl = request.POST['textarea2']
    pt = request.POST['textfield5']
    pn = request.POST['textfield6']
    dobb = request.POST['textfield7']
    usr = request.POST['textfield8']
    ps = request.POST['textfield9']
    gen = request.POST['radio']

    im = request.FILES['file']
    cnsltfee = request.POST['consult']
    certi = request.FILES['file1']
    sp =request.POST['specy']
    fs = FileSystemStorage()
    fsave = fs.save(im.name, im)
    fc = FileSystemStorage()
    fsav = fc.save(certi.name, certi)
    ob = login_table()
    ob.username = usr
    ob.password = ps
    ob.type = "pending"
    ob.save()

    oj = doctor_table()
    oj.fname = fn
    oj.lname = ln
    oj.phoneno = ph
    oj.email = em
    oj.qualification = ql
    oj.place = pl
    oj.post = pt
    oj.pin = pn
    oj.dob = dobb
    oj.image = fsave
    oj.consultfee = cnsltfee
    oj.gender = gen
    oj.specialization = sp
    oj.certificate = fsav
    oj.LOGIN_id = ob.id
    oj.save()
    return HttpResponse('''<script>alert("Registered ");window.location='/'</script>''')






def login_code(request):
    a=request.POST['textfield']
    b=request.POST['textfield2']
    try:

        ob=login_table.objects.get(username=a,password=b)
        if ob.type == 'admin':
            request.session['lid']=ob.id
            ob1=auth.authenticate(username='admin',password='123')
            if ob1 is not None:
                auth.login(request,ob1)
            return HttpResponse('''<script>alert("Successfully login");window.location='/admin_home'</script>''')

        elif ob.type == 'expert':
            ob1 = auth.authenticate(username='admin', password='123')
            if ob1 is not None:
                auth.login(request, ob1)
            request.session["eid"] = ob.id


            return HttpResponse('''<script>alert("Successfully login");window.location='/expert_home'</script>''')

        elif ob.type == 'doctor':
            ob1 = auth.authenticate(username='admin', password='123')
            if ob1 is not None:
                auth.login(request, ob1)
            request.session["lid"]=ob.id
            obb=doctor_table.objects.get(LOGIN__id=ob.id)
            request.session["name"] = obb.fname+" "+obb.lname
            request.session["sp"] = obb.specialization
            return HttpResponse('''<script>alert("Successfully login");window.location='/doctor_home'</script>''')

        else:
            return HttpResponse('''<script>alert("Invalid Password or Username");window.location='/'</script>''')

    except:
        return HttpResponse('''<script>alert("Invalid Password or Username");window.location='/'</script>''')


def logout(request):
    auth.logout(request)
    return render(request,'login_index.html')








@login_required(login_url='/')
def admin_home(request):
    return render(request,'adminindex.html')
@login_required(login_url='/')
def expert_home(request):
    return render(request,'expert/expertindex.html')
@login_required(login_url='/')
def doctor_home(request):
    return render(request,'doctor/doctorindex.html')
@login_required(login_url='/')

def blockaunb(request):
    ob = doctor_table.objects.all()
    return render(request, 'block_unblockD.html', {"data": ob})
@login_required(login_url='/')
def blockaunb_search(request):
    name = request.POST["textfield"]
    ob = doctor_table.objects.filter(fname__contains=name)
    return render(request, 'block_unblockD.html', {"data": ob})
@login_required(login_url='/')
def blockaunb_block(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='blocked'
    ob.save()
    return HttpResponse('''<script>alert("blocked ");window.location='/blockaunb'</script>''')
@login_required(login_url='/')
def blockaunb_unblock(request,id):
    ob = login_table.objects.get(id=id)
    ob.type = 'doctor'
    ob.save()
    return HttpResponse('''<script>alert("unblocked ");window.location='/blockaunb'</script>''')
@login_required(login_url='/')
def blockaunbExp(request):
    ob = expert_table.objects.all()
    return render(request, 'block_unblockE.html', {"data": ob})
@login_required(login_url='/')
def blockaunbExp_search(request):
    name = request.POST["textfield"]
    ob = expert_table.objects.filter(fname__contains=name)
    return render(request, 'block_unblockE.html', {"data": ob})
@login_required(login_url='/')
def blockaunbExp_block(request,id):
    ob = login_table.objects.get(id=id)
    ob.type = 'blocked'
    ob.save()
    return HttpResponse('''<script>alert("blocked ");window.location='/blockaunb'</script>''')
@login_required(login_url='/')
def blockaunbExp_unblock(request,id):
    ob = login_table.objects.get(id=id)
    ob.type = 'expert'
    ob.save()
    return HttpResponse('''<script>alert("unblocked ");window.location='/blockaunb'</script>''')
@login_required(login_url='/')
def expertreg(request):
    return render(request,'expertreg_index.html')

@login_required(login_url='/')
def exper_code(request):
    fn=request.POST['textfield']
    ln=request.POST['textfield2']
    ph = request.POST['textfield3']
    em = request.POST['textfield4']
    ql = request.POST['textarea']
    pl = request.POST['textarea2']
    pt = request.POST['textfield5']
    pn = request.POST['textfield6']
    dobb = request.POST['textfield7']
    usr = request.POST['textfield8']
    ps = request.POST['textfield9']

    im = request.FILES['file']
    fs=FileSystemStorage()
    fsave=fs.save(im.name,im)

    ob=login_table()
    ob.username=usr
    ob.password=ps
    ob.type="expert"
    ob.save()


    oj=expert_table()
    oj.fname=fn
    oj.lname=ln
    oj.phoneno=ph
    oj.email=em
    oj.qualification=ql
    oj.place=pl
    oj.post=pt
    oj.pin=pn
    oj.dob=dobb
    oj.image=fsave
    oj.LOGIN_id=ob.id
    oj.save()
    return redirect('/manage_expert')

@login_required(login_url='/')
def feedback(request):
    ob = feedback_table.objects.all()
    return render(request, 'feedback.html', {"data": ob})
@login_required(login_url='/')
def feedback_search(request):
    date=request.POST["textfield"]
    ob = feedback_table.objects.filter(date__exact=date)
    return render(request, 'feedback.html', {"data": ob})






@login_required(login_url='/')
def manage_expert(request):
    ob=expert_table.objects.all()
    return render(request,'manage_expert.html',{'val':ob})
@login_required(login_url='/')
def manage_expert_delete(request,id):
    ob=login_table.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("deleted");window.location='/manage_expert'</script>''')
@login_required(login_url='/')
def manage_expert_edit(request,id):
    ob=expert_table.objects.get(id=id)
    request.session["expertid"]=id
    return render(request,'edit_expert.html',{"data":ob})
@login_required(login_url='/')
def manage_expert_edit_post(request):
    fname = request.POST["textfield"]
    lname = request.POST["textfield2"]
    phoneno = request.POST["textfield3"]
    email = request.POST["textfield4"]
    qualification = request.POST["textarea"]
    place = request.POST["textarea2"]
    post = request.POST["textfield5"]
    pin = request.POST["textfield6"]
    dob = request.POST["textfield7"]
    img = request.FILES["file"]
    fs = FileSystemStorage()
    fsave = fs.save(img.name, img)


    ob=expert_table.objects.get(id=request.session["expertid"])
    ob.fname=fname
    ob.lname = lname
    ob.phoneno = phoneno
    ob.email = email
    ob.qualification = qualification
    ob.place = place
    ob.post = post
    ob.pin = pin
    ob.dob = dob
    ob.image = fsave
    ob.save()
    return HttpResponse('''<script>alert("updated");window.location='/manage_expert'</script>''')

@login_required(login_url='/')
def manage_expert_search(request):
    name=request.POST["textfield"]
    ob=expert_table.objects.filter(fname__contains=name)
    return render(request,'manage_expert.html',{'val':ob})
@login_required(login_url='/')
def reply(request):
    return render(request,'reply.html')
@login_required(login_url='/')
def verify_doc(request):
    ob=doctor_table.objects.all()
    return render(request,'verify_doctor.html',{"data":ob})
@login_required(login_url='/')
def verify_doc_search(request):
    name=request.POST["textfield"]
    ob=doctor_table.objects.filter(fname__contains=name)
    return render(request,'verify_doctor.html',{"data":ob})
@login_required(login_url='/')
def verify_doc_accept(request,id):
    ob = login_table.objects.filter(id=id).update(type="doctor")
    return HttpResponse('''<script>alert("ACCEPTED ");window.location='/verify_doc'</script>''')
@login_required(login_url='/')
def verify_doc_reject(request,id):
    ob = login_table.objects.filter(id=id).update(type="rejected")
    return HttpResponse('''<script>alert("REJECTED ");window.location='/verify_doc'</script>''')
@login_required(login_url='/')
def view_user(request):
    ob=user_table.objects.all()
    return render(request,'admin_view_users.html',{"data":ob})



@login_required(login_url='/')
def view_user_search(request):
    name = request.POST["textfield"]
    ob=user_table.objects.filter(fname__contains=name)
    return render(request,'admin_view_users.html',{"data": ob})

@login_required(login_url='/')

def user_accept(request, id):
    ob = login_table.objects.filter(id=id).update(type="user")
    return HttpResponse('''<script>alert("ACCEPTED ");window.location='/view_user#about'</script>''')

@login_required(login_url='/')
def user_reject(request, id):
    ob = login_table.objects.filter(id=id).update(type="rejected")
    return HttpResponse('''<script>alert("REJECTED ");window.location='/view_user#about'</script>''')

@login_required(login_url='/')
def complaints(request):
    ob = complaint_table.objects.all()
    return render(request, 'view_complaint.html', {"data": ob})
@login_required(login_url='/')
def complaints_search(request):
    date=request.POST["textfield"]
    ob = complaint_table.objects.filter(date__exact=date)
    return render(request, 'view_complaint.html', {"data": ob})
@login_required(login_url='/')
def adminreply(request,id):
    # ob=user_table.objects.get(id=id)
    request.session["complaintid"]=id
    return render(request,'reply.html' )

@login_required(login_url='/')
def reply_post(request):
    rep= request.POST["textarea"]
    ob= complaint_table.objects.get(id=request.session["complaintid"])
    ob.reply=rep
    ob.save()
    return HttpResponse('''<script>alert("replied");window.location='/complaints'</script>''')

@login_required(login_url='/')
def manage_tips(request):
    #request.session['eid'] = id
    ob=tip_table.objects.all()
    return render(request,'expert/manage_tips.html',{'data':ob})
@login_required(login_url='/')
def manage_tips_post(request):
    tips = request.POST["textarea"]
    ob = tip_table()
    ob.tip = tips
    ob.EXPERT = expert_table.objects.get(LOGIN__id=request.session['eid'])
    ob.save()
    return HttpResponse('''<script>alert("Added Tip");window.location='/manage_tips'</script>''')

@login_required(login_url='/')
def view_doubt(request):
    ob=doubt_table.objects.filter(EXPERT__LOGIN__id=request.session["eid"])
    return render(request,'expert/view_doubt.html',{'val':ob})

@login_required(login_url='/')
def searchdoubt(request):
    date=request.POST['textfield']
    ob=doubt_table.objects.filter(date=date)
    return render(request,'expert/view_doubt.html',{'val':ob})

@login_required(login_url='/')
def sendreply(request,id):
    request.session['pp']=id
    return render(request,"expert/doubtreply.html")

@login_required(login_url='/')
def sendreplycode(request):
    reply=request.POST['textarea']

    ob=doubt_table.objects.get(id=request.session['pp'])
    ob.reply=reply
    ob.save()
    return HttpResponse('''<script>alert("Reply sent");window.location='/view_doubt'</script>''')



@login_required(login_url='/')

def manage_schedule(request):
    ob=schedule_table.objects.filter(DOCTOR__LOGIN=request.session["lid"])
    return render(request,'doctor/manage_schedule.html',{'data':ob})


@login_required(login_url='/')
def manage_schedule_post(request):
    ftime = request.POST["textfield"]
    ttime = request.POST["textfield2"]
    date = request.POST["textfield3"]

    ob=schedule_table()
    ob.fromtime=ftime
    ob.totime=ttime
    ob.date=date
    ob.DOCTOR=doctor_table.objects.get(LOGIN=request.session["lid"])
    ob.save()
    return redirect('/manage_schedule')

@login_required(login_url='/')
def manage_schedule_delete(request,id):
    ob= schedule_table.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("deleted");window.location='/manage_schedule'</script>''')
@login_required(login_url='/')
def manage_schedule_edit(request,id):
    print("******************", id)
    ob=schedule_table.objects.get(id=id)
    request.session["scheduleid"]=id
    return render(request,'doctor/edit_scedule.html',{"data":ob})
@login_required(login_url='/')
def manage_schedule_edit_post(request):
    ftime = request.POST["textfield"]
    totime = request.POST["textfield2"]
    dt = request.POST["textfield3"]
    #schedule_id = request.POST["schedule_id"]  # Assuming you have a hidden field in your form to store the schedule ID

    #oj = schedule_table.objects.get(id=schedule_id)


    oj=schedule_table.objects.get(id=request.session["scheduleid"] )
    oj.fromtime=ftime
    oj.totime = totime
    oj.date = dt
    oj.save()
    return HttpResponse('''<script>alert("updated");window.location='/manage_schedule'</script>''')
@login_required(login_url='/')
def prescription(request,id):
    request.session['biid']=id
    ob=prescription_table.objects.all()
    return render(request,'doctor/prescription.html',{'data':ob})
@login_required(login_url='/')
def prescription_post(request):
    pres = request.POST["textarea"]
    rep = request.FILES["file"]
    fs=FileSystemStorage()
    fsave = fs.save(rep.name, rep)

    ob=prescription_table()
    ob.prescription=pres
    ob.report=fsave
    ob.BOOKING= booking_table.objects.get(id=request.session['biid'])
    ob.date =datetime.today()
    #ob.BOOKING=ob
    ob.save()
    return HttpResponse('''<script>alert("Added");window.location='/view_booking'</script>''')

@login_required(login_url='/')
def prescription_delete(request,id):
    ob= prescription_table.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("deleted");window.location='/view_booking#about'</script>''')

@login_required(login_url='/')
def view_booking(request):
    ob = booking_table.objects.filter(SCHEDULE__DOCTOR__LOGIN__id=request.session['lid'],SCHEDULE__date=datetime.today())

    return render(request,'doctor/view_booking.html',{'data':ob})
@login_required(login_url='/')
def view_booking_delete(request,id):
    ob= booking_table.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("deleted");window.location='/view_booking'</script>''')
@login_required(login_url='/')
def manage_tip_delete(request,id):
    ob= tip_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("deleted");window.location='/manage_tips'</script>''')

#+++++++++++++++++++++++++web chat=======================


def chatwithuser(request):
    ob = user_table.objects.all()
    return render(request,"expert/fur_chat.html",{'val':ob})




def chatview(request):
    ob = user_table.objects.all()
    d=[]
    for i in ob:
        r={"name":i.fname+" "+i.lname,'photo':"",'email':i.email,'loginid':i.LOGIN.id}
        d.append(r)
    return JsonResponse(d, safe=False)




def coun_insert_chat(request,msg,id):
    print("===",msg,id)
    ob=chat_table()
    ob.FROMID=login_table.objects.get(id=request.session['eid'])
    ob.TOID=login_table.objects.get(id=id)
    ob.message=msg
    ob.date=datetime.now().strftime("%Y-%m-%d")
    ob.time=datetime.now()
    ob.save()

    return JsonResponse({"task":"ok"})
    # refresh messages chatlist



def coun_msg(request,id):

    ob1=chat_table.objects.filter(FROMID__id=id,TOID__id=request.session['eid'])
    ob2=chat_table.objects.filter(FROMID__id=request.session['eid'],TOID__id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.FROMID.id,"msg":i.message,"date":i.date,"chat_id":i.id})

    obu=user_table.objects.get(LOGIN__id=id)


    return JsonResponse({"data":res,"name":obu.fname,"user_lid":obu.LOGIN.id})


#_______________________________WEBSERVICE_____________________________





def login_code1(request):
    username = request.POST['uname']
    password = request.POST['pass']
    try:
        users = login_table.objects.get(username=username, password=password)
        if users is None:
            data = {"task": "invalid"}

        else:
            data = {"task": "valid", "id": users.id}
            r = json.dumps(data)
            return HttpResponse(r)
    except:
        data = {"task": "invalid"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)


def registration(request):
    print(request.POST)
    firstname = request.POST['fname']
    lastname = request.POST['lname']
    place = request.POST['place']
    post_office = request.POST['post']
    pin_code = request.POST['pin']
    phone = request.POST['phone']
    age = request.POST['age']
    weight = request.POST['weight']
    email_id = request.POST['email']
    username = request.POST['usr']
    password = request.POST['pwrd']

    lob = login_table()
    lob.username = username
    lob.password = password
    lob.type = 'user'
    lob.save()

    user_obj = user_table()
    user_obj.fname = firstname
    user_obj.lname = lastname
    user_obj.place = place
    user_obj.post = post_office
    user_obj.pin = pin_code
    user_obj.phoneno = phone
    user_obj.email = email_id
    user_obj.age = age
    user_obj.weight = weight
    user_obj.LOGIN = lob
    user_obj.save()
    data = {"task": "success"}
    r = json.dumps(data)
    return HttpResponse(r)


def viewdep(request):
    ob = doctor_table.objects.all()
    data = []
    # dept.add(jo.getString("dep_name"));
    # dept_id.add(jo.getString("dep_id"));
    r=[]
    for i in ob:
        if i.specialization not in r:
            row = {'dep_name': i.specialization,'dep_id': i.specialization}
            data.append(row)
            r.append(i.specialization)
    r = json.dumps(data)
    return HttpResponse(r)


def viewtips_app(request):
    ob = tip_table.objects.all()
    data = []
    for i in ob:
        row = {'tips': i.tip}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)


def viewdoctor_all(request):
    print(request.POST)

    ob = doctor_table.objects.all()
    data = []
    for i in ob:
        row = {'name': i.fname+" "+i.lname,'phone':i.phoneno,'email':i.email,'specialization':i.specialization,'consultfee':i.consultfee,'address':i.place+" "+i.post+" "+str(i.pin),'id':i.id}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)




def viewdoctor(request):
    print(request.POST)
    dep=request.POST['dep']
    ob = doctor_table.objects.filter(specialization=dep)
    data = []
    for i in ob:
        row = {'name': i.fname+" "+i.lname,'phone':i.phoneno,'email':i.email,'specialization':i.specialization,'consultfee':i.consultfee,'address':i.place+" "+i.post+" "+str(i.pin),'id':i.id}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)



def viewexpert(request):
    print(request.POST)

    ob = expert_table.objects.all()
    data = []
    for i in ob:
        row = {'name': i.fname+" "+i.lname,'phone':i.phoneno,'qualification':i.qualification,'image':str(i.image.url),'place':i.place,'lid':i.LOGIN.id}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)



def viewshedule(request):
    did=request.POST['did']
    ob = schedule_table.objects.filter(DOCTOR__id=did,date__gte=datetime.today())
    data = []
    for i in ob:
        row = {'Date': str(i.date),'Ftime':str(i.fromtime),'Ttime':str(i.totime),'Sid':i.id}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)

def view_complaintreply(request):
    print(request.POST)
    c_id = request.POST['lid']
    ob = complaint_table.objects.filter(USER__LOGIN__id=c_id)
    data = []

    for i in ob:
        row = {'Reply': i.reply ,'complaint':i.complaint,'Date':str(i.date)}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)

def view_doubtreply(request):
    d_id = request.POST['did']
    ob = doubt_table.objects.filter(id=d_id)
    data = []
    for i in ob:
        row = {'reply': i.reply ,'doubt':i.doubt,'date':str(i.date)}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)


def send_complaint_app(request):
    print(request.POST)
    complaints = request.POST["complaint"]
    u_id = request.POST["lid"]
    date = datetime.now()
    reply = "pending"
    complaint_obj = complaint_table()
    complaint_obj.complaint = complaints
    complaint_obj.date = date
    complaint_obj.reply = reply
    complaint_obj.USER = user_table.objects.get(LOGIN__id=u_id)
    complaint_obj.save()
    data = {'task': 'success'}
    r = json.dumps(data)
    return HttpResponse(r)



def send_feedback_app(request):
    feedbacks = request.POST["feedback"]
    f_id = request.POST["lid"]
    date = datetime.now()
   # reply = "waiting"
    complaint_obj = feedback_table()
    complaint_obj.feedback = feedbacks
    complaint_obj.date = date
    #complaint_obj.reply = reply
    complaint_obj.USER = user_table.objects.get(LOGIN__id=f_id)
    complaint_obj.save()
    data = {'task': 'valid'}
    r = json.dumps(data)
    return HttpResponse(r)


def send_doubt_app(request):
    doubts = request.POST["Doubts"]
    d_id = request.POST["did"]
    eid = request.POST["eid"]
    date = datetime.now()
    reply = "waiting"
    complaint_obj = doubt_table()
    complaint_obj.doubt = doubts
    complaint_obj.date = date
    complaint_obj.reply = reply
    complaint_obj.USER = user_table.objects.get(LOGIN__id=d_id)
    complaint_obj.EXPERT = expert_table.objects.get(id=eid)
    complaint_obj.save()
    data = {'task': 'success'}
    r = json.dumps(data)
    return HttpResponse(r)



def booking(request):
    print(request.POST)
    d_id = request.POST["pat_id"]
    sid = request.POST["sid"]
    date = datetime.now()
    complaint_obj = booking_table()
    complaint_obj.date = date
    complaint_obj.USER = user_table.objects.get(LOGIN__id=d_id)
    complaint_obj.SCHEDULE = schedule_table.objects.get(id=sid)
    complaint_obj.save()
    data = {'task': 'success'}
    r = json.dumps(data)
    return HttpResponse(r)

def viewbooking(request):
    print(request.POST)
    d_id = request.POST["lid"]
    # USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    # SCHEDULE = models.ForeignKey(schedule_table, on_delete=models.CASCADE)
    # date = models.DateField()

    # dname.add(jo.getString("fname") + jo.getString("lname"));
    # date.add(jo.getString("Date"));
    # ftime.add(jo.getString("Ftime"));
    # ttime.add(jo.getString("Ttime"));
    # status.add(jo.getString("Status"));


    ob = booking_table.objects.filter(USER__LOGIN__id=d_id)

    data = []
    for i in ob:
        row = {'fname': i.SCHEDULE.DOCTOR.fname ,'lname': i.SCHEDULE.DOCTOR.lname ,'Ftime':str(i.SCHEDULE.fromtime),'Ttime':str(i.SCHEDULE.totime),'Date':str(i.date),'Status':str("Booked")}
        data.append(row)
    print(data)
    r = json.dumps(data)
    return HttpResponse(r)


def viewtips(request):

    ob = tip_table.objects.all()

    data = []
    for i in ob:
        row = {'tip': i.tip }
        data.append(row)
    print(data)
    r = json.dumps(data)
    return HttpResponse(r)
def downloadprescription(request):

    d_id = request.POST["lid"]
    # prescription


    ob = prescription_table.objects.filter(BOOKING__USER__LOGIN__id=d_id)

    data = []
    for i in ob:
        row = {'prescription': i.prescription ,"report":i.report.url}
        data.append(row)
    print(data)
    r = json.dumps(data)
    return HttpResponse(r)
def predict(request):
    print(request.POST,"jjjjjjjjjjjjjjjjjjjjj")
    try:
        d_id = request.POST["disease"]

        print(d_id, "jjjkkkkkkkkkjjjjjjjjjjjjjjjjjj")
        print(d_id, "jjjkkkkkkkkkjjjjjjjjjjjjjjjjjj")
    except:
        d_id = request.POST["disease"]
    # prescription
    ob = disease.objects.filter(disease=d_id)
    print(ob,"obbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    try:
        ob=doctor_table.objects.filter(specialization=ob[0].did.dep_name)
    except:
        ob=doctor_table.objects.filter(specialization="dermatologist")


    # doc.add(jo.getString("fname") + jo.getString("lname"));
    # docid.add(jo.getString("lid"));
    data = []
    for i in ob:
        row = {'fname': i.fname ,"lname":i.lname,"lid":i.id}
        data.append(row)
    print(data)
    r = json.dumps(data)
    return HttpResponse(r)
def AV_symptoms(request):



    ob = symptoms.objects.all()

    data = []
    for i in ob:
        row = {'symptom': i.symptom }
        if row not in data:
            data.append(row)
    print(data)
    r = json.dumps(data)
    return HttpResponse(r)
def AV_symptoms1(request):
    print(request.POST,"jhhhhhhhhhhhhj")
    print(request.POST,"jhhhhhhhhhhhhj")
    print(request.POST,"jhhhhhhhhhhhhj")
    print(request.POST,"jhhhhhhhhhhhhj")
    sym = request.POST['sym']
    syms = sym.split("#")
    print("---", syms)
    symrow = []
    for i in syms:

        if i != "":
            symrow.append(i)


    print(symrow)
    symrow = ",".join(symrow)
    print(symrow)
    symrow = "'" + symrow + "'"
    symrow = symrow.replace(",", "','")

    con = pymysql.connect(host='localhost', user='root', password='12345678', port=3306, db='disease prediction')
    cmd = con.cursor()
    qry = "SELECT DISTINCT `disease_id_id` FROM `ds_app_symptoms` WHERE `symptom` IN(" + symrow + ")"
    cmd.execute(qry)
    resss = cmd.fetchall()

    distdi = []
    for i in resss:
        print(i)
        distdi.append(str(i[0]))

    distdi = ','.join(distdi)

    try:
        cmd.execute("select distinct symptom from ds_app_symptoms WHERE `disease_id_id` IN(" + distdi + ") order by symptom")
    except:
        return JsonResponse({"task": "failed"})
    s = cmd.fetchall()
    print(s)
    dsym = []
    for i in s:
        dsym.append(i[0])
    row = []
    for w in dsym:
        if w in syms:
            row.append(1)
        else:
            row.append(0)

    ress = prep([row], distdi)
    qry = "select disease,treatment,preventive_measure,did_id from ds_app_disease where id=" + str(ress)
    cmd.execute(qry)
    res = cmd.fetchone()
    print(res[0], "aaaaaaaaaaaaaa")
    return JsonResponse({"task": res[0], "t": res[1], "pm": res[2], "did": str(res[3])})


def imagepredict(request):
    print(request.FILES)
    img = request.FILES['file']
    fs = FileSystemStorage()
    fn = fs.save(img.name, img)
    res=predictfn(r"C:\Users\HP\PycharmProjects\ds\media/"+fn)
    return JsonResponse({"task": "valid","res":res})



def forgotpassword1(request):
    print(request.POST)
    try:
        print("1")
        print(request.POST)
        email = request.POST['email']
        print(email)
        s = user_table.objects.get(email=email)
        print(s, "=============")
        if s is None:
            return JsonResponse({'task': 'invalid email'})
        else:
            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)
                gmail.ehlo()
                gmail.starttls()
                gmail.login('basimsalam77@gmail.com', 'filx sllr kppe kdyf')
                print("login=======")
            except Exception as e:
                print("Couldn't setup email!!" + str(e))
            msg = MIMEText("Your  password is : " + str(s.LOGIN.password))
            print(msg)
            msg['Subject'] = 'Password Recovery'
            msg['To'] = email
            msg['From'] = 'basimsalam77@gmail.com'

            print("ok====")

            try:
                gmail.send_message(msg)
                return JsonResponse({"task": "valid"})
            except Exception as e:
                return JsonResponse({"task":"invalid"})
            return JsonResponse({"task":"success"})
    except Exception as e:
        print(e)
        return JsonResponse({"task":"invalid"})

def view_message2(request):
    print(request.POST)
    fromid=request.POST['fid']
    toid=request.POST['toid']
    mid=request.POST['lastmsgid']
    print(mid,"uuuuuuuuuuuu0")
    ob=chat_table.objects.filter(Q(TOID__id=toid,FROMID__id=fromid,id__gt=mid)|Q(TOID_id=fromid,FROMID__id=toid,id__gt=mid)).order_by('id')
    print(ob,"YYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
    data=[]
    print("++++++++==============================")
    print("++++++++==============================")
    print("++++++++==============================")
    for i in ob:
        r={"Cid":i.id,"Date":i.date,"Message":i.message,"Fid":i.FROMID.id}
        data.append(r)
        print(r,"KKKKKKKKKKKKKKKKKKKKKKKKKKKK")
    # print(data,"JJJJJJJJJJJJJJJJJJJJJJJJJ")
    print(len(data),"=========================================")
    if len(data)>0:
        return JsonResponse({"status":"ok","res1":data})
    else:
        return JsonResponse({"status": "na"})



def in_message2(request):
    fromid = request.POST['fid']
    toid=request.POST['toid']
    chat = request.POST['msg']

    ob = chat_table()
    ob.message = chat
    ob.time = datetime.now().strftime("%H:%M:%S")
    ob.date = datetime.now()

    ob.FROMID = login_table.objects.get(id=fromid)
    ob.TOID = login_table.objects.get(id=toid)
    ob.save()
    data = {"status": "send"}
    r = json.dumps(data)

    print(r)
    return HttpResponse(r)



