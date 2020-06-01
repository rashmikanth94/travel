from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.
def login(request):
	return render(request,"login.html")


def register(request):

	if request.method =='POST':
		first_name= request.POST['first_name']
		last_name= request.POST['last_name']
		pass1= request.POST['password1']
		pass2= request.POST['password2']
		username= request.POST['username']
		email= request.POST['email']

		if pass1==pass2:
			if User.objects.filter(username=username).exists():
				error="The username was already used! please try another username"
				return render(request,"register.html",{'error':error})

			elif User.objects.filter(email=email).exists():
				error="email id exist! please try with another account!!!"
				return render(request,"register.html",{'error':error})

			else:
				user=User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=pass1)
				user.save()
				print("user created")
				return redirect('login')
		else:
			error="password doesnt match"
			return render(request,"register.html",{'error':error})
	else:
		return render(request,"register.html")

def login(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']

		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			error="enter valid username or password"
			return render(request,'login.html',{'error':error})
	else:

		return render(request,'login.html')
def logout(request):
	auth.logout(request)
	return redirect('/')