from django.shortcuts import render
from generator.models import Password


# Create your views here.
def index(request):
    context = {}

    if request.method == "POST":
        length = request.POST.get("length", None)
        uppercase = request.POST.get("uppercase", None)
        lowercase = request.POST.get("lowercase", None)
        numbers = request.POST.get("numbers", None)
        special = request.POST.get("special", None)

        context = {
            "length": length,
            "uppercase": uppercase,
            "lowercase": lowercase,
            "numbers": numbers,
            "special": special,
        }

        if length == None:
            context["error"] = "Please enter a length."
        elif (
            uppercase == None
            and lowercase == None
            and numbers == None
            and special == None
        ):
            context["error"] = "Please select at least one option."
        else:
            context["password"] = Password().generate_password_and_save(
                int(length),
                lowercase,
                uppercase,
                numbers,
                special,
            )

    return render(request, "generator/index.html", context)
