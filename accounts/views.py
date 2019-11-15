from django.shortcuts import render, redirect
from django.contrib.auth.models import User,AbstractUser
from app.models import CustomUser
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.
def register(request):

	if request.method == 'POST':
		 first_name = request.POST['first_name']
		 last_name = request.POST['last_name']
		 username = request.POST['username']
		 password1 = request.POST['password1']
		 password2 = request.POST['password2']
		 email = request.POST['email']
		 gender = request.POST['gender']
		 user_type = request.POST['user_type']
		 mobile_no = request.POST['mobile_no']

		 if password1==password2:
		 	user =CustomUser.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name,gender=gender,user_type=user_type,mobile_no=mobile_no)
		 	user.save()
		 	return redirect('/')
	else:
		return render(request, 'register.html')

def login(request):
	if request.method == 'POST':
		 user = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))
		 if user is not None:
		 	auth_login(request, user)
		 	return redirect('index')
		 else:
		 	return render(request, 'login.html', {'error':'Username or Password is wrong'})
	else:
		return render(request, 'login.html')


def logout(request):
	# if request.method == 'POST':
		auth.logout(request)
		return redirect('index')

