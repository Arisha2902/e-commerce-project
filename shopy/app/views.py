from django.shortcuts import render, HttpResponse
from app.models import Contact, product
from django.contrib import messages
from math import ceil


def index(request):
    allprods=[]
    catprods=product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=product.objects.filter(category=cat)
        nSlides=len(prod)//4 + ceil((len(prod)/4)-(len(prod)//4))
        allprods.append([prod,range(1,nSlides),nSlides])
    params={'allprods':allprods}
    return render(request, 'index.html',params)







def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        pnumber = request.POST.get('pnumber')
        myquery = Contact(name=name,email= email, desc= desc,phonenumber= pnumber)
        myquery.save()
        messages.info(request, 'We Will get back to you soon..')
        return render(request, 'contact.html')

        # print(name, email, desc, phonenumber)
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

