from django.urls import path

from . import views

urlpatterns = [
    path('', views.startingPage),
    path('app/today/', views.todayView.as_view(), name="today-tasks"),
    path('app/upcoming/', views.upcomingView.as_view(), name="upcoming-tasks"),
    path('app/project/<str:name>/', views.projectView.as_view(), name="project-detail"),
    path('app/label/<str:name>/', views.labelView.as_view(), name="label-detail"),
    path('app/new/<str:type>/', views.itemAddView.as_view(), name="item-add"),
    path('app/edit/<str:type>/<str:name>', views.itemEditView.as_view(), name="item-edit"),
    path('app/delete/<str:type>/<str:name>', views.itemDeleteView.as_view(), name="item-delete"),
    path('app/task-done/', views.taskDoneView.as_view(), name="task-done"),
    path('app/task-edit/<id>', views.taskEditView.as_view(), name="task-edit"),
]
