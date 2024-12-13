from django.shortcuts import render

def home(request):
    context={"user":"Guest"}
    return render(request, 'pages/home/home.html', context)
