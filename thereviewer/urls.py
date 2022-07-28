""" Creating urls to pass in a int or string value
     and calling the views file where all the methods
     are. Also nameing the url so that It can get acessed by the name
"""
from django.contrib import admin
from django.urls import path, include
from bimmerreviewer import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='homepage'),
    path('contactus', views.contact_us, name='contact-us'),
    path('userreview', views.UserView.as_view(), name='user-reviews'),
    path('showall', views.FirstView.as_view(), name='home'),
    path('review/<int:pk>', views.DetailReview.as_view(),
         name='detail-review'),
    path('create-reviews/', views.CreateReview.as_view(),
         name='create-review'),
    path('update-reviews/<int:pk>', views.UpdateReview.as_view(),
         name='update-review'),
    path('delete-reviews/<int:pk>', views.DeleteReview.as_view(),
         name='delete-review'),
    path('accounts/', include('allauth.urls')),
    path('review/<int:pk>/comment', views.AddComment.as_view(),
         name='add-comment'),
    path('likepost/<int:pk>', views.like_review,
         name='like_review'),
    path('category/<str:series>/', views.category_review,
         name='category-view'),
    path('search/', views.search_list,
         name='search_list')
]

# For error pages
handler404 = 'bimmerreviewer.views.error_404'
handler500 = 'bimmerreviewer.views.error_500'