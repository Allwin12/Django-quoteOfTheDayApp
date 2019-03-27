import wikiquote
from django.shortcuts import render,HttpResponse

def home(request):
    str=wikiquote.quote_of_the_day()
    quote=str[0]
    author=str[1]
    html="<html><center><h1>Quote of the day</h1></center><br><h2>%s</h2><br><div align='right'><h3>Author : %s</h3></div></html>" %(quote,author)
    return HttpResponse(html)
