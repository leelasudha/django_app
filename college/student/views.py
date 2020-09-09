from django.shortcuts import render, redirect
from .models import Student, LoginUser
from django.http import HttpResponse
# Create your views here.
def register(request):
	if request.method =="POST":
		data = {}
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		age = request.POST.get('age')
		email = request.POST.get('email')
		branch = request.POST.get('department')
		data['fname'] = fname
		data['lname'] = lname
		obj = Student(First_name= fname, Last_name=lname, Branch= branch, Age=age, Email=email)
		obj.save()
		#return render(request, 'student/data.html',  data)
		return HttpResponse('Student added successfuly')
	return render(request, 'student/register.html')
def show(request):
	obj = Student.objects.all()
	return render(request, 'student/data.html',{'data':obj})

def edit(request, id):
	data = Student.objects.get(id = id)
	print(data.First_name)
	if(request.method =="POST"):
		data.First_name = request.POST.get('fname')
		data.Last_name = request.POST.get('lname')
		data.Branch = request.POST.get('branch')
		data.Email = request.POST.get('email')
		data.Age =request.POST.get('age')
		data.save()
		return redirect('show')
	return render(request, 'student/edit.html', {'data':data})
def delete(request, id):
	data = Student.objects.get(id = id)
	return render(request, 'student/delete.html', {'data': data})

def confirm(request, id):
	data = Student.objects.get(id=id)
	data.delete()
	return redirect('show')
def login(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		#data = LoginUser.objects.get(username= username, password=password)
		data = LoginUser.objects.all.filter(username= username, password=password)
		if data:
			return render(request, 'student/welcome.html', {'user':username})
		else:
			return HttpResponse('No such User')
	return render(request,'student/login.html')

def forgotpwd(request):
	if request.method=='POST':
		email=request.POST['email']
		data = LoginUser.objects.get(email=email)
		sub = "regarding to password"
		body = "Your username : " + data.username + "Your password:  "+ data.password
		sender = settings.EMAIL_HOST_USER
		receiver = email
		e = EmailMessage(sub, body, sender, [receiver])
		e.send()
		return HttpResponse('Check your mail for password')
	return render(request, 'student/forgotpwd.html')

def changepwd(request):
	if request.method == 'POST':
		oldpass = request.POST['oldpass']
		newpass = request.POST['newpass']
		confirmpwd = request.POST['confirmpwd']
		data = LoginUser.objects.get(password=oldpass)
		if newpass != confirmpwd:
			return HttpResponse("Passwords doesn't Match")
		else:
			data.password = confirmpwd
			data.save()
			return HttpResponse("Your password is updated")
	return render(request, 'student/changepwd.html')