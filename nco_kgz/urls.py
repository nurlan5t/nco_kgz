"""nco_kgz URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from info import views
from users import views as login_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/law_types/', views.LawTypesAPI.as_view()),
    path('api/v1/law_type/<int:pk>/', views.LawTypeAPI.as_view()),
    path('api/v1/laws/<int:id>/', views.LawDetailAPI.as_view()),
    path('api/v1/news/', views.NewsCreateAPI.as_view()),
    path('api/v1/publications/<int:pk>/', views.PublicationTypeAPI.as_view()),
    path('api/v1/publication/<int:pk>/', views.PublicationDetailAPI.as_view()),
    path('api/v1/news/<int:id>/', views.NewsDetailApi.as_view()),
    path('api/v1/register/', login_views.RegisterView.as_view()),
    path('api/v1/confirm/', login_views.ConfirmAPIView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)