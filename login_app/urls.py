from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
urlpatterns=[

    path('signup/',views.signup,name="signup"),
    path('login/',views.log_in, name='login'),
    path('view/',views.view,name='view'),
    path('add/', views.add_car, name='add'),
    path('logout/',views.log_out, name='logout'),
    path('delete/<int:car_id>/', views.delete_car, name='delete'),
    path('edit/<int:car_id>/',views.edit_car,name='edit'),
    path('my_cars/', views.my_cars, name='my_cars')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)