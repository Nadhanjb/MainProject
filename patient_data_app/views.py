import json
import smtplib
from email.mime.text import MIMEText
from random import random

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from patient_data_app.models import *


from web3 import Web3, HTTPProvider


from datetime import datetime,timedelta
# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:7545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]
compiled_contract_path = r"C:\Users\nadha\PycharmProjects\patient_data_using_blockchain\node_modules\.bin\build\contracts\Structrecord.json"
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0xC5E6Cc39873b1a3e1971AD0541b99c1A813eeeC2'



def home(request):
    return render(request,'homeindex.html')
def login(request):
    return render(request,'logindex.html')

def logout(request):
    auth.logout(request)
    return render(request,'logindex.html')


def logincode(request):
  uname=request.POST['textfield']
  pwd=request.POST['textfield2']
  try:
        ob=login_table.objects.get(username__exact=uname,password__exact=pwd)
        if(ob.username!=uname or ob.password!=pwd):
            return HttpResponse('''<script>alert('invalid username&password');window.location='/'</script>''')

        if ob.type == 'admin':
            ob1=auth.authenticate(username="admin",password="admin")
            if ob1 is not None:
                auth.login(request, ob1)
            request.session['lid'] = ob.id
            return HttpResponse('''<script>alert('welcome');window.location='/ahome'</script>''')
        elif ob.type == 'hospital':
            ob1=auth.authenticate(username="admin",password="admin")
            if ob1 is not None:
                auth.login(request, ob1)
            request.session['lid'] = ob.id
            obh=hospital_table.objects.get(LOGIN__id=ob.id)
            request.session['hname'] = obh.hosp_name
            return HttpResponse('''<script>alert('welcome');window.location='/hhome'</script>''')
        elif ob.type == 'doctor':
            ob1=auth.authenticate(username="admin",password="admin")
            if ob1 is not None:
                auth.login(request, ob1)
            request.session['lid'] = ob.id
            return HttpResponse('''<script>alert('welcome');window.location='/dhome'</script>''')
        elif ob.type == 'block':
            request.session['lid'] = ob.id
            return HttpResponse('''<script>alert('You have been blocked');window.location='/login'</script>''')
        elif ob.type == 'break':
            request.session['lid'] = ob.id
            return HttpResponse('''<script>alert('You are on you vacation!!');window.location='/login'</script>''')
        else:
            return HttpResponse('''<script>alert('invalid username&password');window.location='/login'</script>''')
  except:
        return HttpResponse('''<script>alert('invalid username&password');window.location='/login'</script>''')


def reg(request):
    username  = request.GET['username']
    print(username)
    data = {
        'is_taken': login_table.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message']="A user with this username already exists."

        # return HttpResponse("A user with this username already exists.")
    return JsonResponse(data)





######################################################## forgot password ###############################################3



def forgot(request):
    return render(request,'forgot password.html')

from django.core.mail import send_mail
import random
def forgot_password(request):
    print(request.POST,"+++++++++++++++++++++++++++++")
    try:
        uname=request.POST['textfield']
        g=login_table.objects.filter(username=uname)
        type = g[0].type
        if len(g) ==1:
            lid=g[0].id
            if type == "hospital":
                obu=hospital_table.objects.get(LOGIN__id=lid)
                mail=obu.email
                # send_mail('MediSafe Reset Password', "http://127.0.0.1:8000/fpwd1?id="+str(g.id), 'medisafea@gmail.com',[mail], fail_silently=False)
                try:
                    gmail = smtplib.SMTP('smtp.gmail.com', 587)
                    gmail.ehlo()
                    gmail.starttls()
                    gmail.login('medisafea@gmail.com', 'ryhb ksnv gaem kbnz')
                    print("login=======")
                except Exception as e:
                    print("Couldn't setup email!!" + str(e))
                msg = MIMEText("http://127.0.0.1:8000/fpwd1?id="+str(g[0].id))
                print(msg)
                msg['Subject'] = 'MediSafe Reset Passwor'
                msg['To'] = mail
                msg['From'] = 'medisafea@gmail.com'

                print("ok====")

                try:
                    gmail.send_message(msg)
                    return HttpResponse('''<script>alert('Check registred email to reset password');window.location='/forgot'</script>''')

                except Exception as e:
                    print(e)
                    pass
                    return HttpResponse('''<script>alert('couldn't send');window.location='/forgot'</script>''')

            elif type == "doctor":
                obu = doctor_table.objects.get(LOGIN__id=lid)
                print(obu)
                mail = obu.email
                print(mail)


                try:
                    gmail = smtplib.SMTP('smtp.gmail.com', 587)
                    gmail.ehlo()
                    gmail.starttls()
                    gmail.login('medisafea@gmail.com', 'ryhb ksnv gaem kbnz')
                    print("login=======")
                except Exception as e:
                    print("Couldn't setup email!!" + str(e))
                msg = MIMEText("http://127.0.0.1:8000/fpwd1?id="+str(g[0].id))
                print(msg)
                msg['Subject'] = 'MediSafe Reset Password'
                msg['To'] = mail
                msg['From'] = 'medisafea@gmail.com'

                print("ok====")

                try:
                    gmail.send_message(msg)
                    return HttpResponse('''<script>alert('Check registred email to reset password');window.location='/forgot'</script>''')

                except Exception as e:
                    print(e)
                    pass
                    return HttpResponse('''<script>alert('couldn't send');window.location='/forgot'</script>''')







                # send_mail('MediSafe Reset Password', "http://127.0.0.1:8000/fpwd1?id=" + str(g[0].id), 'medisafea@gmail.com',
                #           [mail], fail_silently=False)
                # return HttpResponse(
                # '''<script>alert('Check registred email to reset password');window.location='/forgot'</script>''')
        else:
            print('error==========')
            return HttpResponse('''<script>alert('Invalid data');window.location='/forgot'</script>''')
    except Exception as e:
        print(e,"")
        return HttpResponse('''<script>alert('Error');window.location='/'</script>''')

def fpwd1(request):
        request.session['uid']=request.GET['id']
        return render(request,"forgot2_index.html")



def resetForm(request):
        pwd=request.POST['textfield']
        pwd1=request.POST['textfield2']
        if pwd==pwd1 :

            ob=login_table.objects.get(id=request.session['uid'])
            ob.password=pwd1

            ob.save()
            return HttpResponse('''<script>alert('Password Updated');window.location='/'</script>''')
        else :
            return HttpResponse('''<script>alert('Password must be same');window.location='/'</script>''')



# def forgot_password(request):
#     username = request.POST['textfield']
#     email=request.POST['textfield2']
#     ob=login_table.objects.get(username=username)
#     if len(ob)==0:
#         return HttpResponse('''<script>alert('Invalid')''')
#     else:
#
#     try:
#         gmail = smtplib.SMTP('smtp.gmail.com', 587)
#         gmail.ehlo()
#         gmail.starttls()
#         gmail.login('medisafea@gmail.com', 'gipo zfni sbml lznx')
#         print("login=======")
#     except Exception as e:
#         print("Couldn't setup email!!" + str(e))
#     msg = MIMEText("Your Booking  OTP is: " + str(otp))
#     print(msg)
#     msg['Subject'] = 'Medisafe'
#     msg['To'] = email
#     msg['From'] = 'medisafea@gmail.com'
#
#     print("ok====")
#
#     try:
#         gmail.send_message(msg)
#         data = {"task": "valid", "otp": otp}
#         r = json.dumps(data)
#         return HttpResponse(r)
#     return render(request,'Login.html')



def hosp_reg(request):
    return render(request,'reg/regindex.html')

def hospitalreg(request):
    name = request.POST['Name']
    district = request.POST['select1']
    phone = request.POST['Phone no']
    email = request.POST['Email']
    place = request.POST['Place']
    pin = request.POST['Pin']
    post = request.POST['Post']
    lisence_no = request.POST['ln']
    proof=request.FILES['proof']
    fs=FileSystemStorage()
    fp=fs.save(proof.name,proof)
    password=request.POST['Password']
    ox = hospital_table.objects.filter(email=email)
    if len(ox) == 0:
        oy = hospital_table.objects.filter(license_no=lisence_no)
        if len(oy) == 0:
            ob=login_table()
            ob.username=email
            ob.password=password
            ob.type = 'pending'
            ob.save()
            hosp_obj = hospital_table()
            hosp_obj.hosp_name = name
            hosp_obj.district = district
            hosp_obj.phone = phone
            hosp_obj.email = email
            hosp_obj.place=place
            hosp_obj.pin =pin
            hosp_obj.post = post
            hosp_obj.license_no=lisence_no
            hosp_obj.proof=fp
            hosp_obj.status="pending"
            hosp_obj.LOGIN = ob
            hosp_obj.save()
            return HttpResponse('''<script>alert("Successfully registered!!");window.location="/"</script>''')
        else:
            return HttpResponse(
                '''<script>alert("This licence number was already exist so doesnt use it again");window.location="/hospitalreg"</script>''')

    else:
        return HttpResponse('''<script>alert("This email was already exist so doesnt use it again");window.location="/hospitalreg"</script>''')




################################################################################################



@login_required(login_url="/")
def ahome(request):
    return render(request,'Admin/aindex.html')

@login_required(login_url="/")
def hosp_verification(request):
    my_objects=hospital_table.objects.all().order_by('-id')
    # Set the number of items per page
    items_per_page = 3

    # Create a Paginator instance
    paginator = Paginator(my_objects, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)

    return render(request,'Admin/hospital verification.html',{'my_objects':my_objects})

@login_required(login_url="/")
def hosp_verification_search(request):
    name=request.POST['textfield']
    district=request.POST['select1']
    if (name == '' and district == 'ALL'):
        my_objects = hospital_table.objects.all()
        items_per_page = 3

        # Create a Paginator instance
        paginator = Paginator(my_objects, items_per_page)

        # Get the current page number from the request's GET parameters
        page = request.GET.get('page')

        try:
            # Get the Page object for the requested page
            my_objects = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver the first page
            my_objects = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g., 9999), deliver the last page
            my_objects = paginator.page(paginator.num_pages)
        return render(request, 'Admin/hospital verification.html', {'my_objects': my_objects, 'name': name,"d":district})
    if district == 'ALL':
        my_objects=hospital_table.objects.filter(hosp_name__istartswith=name)
        items_per_page = 3

        # Create a Paginator instance
        paginator = Paginator(my_objects, items_per_page)

        # Get the current page number from the request's GET parameters
        page = request.GET.get('page')

        try:
            # Get the Page object for the requested page
            my_objects = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver the first page
            my_objects = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g., 9999), deliver the last page
            my_objects = paginator.page(paginator.num_pages)
        return render(request,'Admin/hospital verification.html',{'my_objects':my_objects,'name':name,"d":district})
    if name == '':
        my_objects=hospital_table.objects.filter(district=district)
        items_per_page = 3

        # Create a Paginator instance
        paginator = Paginator(my_objects, items_per_page)

        # Get the current page number from the request's GET parameters
        page = request.GET.get('page')

        try:
            # Get the Page object for the requested page
            my_objects = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver the first page
            my_objects = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g., 9999), deliver the last page
            my_objects = paginator.page(paginator.num_pages)
        return render(request,'Admin/hospital verification.html',{'my_objects':my_objects,'name':name,"d":district})
    my_objects = hospital_table.objects.filter(district=district,hosp_name__istartswith=name)
    # Set the number of items per page
    items_per_page = 3

    # Create a Paginator instance
    paginator = Paginator(my_objects, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)

    return render(request, 'Admin/hospital verification.html', {'my_objects': my_objects, 'name': name,"d":district})

@login_required(login_url="/")
def breakdoc(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='break'
    ob.save()
    return HttpResponse('''<script>alert("added");window.location="/mng_dr"</script>''')



@login_required(login_url="/")
def joindoc(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='doctor'
    ob.save()
    return HttpResponse('''<script>alert("added");window.location="/mng_dr"</script>''')



@login_required(login_url="/")
def accpt_hosp(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='hospital'
    ob.save()
    oj=hospital_table.objects.get(LOGIN__id=id)
    oj.status="Verified"
    oj.save()
    return HttpResponse('''<script>alert("accepted");window.location="/hosp_verification"</script>''')

@login_required(login_url="/")
def reject_hosp(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='rejected'
    ob.save()
    oj = hospital_table.objects.get(LOGIN__id=id)
    oj.status = "Rejected"
    oj.save()
    return HttpResponse('''<script>alert('rejected');window.location='/hosp_verification#about'</script>''')




@login_required(login_url="/")
def view_block_hosp(request):
    ob = hospital_table.objects.filter(Q(LOGIN__type='hospital')|Q(LOGIN__type='block'))
    return render(request,'Admin/view and block unblock.html',{'val':ob})

@login_required(login_url="/")
def view_blockhosp_search(request):
    name=request.POST['textfield']
    ob=hospital_table.objects.filter(hosp_name__icontains=name)
    return render(request,'Admin/view and block unblock.html',{'val':ob,'name':name})

@login_required(login_url="/")
def block_hosp(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='block'
    ob.save()
    return HttpResponse('''<script>alert("blocked");window.location='/hosp_verification#about'</script>''')

def unblock_hosp(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='hospital'
    ob.save()
    return HttpResponse('''<script>alert('unblocked');window.location='/hosp_verification#about'</script>''')

@login_required(login_url="/")
def view_dr(request):
    ob=doctor_table.objects.all().order_by('-id')
    for i in ob:
        i.dob=int(datetime.now().strftime("%Y"))-int(str(i.dob).split("-")[0])
    oj=hospital_table.objects.filter(LOGIN__type="hospital")
    return render(request,'Admin/view doctor.html',{'val':ob,'val1':oj})

@login_required(login_url="/")
def view_dr_search(request):
    hid = request.POST['select']
    district=request.POST['select1']
    list_id = []
    list_d = []
    intersection =[]
    oj=hospital_table.objects.filter(LOGIN__type="hospital")
    # ob=doctor_table.objects.filter(Q(DEPARTMENT__HOSPITAL_id=hid)|Q(DEPARTMENT__HOSPITAL__district=district))
    ob1=doctor_table.objects.filter(DEPARTMENT__HOSPITAL_id=hid)
    for i in ob1:
        list_id.append(i.id)
    ob2=doctor_table.objects.filter(DEPARTMENT__HOSPITAL__district=district)
    for i in ob2:
        list_d.append(i.id)

    intersection = list(set(list_id).intersection(list_d))
    ob=doctor_table.objects.filter(id__in=intersection)
    if len(ob) == 0:
        ob=doctor_table.objects.filter(Q(DEPARTMENT__HOSPITAL_id=hid)|Q(DEPARTMENT__HOSPITAL__district=district))
        return render(request, 'Admin/view doctor.html', {'val': ob, 'val1': oj, 'd': district, 'hid': int(hid)})

    return render(request,'Admin/view doctor.html',{'val':ob,'val1':oj, 'd':district, 'hid': int(hid)})




    # print(hid, district)
    # if (hid == '' and district == 'ALL'):
    #     ob = doctor_table.objects.all()
    #     return render(request, 'Admin/view doctor.html', {'val': ob,'val1':oj,'name': hid, "d": district})
    # if district == 'ALL':
    #     ob = doctor_table.objects.filter(DEPARTMENT__HOSPITAL__id=hid)
    #     return render(request, 'Admin/view doctor.html', {'val': ob, 'name': hid, "d": district,'val1':oj})
    # if hid == '':
    #     ob = doctor_table.objects.filter(DEPARTMENT__HOSPITAL__district=district)
    #     return render(request, 'Admin/view doctor.html', {'val': ob, 'name': hid, "d": district,'val1':oj})
    # ob = doctor_table.objects.filter(DEPARTMENT__HOSPITAL__district=district, DEPARTMENT__HOSPITAL__id=hid)


    # return render(request, 'Admin/view doctor.html', {'val': ob, 'name': hid, "d": district,'val1':oj})
@login_required(login_url="/")
def view_patient_ad(request):
    my_objects = patient_table.objects.all().order_by('-id')
    for i in my_objects:
        i.dob = int(datetime.now().strftime("%Y")) - int(str(i.dob).split("-")[0])
        # Set the number of items per page
    items_per_page = 3

    # Create a Paginator instance
    paginator = Paginator(my_objects, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)
    return render(request,'Admin/view patient.html',{'my_objects':my_objects})

@login_required(login_url="/")
def view_patient_search(request):
    name=request.POST['textfield']
    my_objects = patient_table.objects.filter(fname__istartswith=name)
    # Set the number of items per page
    items_per_page = 3

    # Create a Paginator instance
    paginator = Paginator(my_objects, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)
    return render(request,'Admin/view patient.html',{'my_objects':my_objects})





@login_required(login_url="/")
def hhome(request):
    ob = hospital_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request,'Hospital Administrator/hindex.html',{'val':ob})

@login_required(login_url="/")
def update_profile(request):
    ob=hospital_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request,'Hospital Administrator/edit profile.html',{'val':ob})

@login_required(login_url="/")
def update_profile_action(request):

    print(request.session['lid'])
    try:
        hs_obj = hospital_table.objects.get(LOGIN__id=request.session['lid'])
        name = request.POST['Name']
        district=request.POST['select1']
        place = request.POST['Place']
        pin = request.POST['Pin']
        post = request.POST['Post']
        phone = request.POST['Phone no']
        email = request.POST['Email']
        license_no = request.POST['ln']
        proof = request.FILES['proof']
        fs = FileSystemStorage()
        fsave = fs.save(fs.name, proof)

        hs_obj.hosp_name = name
        hs_obj.district = district
        hs_obj.place = place
        hs_obj.pin = pin
        hs_obj.post = post
        hs_obj.phone = phone
        hs_obj.email = email
        hs_obj.license_no=license_no
        hs_obj.proof = fsave
        hs_obj.save()
        return HttpResponse('''<script>window.location="/hhome#about"</script>''')
    except:
        hs_obj = hospital_table.objects.get(LOGIN__id=request.session['lid'])
        name = request.POST['Name']
        district = request.POST['select1']
        place = request.POST['Place']
        pin = request.POST['Pin']
        post = request.POST['Post']
        phone = request.POST['Phone no']
        email = request.POST['Email']
        license_no = request.POST['ln']
        # proof = request.FILES['proof']
        # photo = request.FILES['file']
        # fs = FileSystemStorage()
        # fsave = fs.save(photo.name, photo)
        hs_obj.hosp_name = name
        hs_obj.district = district
        hs_obj.place = place
        hs_obj.pin = pin
        hs_obj.post = post
        hs_obj.phone = phone
        hs_obj.email = email
        hs_obj.license_no = license_no
        # dr_obj.photo = fsave
        hs_obj.save()
        return HttpResponse('''<script>window.location="/hhome"</script>''')





@login_required(login_url="/")
def mng_dep(request):
    my_objects=dept_table.objects.filter(HOSPITAL__LOGIN__id=request.session['lid']).order_by('-id')
    # Set the number of items per page
    items_per_page = 2
    # Create a Paginator instance
    paginator = Paginator(my_objects, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)
    return render(request, 'Hospital Administrator/manage department.html',{'my_objects':my_objects})

@login_required(login_url="/")
def search_mng_dep(request):
    name=request.POST['textfield']
    my_objects=dept_table.objects.filter(HOSPITAL__LOGIN__id=request.session['lid'],dept_name__istartswith=name)
    # Set the number of items per page
    items_per_page = 2

    # Create a Paginator instance
    paginator = Paginator(my_objects, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)
    return render(request, 'Hospital Administrator/manage department.html',{'my_objects':my_objects,"name":name})

@login_required(login_url="/")
def add_dept(request):
    return render(request, 'Hospital Administrator/add department.html')

@login_required(login_url="/")
def add_dept_action(request):
    dep = request.POST['textfield']
    details = request.POST['textarea']
    dept_obj = dept_table()
    dept_obj.dept_name = dep
    dept_obj.details = details
    dept_obj.HOSPITAL=hospital_table.objects.get(LOGIN__id=request.session['lid'])
    dept_obj.save()
    return HttpResponse('''<script>window.location="/mng_dep#about"</script>''')

@login_required(login_url="/")
def edit_dept(request, dept_id):
    request.session['dept_id'] = dept_id
    ob = dept_table.objects.get(id=dept_id)
    return render(request, 'Hospital Administrator/edit department.html', {'val': ob})

@login_required(login_url="/")
def edit_dept_action(request):
    dept_obj = dept_table.objects.get(id=request.session['dept_id'])
    dep = request.POST['textfield']
    details = request.POST['textarea']
    dept_obj.dept_name = dep
    dept_obj.details = details
    dept_obj.save()
    return HttpResponse('''<script>window.location="/mng_dep#about"</script>''')


@login_required(login_url="/")
def dlt_depart(request,id):
    ob=dept_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>window.location="/mng_dep#about"</script>''')

@login_required(login_url="/")
def mng_dr(request):
    ob1=dept_table.objects.filter(HOSPITAL__LOGIN__id=request.session['lid'])
    ob =doctor_table.objects.filter(DEPARTMENT__HOSPITAL__LOGIN__id=request.session['lid']).order_by('-id')
    for i in ob:
        i.dob=int(datetime.now().strftime("%Y"))-int(str(i.dob).split("-")[0])
    return render(request,'Hospital Administrator/Manage doctors.html',{'val':ob,'val1':ob1})


@login_required(login_url="/")
def mng_dr_search(request):
    dep=request.POST['select']
    ob1=dept_table.objects.filter(HOSPITAL__LOGIN__id=request.session['lid'],id=dep)
    ob =doctor_table.objects.filter(DEPARTMENT__HOSPITAL__LOGIN__id=request.session['lid'],DEPARTMENT__id=dep)

    return render(request,'Hospital Administrator/Manage doctors.html',{'val':ob,'val1':ob1,'dep':int(dep)})

@login_required(login_url="/")
def add_dr(request):
    # ob = doctor_table.objects.all()
    ob1=dept_table.objects.filter(HOSPITAL__LOGIN__id=request.session['lid'])
    return render(request,'Hospital Administrator/add doctor.html',{'val1':ob1})

@login_required(login_url="/")
def add_dr_action(request):
    name = request.POST['textfield']
    gender= request.POST['radiobutton']
    dob = request.POST['textfield10']
    place = request.POST['textfield2']
    pin = request.POST['textfield22']
    post = request.POST['textfield23']
    phone = request.POST['textfield3']
    email = request.POST['textfield4']
    qualification = request.POST['textfield5']
    experience=request.POST['textfield6']
    specialization=request.POST['textfield7']
    department = request.POST['select']
    photo = request.FILES['file']
    fs = FileSystemStorage()
    fsave = fs.save(photo.name, photo)
    password=request.POST['textfield9']
    ox=doctor_table.objects.filter(email = email)
    if len(ox) == 0:
        oy = doctor_table.objects.filter(phone = phone)
        if len(oy) == 0:
                ob = login_table()
                ob.username = email
                ob.password = password
                ob.type = 'doctor'
                ob.save()
                dr_obj = doctor_table()
                dr_obj.name = name
                dr_obj.gender = gender
                dr_obj.dob = dob
                dr_obj.place = place
                dr_obj.pin = pin
                dr_obj.post = post
                dr_obj.phone = phone
                dr_obj.email = email
                dr_obj.qualification = qualification
                dr_obj.experience = experience
                dr_obj.specialization = specialization
                dr_obj.DEPARTMENT = dept_table.objects.get(id=department)
                dr_obj.photo = fsave
                dr_obj.LOGIN = ob
                dr_obj.save()
                return HttpResponse('''<script>window.location="/mng_dr#about"</script>''')
        else:

            return HttpResponse(
                '''<script>alert("This phone was already exist so doesnt use it again");window.location="/add_dr#about"</script>''')

    else:
        return HttpResponse('''<script>alert("This email was already exist so doesnt use it again");window.location="/add_dr#about"</script>''')


@login_required(login_url="/")
def edit_dr(request,id):
    request.session['dr_id'] = id
    ob1=dept_table.objects.filter(HOSPITAL__LOGIN__id=request.session['lid'])
    ob2=doctor_table.objects.get(id=id)
    return render(request, 'Hospital Administrator/edit doctor.html',{ 'val1':ob1,'val2':ob2 ,"d":str(ob2.dob)})

@login_required(login_url="/")
def edit_dr_action(request):
    try:
        dr_obj = doctor_table.objects.get(id=request.session['dr_id'])
        name = request.POST['textfield']
        gender = request.POST['radiobutton']
        dob = request.POST['textfield10']
        place = request.POST['textfield2']
        pin = request.POST['textfield22']
        post = request.POST['textfield23']
        phone = request.POST['textfield3']
        email = request.POST['textfield4']
        qualification = request.POST['textfield5']
        experience = request.POST['textfield6']
        specialization = request.POST['textfield7']
        department = request.POST['select']
        photo = request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(photo.name, photo)
        dr_obj.name = name
        dr_obj.gender = gender
        dr_obj.dob = dob
        dr_obj.place = place
        dr_obj.pin = pin
        dr_obj.post = post
        dr_obj.phone = phone
        dr_obj.email = email
        dr_obj.qualification = qualification
        dr_obj.experience = experience
        dr_obj.specialization = specialization
        dr_obj.DEPARTMENT = dept_table.objects.get(id=department)
        dr_obj.photo = fsave
        dr_obj.save()
        return HttpResponse('''<script>window.location="/mng_dr#about"</script>''')
    except:
        dr_obj = doctor_table.objects.get(id=request.session['dr_id'])
        name = request.POST['textfield']
        gender = request.POST['radiobutton']
        dob = request.POST['textfield10']
        place = request.POST['textfield2']
        pin = request.POST['textfield22']
        post = request.POST['textfield23']
        phone = request.POST['textfield3']
        email = request.POST['textfield4']
        qualification = request.POST['textfield5']
        experience = request.POST['textfield6']
        specialization = request.POST['textfield7']
        department = request.POST['select']
        # photo = request.FILES['file']
        # fs = FileSystemStorage()
        # fsave = fs.save(photo.name, photo)
        dr_obj.name = name
        dr_obj.gender = gender
        dr_obj.dob = dob
        dr_obj.place = place
        dr_obj.pin = pin
        dr_obj.post = post
        dr_obj.phone = phone
        dr_obj.email = email
        dr_obj.qualification = qualification
        dr_obj.experience = experience
        dr_obj.specialization = specialization
        dr_obj.DEPARTMENT = dept_table.objects.get(id=department)
        # dr_obj.photo = fsave
        dr_obj.save()
        return HttpResponse('''<script>window.location="/mng_dr"</script>''')

@login_required(login_url="/")
def dlt_dr(request,id):
    ob=doctor_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>window.location="/mng_dr#about"</script>''')

@login_required(login_url="/")
def mng_app(request):
    ob=appointment_table.objects.filter(DOCTOR__DEPARTMENT__HOSPITAL__LOGIN__id=request.session['lid']).order_by('-id')
    obb = doctor_table.objects.filter(DEPARTMENT__HOSPITAL__LOGIN__id=request.session['lid'])
    return render(request,'Hospital Administrator/manage appointment.html',{'val':ob,'val1':obb})

@login_required(login_url="/")
def mng_app_search(request):
    did=request.POST['select']
    print(did,"jjjjjjjjjjjjjjjjjj")
    date=request.POST['textfield']
    list_id = []
    list_d = []
    intersection =[]
    obb = doctor_table.objects.filter(DEPARTMENT__HOSPITAL__LOGIN__id=request.session['lid'])
    ob1=appointment_table.objects.filter(DOCTOR_id=did)
    for i in ob1:
        list_id.append(i.id)
    try:
        ob2=appointment_table.objects.filter(date=date)
    except:
        ob = appointment_table.objects.filter(DOCTOR_id=did)
        return render(request,'Hospital Administrator/manage appointment.html',{'val':ob,'val1':obb,'did':int(did),"dt":str(date)})
    for i in ob2:
        list_d.append(i.id)
    intersection = list(set(list_id).intersection(list_d))
    ob=appointment_table.objects.filter(id__in=intersection)
    if len(ob) == 0:
        try:
            ob=appointment_table.objects.filter(Q(DOCTOR_id=did)|Q(date=date))
        except:
            ob=appointment_table.objects.filter(DOCTOR_id=did)
        return render(request,'Hospital Administrator/manage appointment.html',{'val':ob,'val1':obb,'did':int(did),"dt":str(date)})
    return render(request,'Hospital Administrator/manage appointment.html',{'val':ob,'val1':obb,'did':int(did),"dt":str(date)})

    # try:
    #     ob = appointment_table.objects.filter(Q(DOCTOR__id=did)|Q(date=date),DOCTOR__id=did).order_by('-id')
    # except:
    #     ob = appointment_table.objects.filter(DOCTOR__id=did).order_by('-id')
    #
    # # ob=appointment_table.objects.filter(DOCTOR__id=did)
    # obb = doctor_table.objects.filter(DEPARTMENT__HOSPITAL__LOGIN__id=request.session['lid'])
    # return render(request,'Hospital Administrator/manage appointment.html',{'val':ob,'val1':obb,'did':did,"dt":str(date)})

@login_required(login_url="/")
def dlt_app(request,id):
    ob=appointment_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>window.location="/mng_app#about"</script>''')

@login_required(login_url="/")
def edit_app(request,id):
    request.session['id'] = id
    ob=appointment_table.objects.get(id=id)
    dep=ob.DOCTOR.DEPARTMENT.id
    ob1=doctor_table.objects.filter(DEPARTMENT__id=dep)
    return render(request, 'Hospital Administrator/edit appointment.html', {'val': ob, 'val1': ob1,'dt':str(ob.date),'t':str(ob.time)})

@login_required(login_url="/")
def edit_app_action(request):
    app_obj = appointment_table.objects.get(id=request.session['id'])
    date = request.POST['textfield']
    time = request.POST['textfield2']
    doctor=request.POST['select1']
    app_obj.date = date
    app_obj.time = time
    app_obj.DOCTOR = doctor_table.objects.get(id=doctor)
    app_obj.save()
    return HttpResponse('''<script>window.location="/mng_app#about"</script>''')

@login_required(login_url="/")
def pat_reg(request):
    d=datetime.now().strftime("%Y-%m-%d")
    return render(request,'Hospital Administrator/patient registration.html',{"d":d})

@login_required(login_url="/")
def reg_code(request):
    try:
        ob=patient_table.objects.all().order_by("-id")
        hid=int(ob[0].health_id)+1
        fname=request.POST['textfield']
        lname=request.POST['textfield2']
        gender=request.POST['radiobutton']
        dob=request.POST['textfield3']
        place=request.POST['textfield4']
        pin=request.POST['textfield5']
        post=request.POST['textfield6']
        photo=request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(photo.name, photo)
        email = request.POST['textfield7']
        phone = request.POST['textfield8']
        username = request.POST['textfield9']
        password = request.POST['textfield10']
        ox = patient_table.objects.filter(email=email)
        if len(ox) == 0:
            ob=login_table()
            ob.username=username
            ob.password=password
            ob.type="patient"
            ob.save()
            pat_obj = patient_table()
            pat_obj.fname = fname
            pat_obj.lname=lname
            pat_obj.gender = gender
            pat_obj.dob = dob
            pat_obj.place = place
            pat_obj.pin = pin
            pat_obj.post = post
            pat_obj.phone = phone
            pat_obj.email = email
            pat_obj.photo=fsave
            pat_obj.health_id=hid
            pat_obj.LOGIN=ob
            pat_obj.save()
            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)
                gmail.ehlo()
                gmail.starttls()
                gmail.login('medisafea@gmail.com', 'ryhb ksnv gaem kbnz')
                print("login=======")
            except Exception as e:
                print("Couldn't setup email!!" + str(e))
            msg = MIMEText(str(pat_obj.health_id) + " is the Health ID in your Medisafe account. DO NOT SHARE this code with anyone")
            print(msg)
            msg['Subject'] = 'Medisafe'
            msg['To'] = email
            msg['From'] = 'medisafea@gmail.com'
            print("ok====")
            try:
                gmail.send_message(msg)
            except Exception as e:
                print(e,"=======================")
            return HttpResponse('''<script>alert('Successfully Registered');window.location='/hhome'</script>''')
        else:
            return HttpResponse('''<script>alert('This mail was alreday exist');window.location='/hhome'</script>''')


    except Exception as e:
        print(e)
        return ('''<script>alert('error');window.location='/hhome'</script>''')

@login_required(login_url="/")
def view_pat(request):
    return render(request,'Hospital Administrator/view patient for booking.html')

@login_required(login_url="/")
def view_pat_search(request):
    name=request.POST['textfield']
    try:
        ob=patient_table.objects.get(health_id__exact=name)
        print(ob,"")
        # for i in ob:
        ob.dob = int(datetime.now().strftime("%Y")) - int(str(ob.dob).split("-")[0])
        return render(request, 'Hospital Administrator/view patient for booking.html', {'val': ob, 'name': name,'ck':0})
    except Exception as e:
        return HttpResponse('''<script>alert('not found');window.location='/hhome'</script>''')



@login_required(login_url="/")
def add_app(request,pid):
    request.session["pateintid"]=pid
    ob=dept_table.objects.filter(HOSPITAL__LOGIN__id=request.session['lid'])
    ob1=doctor_table.objects.filter(DEPARTMENT__HOSPITAL__LOGIN__id=request.session['lid'])
    d = datetime.now().strftime("%Y-%m-%d")
    t=datetime.now().strftime("%H:%M")

    print("[[[[[",t)
    # Convert the time string to datetime object
    time_obj = datetime.strptime(t, "%H:%M")

    # Convert to 12-hour format and determine AM/PM
    time_12hr_str = time_obj.strftime('%I:%M %p')
    print(time_12hr_str,"12hrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
    # _______________
    #--------------------------
    current_date = datetime.now().date()

    # Add 3 months
    three_months_later = current_date + timedelta(days=3 * 30)  # Assuming a month is 30 days
    t=time_12hr_str.replace("PM","")
    print("", t)
    print("", current_date)
    print("", three_months_later)
    three_months_later=str(three_months_later).split(' ')[0]
    return render(request,'Hospital Administrator/add appointment.html',{'val':ob,'val1':ob1,'data':d,"t":t,"td":three_months_later})

@login_required(login_url="/")
def add_app_action(request):
    department = request.POST['select']
    doctor = request.POST['select1']
    date = request.POST['textfield2']
    time = request.POST['textfield22']
    ob=appointment_table.objects.filter(date=date,DOCTOR__id=doctor,PATIENT__id=request.session["pateintid"])
    print(ob)
    if len(ob)== 0:
        app_obj = appointment_table()
        app_obj.PATIENT_id = request.session["pateintid"]
        app_obj.DEPARTMENT = dept_table.objects.get(id=department)
        app_obj.DOCTOR = doctor_table.objects.get(id=doctor)
        app_obj.date = date
        app_obj.time = time
        app_obj.otp = 00
        app_obj.status = "pending"
        app_obj.save()
        return HttpResponse('''<script>window.location="/hhome#about"</script>''')
    else:
        return HttpResponse('''<script>alert("already booked");window.location="/hhome#about"</script>''')



def searchslot(request):
    print(request.POST,"jjjjjjjjjjjjjjjjjjjjjjjjjj")
    date=request.GET['date']
    doctor=request.GET['doc']
    slots=["10:00 AM - 10:15 AM","10:15 AM - 10:30 AM","10:30 AM - 10:45 AM","10:45 AM - 11:00 AM","11:00 AM - 11:15 AM","11:15 AM - 11:30 AM","11:30 AM - 11:45 AM","11:45 AM - 12:00 PM","12:00 PM - 12:15 PM","12:15 PM - 12:30 PM","12:30 PM - 12:45 PM","12:45 PM - 01:00 PM","01:00 PM - 01:15 PM","01:15 PM - 01:30 PM","02:00 PM - 02:15 PM","02:15 PM - 02:30 PM","02:30 PM - 02:45 PM","02:45 PM - 03:00 PM","03:00 PM - 03:15 PM","03:15 PM - 03:30 PM","03:30 PM - 03:45 PM","03:45 PM - 04:00 PM",]
    ob=appointment_table.objects.filter(DOCTOR__id=doctor,date=date)
    obs=[]
    for i in ob:
        obs.append(i.time)
    res=[]
    for i in slots:
        if i not in obs:
            res.append({"d":i})

    return JsonResponse(res,safe=False)

def seldoc(request):
    did = request.GET['did']
    doc=doctor_table.objects.filter(DEPARTMENT__id=did,DEPARTMENT__HOSPITAL__LOGIN__id=request.session['lid'],LOGIN__type="doctor")
    data=[]
    for i in doc:
        r={"id":i.id,"name":i.name}
        data.append(r)
    return JsonResponse(data,safe=False)



@login_required(login_url="/")
def dhome(request):
    a = doctor_table.objects.get(LOGIN__id=request.session['lid']).name
    return render(request,'Doctor/dindex.html',{'val':a})

@login_required(login_url="/")
def edit_dr_self(request):
    ok=dept_table.objects.all()
    ob = doctor_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request, 'Doctor/edit doctor self.html', {'val1':ob,'val2':ok,'dt':str(ob.dob)})

@login_required(login_url="/")
def edit_dr_action_self(request):
    try:
        dr_self_obj = doctor_table.objects.get(LOGIN__id=request.session['lid'])
        name = request.POST['textfield']
        gender = request.POST['radiobutton']
        dob = request.POST['textfield10']
        place = request.POST['textfield2']
        pin = request.POST['textfield22']
        post = request.POST['textfield23']
        phone = request.POST['textfield3']
        email = request.POST['textfield4']
        qualification = request.POST['textfield5']
        experience = request.POST['textfield6']
        specialization = request.POST['textfield7']
        department = request.POST['select']
        photo = request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(photo.name, photo)
        dr_self_obj.name = name
        dr_self_obj.gender = gender
        dr_self_obj.dob = dob
        dr_self_obj.place = place
        dr_self_obj.pin = pin
        dr_self_obj.post = post
        dr_self_obj.phone = phone
        dr_self_obj.email = email
        dr_self_obj.qualification = qualification
        dr_self_obj.experience = experience
        dr_self_obj.specialization = specialization
        dr_self_obj.DEPARTMENT = dept_table.objects.get(id=department)
        dr_self_obj.photo = fsave
        dr_self_obj.save()
        return HttpResponse('''<script>window.location="/dhome#about"</script>''')
    except:
        dr_self_obj = doctor_table.objects.get(LOGIN__id=request.session['lid'])
        name = request.POST['textfield']
        gender = request.POST['radiobutton']
        dob = request.POST['textfield10']
        place = request.POST['textfield2']
        pin = request.POST['textfield22']
        post = request.POST['textfield23']
        phone = request.POST['textfield3']
        email = request.POST['textfield4']
        qualification = request.POST['textfield5']
        experience = request.POST['textfield6']
        specialization = request.POST['textfield7']
        department = request.POST['select']
        # photo = request.FILES['file']
        # fs = FileSystemStorage()
        # fsave = fs.save(photo.name, photo)
        dr_self_obj.name = name
        dr_self_obj.gender = gender
        dr_self_obj.dob = dob
        dr_self_obj.place = place
        dr_self_obj.pin = pin
        dr_self_obj.post = post
        dr_self_obj.phone = phone
        dr_self_obj.email = email
        dr_self_obj.qualification = qualification
        dr_self_obj.experience = experience
        dr_self_obj.specialization = specialization
        dr_self_obj.DEPARTMENT = dept_table.objects.get(id=department)
        # dr_obj.photo = fsave
        dr_self_obj.save()
        return HttpResponse('''<script>window.location="/dhome"</script>''')

@login_required(login_url="/")
def view_appointment(request):
    ob = appointment_table.objects.filter(DOCTOR__LOGIN__id=request.session['lid'],status='accepted',date=datetime.today()).order_by('-id')
    return render(request,'Doctor/view appointment.html',{'val':ob})

@login_required(login_url="/")
def view_appointment_search(request):
    date=request.POST['textfield']
    month=request.POST['textfield2']
    try:
        ob = appointment_table.objects.filter(
         Q(DOCTOR__LOGIN__id=request.session['lid']) &   Q(status='accepted') & Q(date__month=month)).order_by('-id')
        return render(request, 'Doctor/view appointment.html', {'val': ob, "dt": str(date),"dm":month})
    except:
        ob = appointment_table.objects.filter(
            Q(DOCTOR__LOGIN__id=request.session['lid']) & Q(status='accepted') &
            Q(date=date) ).order_by('-id')
        return render(request, 'Doctor/view appointment.html', {'val': ob, "dt": str(date),"dm":month})

    return render(request,'Doctor/view appointment.html',{'val':ob,"dt":str(date),"dm":month})


@login_required(login_url="/")
def view_pat_dr(request,id,aid):
    ob = patient_table.objects.get(id=id)
    ob1 = appointment_table.objects.get(id=aid)
    request.session['pid']=id
    ob.dob = int(datetime.now().strftime("%Y")) - int(str(ob.dob).split("-")[0])
    kk=datetime.now().date()
    return render(request,'Doctor/view patient.html',{'val':ob,'date':ob1.date,'curdate':kk})

@login_required(login_url="/")
def view_prev_rec(request,id):
    request.session['uid']=id
    # ob =  medical_record_table.objects.filter(DOCTOR__LOGIN_id=request.session['lid'], PATIENT_id=request.session['pid'])
    data = []
    with open(
            r'C:\Users\nadha\PycharmProjects\patient_data_using_blockchain\node_modules\.bin\build\contracts\Structrecord.json') as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address='0xC5E6Cc39873b1a3e1971AD0541b99c1A813eeeC2', abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    for i in range(blocknumber, 4, -1):
        try:
            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            print(decoded_input[1],"********************************************")
            if str(decoded_input[1]['userid']) == str(id):
                data.append(decoded_input[1])
        except Exception as e:
            print(e)
            pass
    print(data, "==============================",id)
    res = []
    for k in data:
        # ob1 = patient_table.objects.get(id=k['userid'])
        try:
            ob2 = medical_record_table.objects.get(id=k['recordid'])
            row = {'date': k['date'], 'record': ob2.disease,"tname":ob2.test_name,"image":ob2.test_result.url,"trc":ob2.test_result_conclusion,"details":ob2.desc}
            res.append(row)
        except:
            pass
        # row={'needs':i.needs,'d_name':i.department.d_name,'amount':i.amount,'details':i.details,'date':i.date,'id':i.id,'amt':amnt}
    obc=dept_table.objects.all()
    return render(request,'Doctor/view previous medical.html', {'val': res,'v':obc})


@login_required(login_url="/")
def view_prev_rec1(request):
    id=request.session['uid']
    test = request.POST['textfield2']
    date = request.POST['textfield']
    department = request.POST['select']
    print(date, "++++++++++++++++++++")
    print(date, "++++++++++++++++++++")
    print(date, "++++++++++++++++++++")
    print(date, "++++++++++++++++++++")
    print(date, "++++++++++++++++++++")
    # ob =  medical_record_table.objects.filter(DOCTOR__LOGIN_id=request.session['lid'], PATIENT_id=request.session['pid'])
    data = []
    with open(
            r'C:\Users\nadha\PycharmProjects\patient_data_using_blockchain\node_modules\.bin\build\contracts\Structrecord.json') as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address='0xC5E6Cc39873b1a3e1971AD0541b99c1A813eeeC2', abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    for i in range(blocknumber, 4, -1):
        try:
            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            print(decoded_input[1],"********************************************")
            if str(decoded_input[1]['userid']) == str(id):
                data.append(decoded_input[1])
        except Exception as e:
            print(e)
            pass
    print(data, "==============================",id)
    res = []
    for k in data:
        # ob1 = patient_table.objects.get(id=k['userid'])
        if date=="":
            try:
                ob2 = medical_record_table.objects.get(id=k['recordid'],test_name__istartswith=test,DOCTOR__DEPARTMENT__dept_name__istartswith=department)
                row = {'date': k['date'], 'record': ob2.disease,"tname":ob2.test_name,"image":ob2.test_result.url,"trc":ob2.test_result_conclusion,"details":ob2.desc}
                res.append(row)
            except:
                pass
        else:
            try:
                ob2 = medical_record_table.objects.get(id=k['recordid'], test_name__istartswith=test,
                                                       DOCTOR__DEPARTMENT__dept_name__istartswith=department)
                print("=================",date,k['date'])
                if k['date']==date:
                    row = {'date': k['date'], 'record': ob2.disease, "tname": ob2.test_name, "image": ob2.test_result.url,
                           "trc": ob2.test_result_conclusion, "details": ob2.desc}
                    res.append(row)
            except Exception as e:
                print(e,"====================")
                pass
    # row={'needs':i.needs,'d_name':i.department.d_name,'amount':i.amount,'details':i.details,'date':i.date,'id':i.id,'amt':amnt}
    obc=dept_table.objects.all()
    return render(request,'Doctor/view previous medical.html', {'val': res,'v':obc,"dt":str(date),"d":department})


@login_required(login_url="/")
def prev_rec_search(request):
    obc=dept_table.objects.all()
    test=request.POST['textfield2']
    date=request.POST['textfield']
    department=request.POST['select']

    data = []
    with open(
            r'C:\Users\nadha\PycharmProjects\patient_data_using_blockchain\node_modules\.bin\build\contracts\Structrecord.json') as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address='0xC5E6Cc39873b1a3e1971AD0541b99c1A813eeeC2', abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    for i in range(blocknumber, 4, -1):
        try:
            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            # print(decoded_input[1],"********************************************")
            if str(decoded_input[1]['userid']) == str(request.session['uid']):
                data.append(decoded_input[1])
        except Exception as e:
            print(e)
            pass
    # print(data, "==============================",request.session['uid'])
    res = []
    # r1=[]
    # for k in data:
    #     r1.append(k['date'])
    # print(r1)
        # ob1 = patient_table.objects.get(id=k['userid'])
    try:
        ob2 = medical_record_table.objects.filter(Q(date=date)|Q(test_name__istartswith=test),Q(DOCTOR__DEPARTMENT__id=department),Q(DOCTOR__DEPARTMENT__id=department,test_name__istartswith=test,date=date))
    except:
        ob2 = medical_record_table.objects.filter(Q(test_name__istartswith=test),Q(DOCTOR__DEPARTMENT__id=department),Q(DOCTOR__DEPARTMENT__id=department,test_name__istartswith=test))

    for i in ob2:
        row = {'date': i.date, 'record': i.disease,"tname":i.test_name,"image":i.test_result.url,"trc":i.test_result_conclusion,"details":i.desc}
        res.append(row)
        # row={'needs':i.needs,'d_name':i.department.d_name,'amount':i.amount,'details':i.details,'date':i.date,'id':i.id,'amt':amnt}
    print(res, "==============================")

    return render(request,'Doctor/view previous medical.html', {'val': res,'v':obc,"dt":str(date)})


@login_required(login_url="/")
def add_record(request):
    return render(request, 'Doctor/add new medical record.html')

@login_required(login_url="/")
def add_record_action(request):
    btn=request.POST['Submit']
    if btn == "Add":
        disease = request.POST['textfield4']
        # duration = request.POST['textfield3']
        request.session['dis']=disease
        # request.session['dur']=duration
        test_name = request.POST['select']
        test_result = request.FILES['file']
        fn=FileSystemStorage()
        import datetime
        fs=fn.save(test_result.name,test_result)
        test_result_conclusion = request.POST['textfield2']
        desc = request.POST['textfield']
        record_obj = medical_record_table()
        record_obj.disease = disease
        # record_obj.duration = duration
        record_obj.test_name=test_name
        record_obj.test_result=fs
        record_obj.test_result_conclusion=test_result_conclusion
        record_obj.desc=desc
        record_obj.date=datetime.datetime.today()
        record_obj.DOCTOR = doctor_table.objects.get(LOGIN__id=request.session['lid'])
        record_obj.PATIENT = patient_table.objects.get(id=request.session['pid'])
        record_obj.save()
        with open(
                r'C:\Users\nadha\PycharmProjects\patient_data_using_blockchain\node_modules\.bin\build\contracts\Structrecord.json') as file:
            contract_json = json.load(file)  # load contract info as JSON
            contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
        contract = web3.eth.contract(address='0xC5E6Cc39873b1a3e1971AD0541b99c1A813eeeC2', abi=contract_abi)
        blocknumber = web3.eth.get_block_number()
        message2 = contract.functions.addrecord(blocknumber + 1, str(record_obj.id), str(request.session['pid']),
                                              str(datetime.datetime.now().strftime("%Y-%m-%d")), str(disease+"#"+test_name+"#"+fs+"#"+
                                    test_result_conclusion+"#"+desc)).transact()
        return redirect('/add_record')
    else:
        disease = request.POST['textfield4']
        # duration = request.POST['textfield3']
        test_name = request.POST['select']
        test_result = request.FILES['file']
        fn = FileSystemStorage()
        import datetime
        fs = fn.save(test_result.name, test_result)
        test_result_conclusion = request.POST['textfield2']
        desc = request.POST['textfield']
        record_obj = medical_record_table()
        record_obj.disease = disease
        # record_obj.duration = duration
        record_obj.test_name = test_name
        record_obj.test_result = fs
        record_obj.test_result_conclusion = test_result_conclusion
        record_obj.desc = desc
        record_obj.date = datetime.datetime.today()
        record_obj.DOCTOR = doctor_table.objects.get(LOGIN__id=request.session['lid'])
        record_obj.PATIENT = patient_table.objects.get(id=request.session['pid'])
        record_obj.save()
        with open(
                r'C:\Users\nadha\PycharmProjects\patient_data_using_blockchain\node_modules\.bin\build\contracts\Structrecord.json') as file:
            contract_json = json.load(file)  # load contract info as JSON
            contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
        contract = web3.eth.contract(address='0xC5E6Cc39873b1a3e1971AD0541b99c1A813eeeC2', abi=contract_abi)
        blocknumber = web3.eth.get_block_number()
        message2 = contract.functions.addrecord(blocknumber + 1, str(record_obj.id), str(request.session['pid']),
                                                str(datetime.datetime.now().strftime("%Y-%m-%d")),
                                                str(disease + "#" + test_name + "#" + fs + "#" +
                                                    test_result_conclusion + "#" + desc)).transact()
        request.session['dis'] = ''
        request.session['dur'] = ''
        return HttpResponse('''<script>alert("completed!");window.location="/dhome"</script>''')



##############################  android   #################################


def and_logincode(request):
  uname=request.POST['uname']
  pwd=request.POST['pass']
  try:
        ob=login_table.objects.get(username__exact=uname,password__exact=pwd)
        if (ob.username != uname or ob.password != pwd):
            data = {"task": "invalid"}
            r = json.dumps(data)
            return HttpResponse(r)


        else:
            if ob is not None:
                data={"task":"valid","lid":ob.id}
                r=json.dumps(data)
                return HttpResponse(r)
            else:
                data = {"task": "invalid"}
                r = json.dumps(data)
                return HttpResponse(r)
  except Exception as e:
      print(e)
      data = {"task": "invalid"}
      r = json.dumps(data)
      return HttpResponse(r)

def and_reg_code(request):
    ob = patient_table.objects.all().order_by("-id")
    hid = int(ob[0].health_id) + 1
    fname=request.POST['Fname']
    lname=request.POST['Lname']
    gender=request.POST['gender']
    dob=request.POST['dob']
    place=request.POST['place']
    pin=request.POST['pin']
    post=request.POST['post']
    photo=request.FILES['file']
    fs = FileSystemStorage()
    fsave = fs.save(photo.name, photo)
    email = request.POST['email_id']
    phone = request.POST['phone_number']
    username = request.POST['username']
    password = request.POST['password']
    ox = patient_table.objects.filter(email=email)
    if len(ox) == 0:
        ob=login_table()
        ob.username=username
        ob.password=password
        ob.type="patient"
        ob.save()
        pat_obj = patient_table()
        pat_obj.fname = fname
        pat_obj.lname=lname
        pat_obj.gender = gender
        pat_obj.dob = dob
        pat_obj.place = place
        pat_obj.pin = pin
        pat_obj.post = post
        pat_obj.phone = phone
        pat_obj.email = email
        pat_obj.photo=fsave
        pat_obj.health_id = hid
        pat_obj.LOGIN=ob
        pat_obj.save()
        # healthid = request.POST['healthid']
        # obb = patient_table.objects.get(health_id=healthid)
        #
        # if obb is None:
        #     return JsonResponse({'task': "invalid"})
        # else:
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('medisafea@gmail.com', 'ryhb ksnv gaem kbnz')
            print("login=======")
        except Exception as e:
            print("Couldn't setup email!!" + str(e))
        msg = MIMEText(str(pat_obj.health_id) + " is the Health ID in your Medisafe account. DO NOT SHARE this code with anyone ")
        print(msg)
        msg['Subject'] = 'Medisafe'
        msg['To'] = email
        msg['From'] = 'medisafea@gmail.com'
        print("ok====")
        try:
            gmail.send_message(msg)
            data = {"task": "valid"}
            r = json.dumps(data)
            return HttpResponse(r)
        except Exception as e:
            data = {"task": "invalid data"}
            r = json.dumps(data)
            return HttpResponse(r)
    else:
        data = {"task": "This mail was already exist"}
        r = json.dumps(data)
        return HttpResponse(r)







def forgotpasss(request):
    email=request.POST['uname']
    obb=patient_table.objects.get(email=email)
    if obb is None:
        return JsonResponse({'task':"invalid"})
    else:
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('medisafea@gmail.com', 'ryhb ksnv gaem kbnz')
            print("login=======")
        except Exception as e:
            print("Couldn't setup email!!" + str(e))
        msg = MIMEText( str(obb.LOGIN.password) + " Is the forgotted password in Medisafe account " )
        print(msg)
        msg['Subject'] = 'Medisafe'
        msg['To'] = email
        msg['From'] = 'medisafea@gmail.com'

        print("ok====")

        try:
            gmail.send_message(msg)
            data = {"task": "valid"}
            r = json.dumps(data)
            return HttpResponse(r)
        except Exception as e:
            pass
            data = {"task": "valid"}
            r = json.dumps(data)
            return HttpResponse(r)

    data = {"task": "invalid"}
    r = json.dumps(data)
    return HttpResponse(r)



def and_viewappointment(request):
    lid=request.POST['lid']
    ob=appointment_table.objects.filter(PATIENT__LOGIN__id=lid).order_by('-id')
    d=[]
    t = datetime.now().strftime("%H:%M")

    print("[[[[[", t)
    # Convert the time string to datetime object
    time_obj = datetime.strptime(t, "%H:%M")

    # Convert to 12-hour format and determine AM/PM
    time_12hr_str = time_obj.strftime('%I:%M %p')
    print(time_12hr_str, "12hrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")


    for i in ob:
        obtime=i.time
        x=obtime.split("-")
        print(x[1],"kkkkkkkkkkkkkkkkkkkkkkkkkkkk")
        obb=appointment_table.objects.filter(date__gte=datetime.today(),id=i.id)
        obb1 =appointment_table.objects.filter(date=datetime.today(),id=i.id)
        obb = appointment_table.objects.filter(date__gte=datetime.today(), id=i.id)
        if len(obb)>0:
            if len(obb1)==0:
                data={"aid":i.id,"hospital":i.DOCTOR.DEPARTMENT.HOSPITAL.hosp_name,"department":i.DOCTOR.DEPARTMENT.dept_name,"doctor":i.DOCTOR.name,"date":str(i.date),"time":i.time,"status":i.status,"r":"yes"}
            else:
                t=i.time.split("- ")[1]
                time_obj1 = datetime.strptime(t, '%I:%M %p')
                if time_obj1>time_obj:
                    data = {"aid": i.id, "hospital": i.DOCTOR.DEPARTMENT.HOSPITAL.hosp_name,
                            "department": i.DOCTOR.DEPARTMENT.dept_name, "doctor": i.DOCTOR.name, "date": str(i.date),
                            "time": i.time, "status": i.status, "r": "yes"}
                else:
                    data = {"aid": i.id, "hospital": i.DOCTOR.DEPARTMENT.HOSPITAL.hosp_name,
                            "department": i.DOCTOR.DEPARTMENT.dept_name, "doctor": i.DOCTOR.name, "date": str(i.date),
                            "time": i.time, "status": i.status, "r": "no"}


        else:
            data={"aid":i.id,"hospital":i.DOCTOR.DEPARTMENT.HOSPITAL.hosp_name,"department":i.DOCTOR.DEPARTMENT.dept_name,"doctor":i.DOCTOR.name,"date":str(i.date),"time":i.time,"status":i.status,"r":"no"}

        d.append(data)
    r=json.dumps(d)
    return HttpResponse(r)


def verifyotp(request):
    lid=request.POST['lid']
    aid=request.POST['aid']
    obb=patient_table.objects.get(LOGIN__id=lid)
    email=obb.email
    import random
    otp = random.randint(0000, 9999)
    ob=appointment_table.objects.get(id=aid)
    ob.otp=otp
    ob.save()
    if obb is None:
        return JsonResponse({'task':"invalid"})
    else:
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('medisafea@gmail.com', 'ryhb ksnv gaem kbnz')
            print("login=======")
        except Exception as e:
            print("Couldn't setup email!!" + str(e))
        msg = MIMEText(  str(otp) + "  is your one time password (OTP) for appointment confirmation and record access in Medisafe . Please enter OTP to proceed " )
        print(msg)
        msg['Subject'] = 'Medisafe'
        msg['To'] = email
        msg['From'] = 'medisafea@gmail.com'

        print("ok====")

        try:
            gmail.send_message(msg)
            data = {"task": "valid","otp":otp}
            r = json.dumps(data)
            return HttpResponse(r)
        except Exception as e:
            print(e)
            pass
            data = {"task": "valid"}
            r = json.dumps(data)
            return HttpResponse(r)

    data = {"task": "invalid"}
    r = json.dumps(data)
    return HttpResponse(r)




def accept_booking(request):
    aid=request.POST['aid']
    otp=request.POST['otp']
    print(otp,"")
    ob=appointment_table.objects.get(id=aid)
    print(ob.otp,"kkkkkkkkkkk")
    otpp=ob.otp
    if(otp == str(otpp)):
        ob.status="accepted"
        ob.save()
        data = {"task": "valid"}
        r = json.dumps(data)
        return HttpResponse(r)
    else:
        ob.status = "cancelled"
        ob.save()
        data = {"task": "invalid"}
        r = json.dumps(data)
        return HttpResponse(r)

def view_prev_rec_and(request):
    id=request.POST['uid']
    print(id,"===============================")
    ob=patient_table.objects.get(LOGIN__id=id)
    # ob =  medical_record_table.objects.filter(DOCTOR__LOGIN_id=request.session['lid'], PATIENT_id=request.session['pid'])
    data = []
    with open(
            r'C:\Users\nadha\PycharmProjects\patient_data_using_blockchain\node_modules\.bin\build\contracts\Structrecord.json') as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address='0xC5E6Cc39873b1a3e1971AD0541b99c1A813eeeC2', abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    for i in range(blocknumber, 20, -1):
        try:
            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            if str(decoded_input[1]['userid']) == str(ob.id):
                data.append(decoded_input[1])
        except Exception as e:
            print(e)
            pass
    print(data, "==============================",id)
    res = []
    for k in data:
        # ob1 = patient_table.objects.get(id=k['userid'])
        ob2 = medical_record_table.objects.get(id=k['recordid'])
        row = {'date': str(ob2.date), 'record': ob2.disease,"tname":ob2.test_name,"image":str(ob2.test_result),"trc":ob2.test_result_conclusion,"details":ob2.desc}
        res.append(row)
    print(res,"------------------------------------")
        # row={'needs':i.needs,'d_name':i.department.d_name,'amount':i.amount,'details':i.details,'date':i.date,'id':i.id,'amt':amnt}
    # obc=dept_table.objects.all()
    return JsonResponse(res,safe=False)


def prev_rec_search_andnew(request):
    uid=request.POST['uid']
    uob=patient_table.objects.get(LOGIN__id=uid)
    uid=uob.id
    # print(test,date,"=========================")
    data = []
    with open(
            r'C:\Users\nadha\PycharmProjects\patient_data_using_blockchain\node_modules\.bin\build\contracts\Structrecord.json') as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address='0xC5E6Cc39873b1a3e1971AD0541b99c1A813eeeC2', abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    r=[]
    for i in range(blocknumber, 4, -1):
        try:
            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            print(decoded_input[1],"")
            if str(decoded_input[1]['userid']) == str(uid):
                data.append(decoded_input[1])
                r.append(decoded_input[1]['recordid'])
        except Exception as e:
            print(e)
            pass
    print(data, "*********************************************************************")
    res = []
    # r1=[]
    # for k in data:
    #     res.append(k['date'])
    # print(r1)
        # ob1 = patient_table.objects.get(id=k['userid'])
    print(r)
    ob2 = medical_record_table.objects.filter(id__in=r)
    # ob2 = medical_record_table.objects.filter(PATIENT__id=str(decoded_input[1]['userid']))
    for i in ob2:
        row = {'date': i.date, 'record': i.disease,"tname":i.test_name,"image":i.test_result.url,"trc":i.test_result_conclusion,"details":i.desc}
        res.append(row)
        # row={'needs':i.needs,'d_name':i.department.d_name,'amount':i.amount,'details':i.details,'date':i.date,'id':i.id,'amt':amnt}
    print(res, "==============================")
    return JsonResponse(res,safe=False)

def prev_rec_search_and(request):
    # obc=dept_table.objects.all()
    test=request.POST['textfield2']
    date=request.POST['textfield']
    uid=request.POST['uid']
    # uob=patient_table.objects.get(LOGIN__id=uid)
    print(test,date,"=========================")
    data = []
    with open(
            r'C:\Users\nadha\PycharmProjects\patient_data_using_blockchain\node_modules\.bin\build\contracts\Structrecord.json') as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address='0xC5E6Cc39873b1a3e1971AD0541b99c1A813eeeC2', abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    for i in range(blocknumber, 4, -1):
        try:
            a = web3.eth.get_transaction_by_block(i, 0)
            decoded_input = contract.decode_function_input(a['input'])
            print(decoded_input[1],"********************************************")
            if str(decoded_input[1]['userid']) == uid:
                data.append(decoded_input[1])
        except Exception as e:
            print(e)
            pass
    print(data, "==============================")
    res = []
    # r1=[]
    # for k in data:
    #     r1.append(k['date'])
    # print(r1)
        # ob1 = patient_table.objects.get(id=k['userid'])
    try:
        if test == "select":
            ob2 = medical_record_table.objects.filter(date=date)
        else:
            ob2 = medical_record_table.objects.filter(PATIENT__id=str(decoded_input[1]['userid']),test_name__istartswith=test,date=date)
    except:
            ob2 = medical_record_table.objects.filter(PATIENT__id=str(decoded_input[1]['userid']),test_name__istartswith=test)
    for i in ob2:
        row = {'date': i.date, 'record': i.disease,"tname":i.test_name,"image":i.test_result.url,"trc":i.test_result_conclusion,"details":i.desc}
        res.append(row)
        # row={'needs':i.needs,'d_name':i.department.d_name,'amount':i.amount,'details':i.details,'date':i.date,'id':i.id,'amt':amnt}
    print(res, "==============================")
    return JsonResponse(res,safe=False)


def and_update_profile(request):
    if "file" in request.FILES:
        ob = patient_table.objects.all().order_by("-id")
        hid = int(ob[0].health_id) + 1
        fname=request.POST['Fname']
        lname=request.POST['Lname']
        gender=request.POST['gender']
        dob=request.POST['dob']
        place=request.POST['place']
        pin=request.POST['pin']
        post=request.POST['post']
        photo=request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(photo.name, photo)
        email = request.POST['email_id']
        phone = request.POST['phone_number']
        lid = request.POST['lid']
        pat_obj = patient_table.objects.get(LOGIN__id=lid)
        pat_obj.fname = fname
        pat_obj.lname=lname
        pat_obj.gender = gender
        pat_obj.dob = dob
        pat_obj.place = place
        pat_obj.pin = pin
        pat_obj.post = post
        pat_obj.phone = phone
        pat_obj.email = email
        pat_obj.photo=fsave
        pat_obj.health_id = hid
        pat_obj.save()
        data = {"task": "valid"}
        r = json.dumps(data)
        return HttpResponse(r)
    else:
        ob = patient_table.objects.all().order_by("-id")
        hid = int(ob[0].health_id) + 1
        fname=request.POST['Fname']
        lname=request.POST['Lname']
        gender=request.POST['gender']
        dob=request.POST['dob']
        place=request.POST['place']
        pin=request.POST['pin']
        post=request.POST['post']
        # photo=request.FILES['file']
        # fs = FileSystemStorage()
        # fsave = fs.save(photo.name, photo)
        email = request.POST['email_id']
        phone = request.POST['phone_number']
        lid = request.POST['lid']
        pat_obj = patient_table.objects.get(LOGIN__id=lid)
        pat_obj.fname = fname
        pat_obj.lname=lname
        pat_obj.gender = gender
        pat_obj.dob = dob
        pat_obj.place = place
        pat_obj.pin = pin
        pat_obj.post = post
        pat_obj.phone = phone
        pat_obj.email = email
        # pat_obj.photo=fsave
        pat_obj.health_id = hid
        pat_obj.save()
        data = {"task": "valid"}
        r = json.dumps(data)
        return HttpResponse(r)

    #     data = {"task": "invalid"}
    #     r = json.dumps(data)
    #     return HttpResponse(r)




def viewprofile(request):
    lid=request.POST['lid']
    ob=patient_table.objects.filter(LOGIN__id=lid)
    d=[]
    for i in ob:
        data={"fname":i.fname,"lname":i.lname,"gender":i.gender,"dob":str(i.dob),"place":i.place,"pin":i.pin,"post":i.post,'phone':i.phone,'email':i.email,'photo':str(i.photo.url),'id':i.id}
        d.append(data)
    r=json.dumps(d)
    print("^^^^^^^^^^^^^^^", r)
    return HttpResponse(r)