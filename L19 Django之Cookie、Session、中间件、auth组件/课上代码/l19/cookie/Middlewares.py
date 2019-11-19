from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, HttpResponse, redirect

class MD1(MiddlewareMixin):
    def process_request(self, request):
        print("MD1 下的 process_request 方法")
        # return HttpResponse("hello")


    def process_response(self, request, response):
        print("MD1 下的 process_response 方法")
        # print(id(response))
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("MD1 下的 process_view 方法")
        # return view_func(request)

    def process_exception(self, request, exception):
        print("MD1 下的 process_exception 方法")



class MD2(MiddlewareMixin):
    def process_request(self, request):
        print("MD2 下的 process_request 方法")

    def process_response(self, request, response):
        print("MD2 下的 process_response 方法")
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("MD2 下的 process_view 方法")

    def process_exception(self, request, exception):
        print("MD2 下的 process_exception 方法")
        return HttpResponse(exception)