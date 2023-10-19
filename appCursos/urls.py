from django.urls import path


from . import views
app_name='appCursos'
urlpatterns=[

    path('',views.listMatricula,name='matricula'),
    path('matricula/',views.createMatricula,name='create_matricula'),
    path('matricula/delete',views.deleteMatricula,name='delete_matricula'),
     path('update_matricula/<int:matricula_id>/', views.updateMatricula, name='update_matricula'),
]