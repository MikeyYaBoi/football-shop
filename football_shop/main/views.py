from django.shortcuts import render

def show_main(request):
    context = {
        'product': 'Air Jordan 1 Retro High',
        'price': '3,042,880',
        'description': 'The Air Jordan 1 Retro High remakes the classic sneaker, giving you a fresh look with a familiar feel. Premium materials with new colors and textures give modern expression to an all-time favorite.'
    }
    return render(request, "main.html", context)
# Create your views here.
