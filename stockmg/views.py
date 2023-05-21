from django.shortcuts import render


def home(request):
    title = 'Welcome: This is the Home Page'
    form = 'Siema'
    context = {
        "title": title,
        "form": form,
    }
    return render(request, "home.html", context)
