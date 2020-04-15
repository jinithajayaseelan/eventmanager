from django.urls import path
from authentication.views import signup,signin,signout


urlpatterns = [
    path('signup/', signup),
    path('signin/',signin),
    path('signout/',signout),
]