from django.shortcuts import render,redirect
from .forms import UserRegisterForm

def Home(request):
	return render(request, 'sport/home.html')


def Register(request):
	if request.method=='POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid:
			form.save()
			return redirect('home')
	else:
		form = UserRegisterForm()
	return render(request, 'sport/register.html', {'form':form})	

def Banku(request):
	return render(request, 'sport/banku.html')		

def Wakye(request):
	return render(request, 'sport/wakye.html')	

def Fufu(request):
	return render(request, 'sport/fufu.html')	

def Gob3(request):
	return render(request, 'sport/gob3.html')	


def CardDetail(request):
	return render(request, 'sport/card_detail.html')		