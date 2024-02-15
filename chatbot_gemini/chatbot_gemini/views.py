from django.shortcuts import render


def texto(request):
    return render(request, 'index.html', {})
