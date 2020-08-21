from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect,reverse
from django.contrib.auth import authenticate,get_user_model
# Create your views here.
import psycopg2
import hashlib
import uuid
import time

MyUser = get_user_model()

def my_md5(password):
    result = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
    return result

def getData(sql):
    conn = psycopg2.connect(database="djangodata", user="test", password="test..2020", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def loginView(request):
    if request.method == 'GET':
        return render(request,'login.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        password_md5 = my_md5(password)
        user = MyUser.objects.get(username=username,password=password,email=email)
        

        if user is not None and user.role == 'Normal':
            return redirect(
                    reverse('userSystem:HomePage',kwargs={'username':username,'password':password_md5})
                )
                        
        
        elif user is not None and user.role == 'Administrator':
            return redirect(
                reverse('userSystem:AdminHomePage',kwargs={'username':username,'password':password_md5})
                )
        
        elif MyUser.objects.get(username=username) is None:
            return render(request,
                        'login.html',
                        context={'error_message0':'The username is error !'}
                        )

        elif MyUser.objects.get(email=email) is None:
            return render(request,
                        'login.html',
                        context={'error_message1':'The email is error !'}
                        )

        elif MyUser.objects.get(password=password) is None:
            return render(request,
                        'login.html',
                        context={'error_message2':'The password is error !'}
                        )



        else:
            return render(request,
                        'login.html',
                        context={'error_message3':'This user is not exists!Please register it!'}
                        )

def registerView(request):
    if request.method == 'GET':
        return render(request,'register.html')
    if request.method == 'POST':

        #avatar = request.POST.get('avatar')
        username = request.POST.get('username')
        birth = request.POST.get('birth')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        address = request.POST.get('address')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        

        try:
            check_user = MyUser.objects.get(username=username,email=email)
            if check_user:
                return redirect(reverse('login'))        
        except Exception as e:
            pass
        

        user = MyUser()
        if password1 == password2:
            #user.avatar = avatar
            user.username = username
            user.userid = uuid.uuid3(uuid.NAMESPACE_DNS,username+email)            
            user.password = password1
            user.email = email
            user.date_of_birth = birth
            user.gender = gender
            user.mobile = mobile
            user.address = address
            user.save()
            return redirect(reverse('login'))
        else:
            
            return render(request,'register.html',context={'error_message0':'Password2 is different with Password1 !'})


def HomePageView(request,username,password):
    #url_ = reverse('HomePage',kwargs={'username':username,'password':password})
    #return redirect(url_)
    return render(request,'HomePage.html',context={'username':username,'password':password})

def AdminHomePageView(request,username,password):
    #url_ = reverse('AdminHomePage',kwargs={'username':username,'password':password})
    #return redirect(url_)  
    return render(request,'AdminHomePage.html',context={'username':username,'password':password})

def DocumentManagementView(request, username, password):
    return render(request,'documentManagement.html',context={'username':username,'password':password})
        