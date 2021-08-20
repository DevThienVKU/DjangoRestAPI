from django.urls import path, include
# from .views import article_list, article_details
# from .views import ArticleList, ArticleDetails
# from .views import ArticleList, ArticleDetails

from .views import ArticleViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

# Viewsets and Routers
# khởi tạo route Article và User
route = DefaultRouter()
route.register('articles', ArticleViewSet, basename='articles')
route.register('users', UserViewSet)

# Tạo đường dẫn cho tới urls của site APIProject.

urlpatterns = [

    # Viewsets and Routers
    path('api/', include(route.urls)),

    # # Mixins
    # path('articles/', ArticleList.as_view()),
    # path('articles/<int:id>/', ArticleDetails.as_view()),

    # Class Based API Views
    # path('articles/', ArticleList.as_view()),
    # path('articles/<int:id>/', ArticleDetails.as_view())

    # API Decorators
    # path('articles/', article_list),
    # path('articles/<int:pk>/', article_details),

    # Function Bases API View
    # path('articles/', article_list),
    # path('articles/<int:pk>/', article_details)
]
