from django.shortcuts import render

# Create your views here.
def bst_download(request):
    return render(request,'bst_download.html')