from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:id>', views.view_student, name='view_student'),
    path('add/', views.add, name='add_student'),
    path('update/<int:id>', views.update, name='update_student'),
    path('delete/<int:id>', views.delete_student, name='delete_student'),
    path('export', views.export, name='export'),
    path('import', views.upload, name='upload'),
    path('export-pdf', views.print_to_pdf, name='pdf_export'),
]
