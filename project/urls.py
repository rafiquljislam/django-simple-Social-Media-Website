from django.contrib import admin
from django.urls import path,include

from django.contrib.auth.views import LoginView, LogoutView
from apps.posts import views as postsViews
from apps.user import views as userViews


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',postsViews.HomeView.as_view(), name='home'),
    path('register/', userViews.RegisterView.as_view(), name='register'),
    path('login/',LoginView.as_view(template_name='user/register.html'), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('profile/',userViews.ProfielView.as_view(),name='profile'),
    path('post/<int:pk>',postsViews.SinglePostView.as_view(), name='post'),
    path('update/<int:pk>',postsViews.SinglePostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>',postsViews.SinglePostDeleteView.as_view(), name='delete'),
    
    path('api/',include('apps.api.urls')), # Django Rest_framwork

    path('user/<int:id>',postsViews.SingleUserPost.as_view(), name="user"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
