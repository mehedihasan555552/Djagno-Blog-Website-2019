from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

from .views import PostListView, PostDetailView,PostCreateView,PostUpdateView,PostDeleteView


urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('register/', views.register, name='register'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('profile/', views.Profile, name='profile'),
    path('about/', views.about, name='about'),
    path('polls/', views.polls, name='indexx'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),


    path('reset_password/',
       auth_views.PasswordResetView.as_view(template_name="base/password_reset.html"),
       name="reset_password"),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="base/password_reset_sent.html"),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="base/password_reset_form.html"),
     name="password_reset_confirm"),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="base/password_reset_done.html"),
        name="password_reset_complete"),

]
