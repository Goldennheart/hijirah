from django.shortcuts import render
from .forms import UserRegisterForm

# Create your views here.

def index (request):
    return render (request, 'hijira/index.html')


def register (request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request.user)
            return redirect('index')
    else:
        form = UserRegisterForm()
        context = {
            'form':form
        }
    return render (request, 'registration/register.html', context)