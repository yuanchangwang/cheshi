from rest_framework.routers import DefaultRouter
from students import views

urlpatterns = []  # 路由列表

router = DefaultRouter()  # 可以处理视图的路由器

router.register('student', views.StuentAPIView)  # url进行注册

urlpatterns += router.urls  # 将路由器中的所有路由信息追加到django的路由列表中