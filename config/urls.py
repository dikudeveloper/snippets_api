from django.urls import path
from django.conf.urls import include

from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views


urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('', views.api_root),
    path('snippets/<int:pk>/highlights', views.SnippetHighlight.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]