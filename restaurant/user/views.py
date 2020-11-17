from django.shortcuts import render

from user.forms import UserForm

# Create your views here.
def register(request):

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserForm()
    else:
        form = UserForm()
    return render(request, 'registration/register.html', {'form': form})


def profile(request):
    return render(request, 'registration/register.html', {'form': form})
