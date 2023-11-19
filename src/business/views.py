from django.shortcuts import render, redirect  
from business.forms import BusinessForm  
from business.models import Business

def home(request):
    return render(request,'home.html')

    
def emp(request):  
    if request.method == "POST": 
        form = BusinessForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass
    else:
        form = BusinessForm()  
    return render(request,'index.html',{'form':form})

def show(request):  
    businesses = Business.objects.all()
    return render(request,"show.html",{'businesses':businesses}) 

def edit(request, id):  
    business = Business.objects.get(id=id)  
    return render(request,'edit.html', {'business':business})

def update(request, id):  
    business = Business.objects.get(id=id)  
    form = BusinessForm(request.POST, instance = business)  
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'business': business})  

def destroy(request, id):  
    business = Business.objects.get(id=id)  
    business.delete()  
    return redirect("/show") 

def search(request):
    query = request.GET.get('query')
    
    if query:
        businesses = Business.objects.filter(name__icontains=query)  # Modify this filter condition as needed
    else:
        businesses = Business.objects.all()

    return render(request, 'search_results.html', {'businesses': businesses, 'query': query})