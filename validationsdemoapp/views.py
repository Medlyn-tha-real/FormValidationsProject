from django.shortcuts import render # type: ignore

from validationsdemoapp.forms import UserRegistrationForm

# Create your views here.

def SignUp(request):

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "validationsdemoapp/listofusers.html")
    else:
        form=UserRegistrationForm()
    return render(request,"validationsdemoapp/SignUp.html",{'form':form})

















