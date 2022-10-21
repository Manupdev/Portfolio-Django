from django.shortcuts import render

from app.forms import ContactoForm

def mainview(request):
    return render(request, 'index.html')


def contacto(request):
    data = {
        'form':ContactoForm()
    }  

    if request.method=="POST":
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            data["form"]= formulario
    return render(request, 'pages/contacto.html', data)
