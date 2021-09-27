from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def indexViews(request):
    return render(request, 'index.html')

def dashboardViews(request):
    return render(request,'dashboard.html')

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {"form": form})
    # form = UserCreationForm(request.POST or None)
    #
    # if form.is_valid():
    #     user = form.save(commit=False)
    #     messages.success(request, 'registration done!')
    #     return redirect('login')
    # return render(request, 'registration/register.html', {"form": form})