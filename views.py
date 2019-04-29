from django.shortcuts import render
from .models import customer

# Create your views here
def Home(request):
	return render(request,'Bosche/home.html')
def About(request):
	return render(request,'Bosche/about.html')
def Contact(request,customer_id):
	latest_customers = Customer.objects.order_by('-pub_date')[:5]
	context= {
	'latest_customers': latest_customers
	}
	return render(request,'Bosche/contact.html', context)