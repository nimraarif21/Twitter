from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
from twitterapp import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tweets', views.TweetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('follow/', views.UserRelationCreateList.as_view()),
    path('followings/', views.FollowingList.as_view()),
    path('followers/', views.FollowerList.as_view()),
    path('like/', views.LikeaTweet.as_view()),
    path('unlike/<int:pk>/', views.UnlikeaTweet.as_view()),
    path('newsfeed/', views.NewsFeed.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
]

