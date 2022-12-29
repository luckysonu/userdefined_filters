from django.shortcuts import render

# Create your views here.
def filters(request):
    import datetime
    dt=datetime.date.today()
    d={'data':'hai suma h r u welcome to new year','dt':dt,'c':1}
    return render(request,'filters.html',d)

def userdefinedfilters(request):
    d={'data':'hai suma h r u welcome to the new year'}
    return render(request,'userdefinedfilters.html',d)