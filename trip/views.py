
from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def anlyze(request):
    djtext=request.POST.get('text','false')
    repunch=request.POST.get('removepunc','off')
    capi=request.POST.get('upper','off')
    Newlineremover=request.POST.get('newlineremover','off')
    analyzed=""
    if repunch=='on':
        
        punch='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punch:
                analyzed=analyzed+char
        variable={'purpose':'  after analyze text we give us','anlyze_text':analyzed}
        return render(request,'base.html',variable)

    if(capi=='on'):
        for char in djtext:
            analyzed=analyzed + char.upper()
        variable={'purpose':'UPPER CASE text','anlyze_text':analyzed}
        return render(request,'base.html',variable)

    if(Newlineremover=='on'):
        for char in djtext:
            if char !='\n' and char !='\r':
              analyzed=analyzed + char
        variable={'purpose':'Capitilize text','anlyze_text':analyzed}
        return render(request,'base.html',variable)
    else:
        return HttpResponse('<h5>error plese click given any box...</h5>')  

def link(request):
    return HttpResponse('''
    <a href="youtube.com">youtube</a>
    <a href="https://www.google.com/">google</a>
    <a href="facebook.com">facebook</a>
    <a href="yono.com">yono</a>''')



    
        

    
