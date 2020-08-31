from django.shortcuts import render

# Create your views here.
def register(request):
	if request.method =="POST":
		data = {}
		fname = request.POST['fname']
		lname = request.POST['lname']
		data['fname'] = fname
		data['lname'] = lname
		return render(request, 'student/data.html',  data)
	return render(request, 'student/register.html')