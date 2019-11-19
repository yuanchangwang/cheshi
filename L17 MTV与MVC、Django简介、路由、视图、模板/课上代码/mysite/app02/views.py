from django.shortcuts import render, HttpResponse

# Create your views here.
def test02(request):
    return HttpResponse("app02下的 test02 函数")


def book_list(request):
    
    return render(request, "book_list.html")


def publish_list(request):
    # return render(request, "publish_list.html")
    return render(request, "publish_list1.html")
