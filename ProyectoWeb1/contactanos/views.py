from django.shortcuts import redirect, render
from .forms import FormularioContactanos
from django.core.mail import EmailMessage



def contactanos(request):
    formulario_contactanos=FormularioContactanos

    if request.method=="POST":
        formulario_contactanos=FormularioContactanos(data=request.POST)
        if formulario_contactanos.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")


            email=EmailMessage("Mensaje desde App Django",
            "El usuario con nombre {} con la direccn {} escribe lo siguiente:\n\n{}".format(nombre, email, contenido),
            "",["kvb.minango@yavirac.edu.ec"],reply_to=[email])

            try:
                email.send()

                return redirect("/contactanos/?valido")
            except:
                return redirect("/contactanos/?novalido")

    return render(request, "contactanos/contactanos.html", {'miFormulario':formulario_contactanos})
