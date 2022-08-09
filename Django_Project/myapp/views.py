from django.shortcuts import render,redirect
from .models import Contact,User
# Create your views here.
def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	if request.method=="POST":
		Contact.objects.create(
			name=request.POST['name'],
			email=request.POST['email'],
			mobile=request.POST['mobile'],
			remarks=request.POST['remarks']
			)
		msg="Contact Saved Successfully"
		contacts=Contact.objects.all().order_by('-id')
		return render(request,'contact.html',{'msg':msg,'contacts':contacts})
	else:
		contacts=Contact.objects.all().order_by('-id') 
		return render(request,'contact.html',{'contacts':contacts})

def signup(request):
	if request.method=="POST":
		try:
			User.objects.get(email=request.POST['email'])
			msg="Email Already Registered"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						address=request.POST['address'],
						gender=request.POST['gender'],
						password=request.POST['password'],
						profile_pic=request.FILES['profile_pic'],
					)
				msg="User Sign Up Successfully"
				return render(request,'login.html',{'msg':msg})
			else:
				msg="Password & Confirm Password Does Not Matched"
				return render(request,'signup.html',{'msg':msg})
	else:
			return render(request,'signup.html')	

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(
					email=request.POST['email'],
					password=request.POST['password']
				)
			request.session['email']=user.email
			request.session['fname']=user.fname
			request.session['profile_pic']=user.profile_pic.url
			return render(request,'index.html')
		except:
			msg="Email & Password Is Incorrect"
			return render(request,'login.html',{'msg':msg})  
	else:	
		return render(request,'login.html')	

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		return render(request,'login.html')
	except:
		return render(request,'login.html')

def change_password(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])
		if user.password==request.POST['old_password']:
			if request.POST['new_password']==request.POST['cnew_password']:
				user.password=request.POST['new_password']
				user.save()
				return redirect('logout')
			else:
				msg="New Password & Confirm New Password Does Not Matched"
				return render(request,'change_password.html',{'msg':msg})
		else:
			msg="Old Password Does Not Matched"
			return render(request,'change_password.html',{'msg':msg})
	else:	
		return render(request,'change_password.html')

def profile(request):
	user=User.objects.get(email=request.session['email']) 
	return render(request,'profile.html',{'user':user}) 