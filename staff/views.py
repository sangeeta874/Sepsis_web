from django.shortcuts import render
from .forms import TestReportForms
from .models import TestReport
import pyrebase
from django.contrib import auth

config = {
   'apiKey': "AIzaSyC6jNBg8QlyHA3cLH0w0TeJzObkslzdpzE",
   'authDomain': "patient-da06d.firebaseapp.com",
   'databaseURL': "https://patient-da06d.firebaseio.com",
   'projectId': "patient-da06d",
   'storageBucket': "patient-da06d.appspot.com",
   'messagingSenderId': "60282937045",
}
firebase = pyrebase.initialize_app(config);
authe = firebase.auth()
database=firebase.database()
def test(request):
    if request.method=='POST':
        form=TestReportForms(request.POST)
        if form.is_valid():
            obj=form.save()
            print(form.cleaned_data)
            Age=form.cleaned_data.get('Age')
            SBP=form.cleaned_data.get('SBP')
            DBP=form.cleaned_data.get('DBP')
            Resp=form.cleaned_data.get('Resp')
            Temp=form.cleaned_data.get('Temp')
            O2Sat=form.cleaned_data.get('O2Sat')
            HR=form.cleaned_data.get('HR')
            MAP=(((2*float(DBP))+float(SBP))/3)
            obj.MAP=(((2*float(DBP))+float(SBP))/3)
            obj.save()
            data = {
                     "Age":Age,
                     'SBP':SBP,
                     'DBP':DBP,
                     'MAP':MAP,
                    'O2Sat':O2Sat,
                     'HR':HR,
                     'Temp':Temp,
                     'Resp':Resp
                    }
            database.child('SIRS').child('name').set(data)
            
    form=TestReportForms()
    return render(request,"test.html",{"form":form})
def sign(request):
    return render(request,"docsignIn.html")
def postsign(request):
    email=request.POST.get('email')
    password=request.POST.get('password')

    try:
        staff = authe.sign_in_with_email_and_password(email,password)
    except:
        message = "invalid cerediantials"
        return render(request,"docsignIn.html",{"msg":message})
    print(staff['idToken'])
    session_id=staff['idToken']
    request.session['uid']=str(session_id)
    idtoken= request.session['uid']
    uid = staff['localId']
   # name = database.child('users').child('details').child(uid).child('name').get().val()
    return render(request, "docwelcome.html")   
def logout(request):
    auth.logout(request)
    return render(request,'docsignIn.html')
def signUp(request):
    return render(request,"docsignup.html") 
def postsignup(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    password=request.POST.get('password')
    empno=request.POST.get('empno')
    password1=request.POST.get('password1')
    if password==password1 :
       try:
         staff=authe.create_user_with_email_and_password(email,password)
         uid = staff['localId']
         data={"name":name,"username":email,"password":password,"empno":empno}
         database.child('staff').child("details").set(data)
       except:
         message="Unable to create account try again"
         return render(request,"docsignup.html",{"msg":message})
    else :
        message="Password did not match"
        return render(request,"docsignup.html",{"msg":message})     
    return render(request,"docsignIn.html")


    