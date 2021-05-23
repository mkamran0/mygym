from django.urls import path
from.import views
urlpatterns = [
    path('',views.index, name='gymhome'),
    path('about/', views.aboutus, name='about'),
    path('contactus/', views.contactus, name='contact'),
    path('joining/', views.joining, name='join'),
    path('joinsuccess/', views.joinsuccess, name='jsuccess'),
    path('calling/', views.calling, name='call'),
    path('messaging/', views.messaging, name='message'),
    path('fees_details/', views.fees_details, name='fees'),
    path('trainer/', views.trainer, name='trainers'),
    path('yogabest/', views.yogabest, name='yoga'),
    path('yogatrainer/', views.yogatrainer, name='yoga_trainers'),
    path('dietplans/', views.dietplans, name='dplans'),
    path('dietplanners/', views.dietplanners, name='dplanners'),
    path('viewdetails1/', views.viewdetails1, name='view1'),
    path('viewdetails2/', views.viewdetails2, name='view2'),
    path('viewdetails3/', views.viewdetails3, name='view3'),
    
    
]