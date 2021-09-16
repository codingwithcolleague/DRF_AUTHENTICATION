"""DRF_CODE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import views
from api.views import student_details,student_list,student_create,student_update,studentdelete,StudentAPI
from student_drf.views import student_api,StudentAPI
from studentmixin.views import (StudentListMixin,
                                StudentCreateMixin,StudentRetriveMixin,
                                StudentUpdateMixin,StudentDestroyMixin)

from studentmixin.views import (StudentListAPIView,StudentCreateAPIView,
                                StudentUpdateAPIView,StudentRetriveAPIView,
                                StudentDestoryAPIView,StudentRetriveDestoryAPIView,StudentRetriveUpdateAPIView)

from student_viewset.views import StudentViewSet,StudenModelViewSet,StudenReadOnlyModelViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from api.auth import CustomAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


router = DefaultRouter()
# router.register('studentapi' , StudentViewSet , basename='student')
router.register('studentapii' , StudenModelViewSet , basename='student')
# router.register('studentapi' , StudenReadOnlyModelViewSet , basename='student')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path("studentinfo/<int:pk>" , student_details),
    # path("studentlist/" , student_list),
    # path("studentcreate/" , student_create),
    # path("studentupdate/" , student_update),
    # path("studentdelete/" , studentdelete),
    # path("studentapi/" , StudentAPI.as_view()),
    # path("studentapi/" , student_api),    
    # path("studentapi/<int:pk>/" , student_api ),

    # path("studentapiclass/" , StudentAPI.as_view() ),
    # path("studentapiclass/<int:pk>/" , StudentAPI.as_view() ),
    
    # path("studentmixinlist/" , StudentListMixin.as_view()),
    # path("studentmixincreate/" , StudentCreateMixin.as_view()),
    # path("studentmixinretrive/<int:pk>/" , StudentRetriveMixin.as_view()),
    # path("studentmixinupdate/<int:pk>/" , StudentUpdateMixin.as_view()),
    # path("studentmixindelete/<int:pk>/" , StudentDestroyMixin.as_view())
    
    path("studentlistapi/" , StudentListAPIView.as_view()),
    # path("studentcreateapi/" , StudentCreateAPIView.as_view()),
    path("studentupdateeapi/<int:pk>/" , StudentUpdateAPIView.as_view()),
    # path("studentretriveapi/<int:pk>/" , StudentRetriveAPIView.as_view()),
    # path("studentdestoryapi/<int:pk>/" , StudentDestoryAPIView.as_view()),
    # path("studentretrivedestoryapi/<int:pk>/" , StudentRetriveDestoryAPIView.as_view()),
    # path("studentretriveupdateapi/<int:pk>/" , StudentRetriveUpdateAPIView.as_view())
    # path("",include(router.urls)),
    # path("auth/",include("rest_framework.urls")),
    # path("gettoken/" , obtain_auth_token),
    # path('apitoken/', CustomAuthToken.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


]