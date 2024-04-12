from . import views
from django.urls import path
from django.contrib.auth import views as authViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
	path('', views.Home, name="home"),
	path('register/', views.Register, name="register"),
	path('login/', authViews.LoginView.as_view(template_name='sport/login.html'), name="login"),
	path('logout/', authViews.LogoutView.as_view(template_name='sport/logout.html'), name="logout"),
	path('gob3/', views.Gob3, name = "gob3"),
	path('fufu/', views.Fufu, name = "fufu"),
	path('banku/', views.Banku, name = "banku"),
	path('wakye/', views.Wakye, name = "wakye"),
	path('card/detail/', views.CardDetail, name="card-detail"),

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
