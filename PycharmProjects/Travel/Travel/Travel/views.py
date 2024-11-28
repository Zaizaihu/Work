from django.http import HttpResponse

def SMStemplate(request):
    return HttpResponse("HEllo, what is you need SMS template")