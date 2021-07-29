from django.shortcuts import render
import pyrebase
from django.contrib import auth
import time
from datetime import datetime, timezone
import pytz
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
def sign(request):
    return render(request,"signIn.html")
def postsign(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    try:
        user= authe.sign_in_with_email_and_password(email,password)
    except:
        message = "invalid cerediantials"
        return render(request,"signIn.html",{"msg":message})
    print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    idtoken= request.session['uid']
    uid = user['localId']
    nam = database.child('users').child('details').child(uid).child('name').get().val()
    a = database.child('SIRS').child('name').child('age').get().val()
    b = database.child('SIRS').child('name').child('SBP').get().val()
    c = database.child('SIRS').child('name').child('DBP').get().val()
    d = database.child('SIRS').child('name').child('Resp').get().val()
    e = database.child('SIRS').child('name').child('Temp').get().val()
    f = database.child('SIRS').child('name').child('O2Sat').get().val()
    return render(request, "welcome.html",{"a":a,"b":b,"c":c,"d":d,"e":e,"f":f ,"n":nam})   
def logout(request):
    auth.logout(request)
    return render(request,'signIn.html')
def signUp(request):
    return render(request,"signup.html") 
def postsignup(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    number=request.POST.get('number')
    gender=request.POST.get('gender')
    password=request.POST.get('password')
    try:
       user=authe.create_user_with_email_and_password(email,password)
       uid = user['localId']
       data={"name":name,"email":email,"number":number,"gender":gender,"status":"1"}
       database.child('users').child("details").child(uid).set(data)
    except:
       message="Unable to create account try again"
       return render(request,"signup.html",{"msg":message})
    return render(request,"signIn.html")

