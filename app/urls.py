from django.urls import path
from .views import ReviewList, ReviewCreate, ReviewUpdate, ReviewDelete

urlpatterns = [
    path('', ReviewList.as_view(), name='list'),
    path('create/', ReviewCreate.as_view(), name='create'),
    path('update/<int:pk>', ReviewUpdate.as_view(), name='update'),
    path('delete/<int:pk>', ReviewDelete.as_view(), name='delete')
]