from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
# Create your views here.

def homeview(Request):
	#return HttpResponse("<b>My first django Homepage</b>")
	return render(Request,'index.html')

def signupview(Request):
    	#return HttpResponse("<b>My first django Homepage</b>")
    return render(Request,'signup.html')

def insertView(request):
    
	f=signupmodelform(request.POST)
	if f.is_valid():
		a=f.save()
	return render(request,'login.html')

def loginview(Request):
    	#return HttpResponse("<b>My first django Homepage</b>")
	return render(Request,'login.html')

def logincheck(request):
    n=request.GET['email']
    p=request.GET['password']
    print(n)
    data=signupmodel.objects.all()
    for d in data:
        if d.email==n and d.password==p:
            print(d.email)
            return render(request,'index.html')
    return render(request,'login.html',{'Error':'Invalid Credentials....'})

def aboutview(Request):
    	#return HttpResponse("<b>My first django Homepage</b>")
	return render(Request,'about.html')

def categoriesview(Request):
    	#return HttpResponse("<b>My first django Homepage</b>")
	return render(Request,'categories.html')

def booklistview(Request):
    	#return HttpResponse("<b>My first django Homepage</b>")
	return render(Request,'booklist.html')

def addbookview(Request):
	# bookform=bookmodelform()
	return render(Request,'AddBook.html')

def insertbookView(request):
    f= bookmodelform(request.POST) 
    if f.is_valid():
        f.save() 
    data=bookmodel.objects.all()
    return render(request,'booklist.html',{'Data':data})

def EditBookView(request):
    id=request.GET['id']
    print(id)
    user=bookmodel.objects.get(id=id)
    print(user)
    return render(request,'EditBook.html',{'d': user })

def updateDataViews(request):
    updateObj=bookmodel.objects.get(id=request.GET['id'])
    updateObj.book_name = request.GET['book_name']
    updateObj.author_name  = request.GET['author_name']
    updateObj.quantity = request.GET['quantity']
    updateObj.price = request.GET['price']
    updateObj.book_categories = request.GET['book_categories']
    updateObj.save(update_fields=['book_name','author_name','quantity','price','book_categories'])
    updateObj.save()
    data=bookmodel.objects.all()
    return render(request,'booklist.html',{'Data':data})

def deleteViews(request):
    deletee = request.GET['del']
    bookmodel.objects.get(id=deletee).delete()
    data=bookmodel.objects.all()
    return render(request,'booklist.html',{'Data':data})

def contactview(Request):
    	#return HttpResponse("<b>My first django Homepage</b>")
	return render(Request,'contact.html')
