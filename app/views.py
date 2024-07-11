from django.shortcuts import render

# Create your views here.

def Backend_Data(request):
    d={"name":"SAI","course":"B.Tech","college":"VITB"}
    return render(request,"Backend_Data.html",d)