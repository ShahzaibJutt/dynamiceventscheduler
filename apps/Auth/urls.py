from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.Auth import views

urlpatterns = [
    path("login/", views.Login.as_view(), name="Login"),
    # path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", views.Register.as_view(), name="Register"),
    path("update_user/<int:user_id>/", views.UpdateUser.as_view(), name="update_user"),
    path("viewusers/", views.ViewAll.as_view(), name="ViewUsers"),
    path("viewuser/<int:user_id>/", views.ViewUser.as_view(), name="ViewUser"),
    path("logout/", views.Logout.as_view(), name="Logout"),
    path("resetpassword/", views.ResetPassword.as_view(), name="reset-password"),
    path(
        "resetpasswordhandler/",
        views.ResetPasswordHandler.as_view(),
        name="reset-password-handler",
    ),
    path("verifyuser/", views.VerifyUser.as_view(), name="verify-user"),
]
