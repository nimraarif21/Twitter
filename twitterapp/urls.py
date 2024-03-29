from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from twitterapp import views
from django.conf.urls import include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('signup/', views.UserSignUp.as_view()),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('tweets/', views.TweetList.as_view()),
    path('tweets/<int:pk>/', views.TweetDetail.as_view()),
    path('follow/', views.UserRelationCreateList.as_view()),
    path('followings/', views.FollowingList.as_view()),
    path('followers/', views.FollowerList.as_view()),
    path('like/', views.LikeaTweet.as_view()),
    path('unlike/<int:pk>/', views.UnlikeaTweet.as_view()),
    path('newsfeed/', views.NewsFeed.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)