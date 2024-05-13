from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная | Auto-Tun',
    }
    return render(request, 'main/index.html', context)
