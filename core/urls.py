from django.contrib import admin
from django.urls import path
from app.views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TodoListView.as_view(), name='list'),
    path('create/', TodoCreateView.as_view(), name='create'),
    path('update/<int:id>/', TodoUpdateView.as_view(), name='update'),
    path('delete/<int:id>/', TodoDeleteView.as_view(), name='delete')
]
