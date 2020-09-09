from django.shortcuts import render, redirect
from .models import Faculty
from django.http import HttpResponse
# Create your views here.
def register(request):
	if request.method =="POST":
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		age = request.POST.get('age')
		email = request.POST.get('email')
		department = request.POST.get('department')
		mobile = request.POST.get('mobile')
		date = request.POST.get('date')
		qualification = request.POST.get('qualification')
		obj = Faculty(First_name= fname, Last_name=lname, Age=age, Email=email, Department= department,
			Join_Date= date, mobile= mobile, qualification=qualification)
		obj.save()
		#return render(request, 'student/data.html',  data)
		return HttpResponse('Faculty added successfuly')
	return render(request, 'faculty/register.html')
def show(request):
	obj = Faculty.objects.all()
	return render(request, 'faculty/data.html',{'data':obj})
def edit(request,id):
	obj = Faculty.objects.get(id= id)
	if request.method=="POST":
		obj.First_name = request.POST.get('fname')
		obj.Last_name = request.POST.get('lname')
		obj.Age = request.POST.get('age')
		obj.Email = request.POST.get('email')
		obj.Department = request.POST.get('department')
		obj.mobile = request.POST.get('mobile')
		obj.Join_Date = request.POST.get('date')
		obj.qualification = request.POST.get('qualification')
		obj.save()
		return redirect('showFaculty')
	return render(request, 'faculty/edit.html', {'data':obj})
def delete(request, id):
	obj = Faculty.objects.get(id=id)
	return render(request, 'faculty/delete.html', {'data' : obj})
def confirm(request, id):
	data = Faculty.objects.get(id=id)
	data.delete()
	return redirect('showFaculty')
