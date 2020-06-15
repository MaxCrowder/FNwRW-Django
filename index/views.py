from django.shortcuts import render
from .forms import EmailForm
# from .models import Email


# def index(request):
#     return render(request, 'index.html')

def index(request):
    form = EmailForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = EmailForm()

    agrs = {
        'form': form,
    }
    return render(request, 'index.html', agrs)

