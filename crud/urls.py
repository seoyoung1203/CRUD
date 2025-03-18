"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from posts import views

urlpatterns = [
    # 주소창에 있으면 수행해줘
    path('admin/', admin.site.urls),
    # Read(All)
    path('posts/', views.index),
    #Read(1)
    path('posts/<int:id>/', views.detail), 
    
    #Create
    ## 입력하는 공간
    path('posts/new/', views.new),
    ## 저장하는 공간
    path('posts/create/', views.create), 
    
    #Delete
    path('posts/<int:id>/delete/', views.delete),
    
    #Update
    # 기존정보 수정
    path('posts/<int:id>/edit/', views.edit),
    # 수정한 정보 데이터 베이스에 반영
    path('posts/<int:id>/update/', views.update),
                 # 숫자 아무거나 들어온당
]

# <int:id> >> 게시물 하나만 찾아서 들어가는 애들
