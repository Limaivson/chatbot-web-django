from django.shortcuts import render


def texto(request):
    return render(request, 'texto.html', {})
