
from django.contrib import admin
from django.urls import path
from bimmerreviewer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.homepage, name='homepage'),
    path('', views.Firstview.as_view(), name='home'),
    path('review/<int:pk>', views.DetailReview.as_view(), name='detail-review'),
    path('create-reviews/', views.CreateReview.as_view(), name='create-review'),
    path('update-reviews/<int:pk>', views.UpdateReview.as_view(), name='update-review'),
    path('delete-reviews/<int:pk>', views.DeleteReview.as_view(), name='delete-review'),
]
