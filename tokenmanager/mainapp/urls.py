from django.urls import path

from . import views

app_name = "mainapp"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profile_list/", views.profile_list, name="profile_list"),
    path("profile/<int:pk>", views.profile, name="profile"),
    path("scheduled_transfer/", views.scheduled_transfer, name="scheduled_transfer"),
    path("scheduled_transfer/<str:sender>/", views.scheduled_transfer, name="transactions"),
    path("accounts/", views.accounts, name="accounts"),
    path("create-standalone/", views.create_standalone, name="create-standalone"),
    path(
        "standalone-account/<str:address>/",
        views.standalone_account,
        name="standalone-account",
    ),
    path("initial-funds/<str:receiver>/", views.initial_funds, name="initial-funds"),
    path("transfer-funds/<str:sender>/", views.transfer_funds, name="transfer-funds"),
    path("wallets/", views.wallets, name="wallets"),
    path("create-wallet/", views.create_wallet, name="create-wallet"),
    path("wallet/<str:wallet_id>/", views.wallet, name="wallet"),
    path(
        "create-wallet-account/<str:wallet_id>/",
        views.create_wallet_account,
        name="create-wallet-account",
    ),
    path(
        "wallet-account/<str:wallet_id>/<str:address>/",
        views.wallet_account,
        name="wallet-account",
    ),
    path("assets/", views.assets, name="assets"),
    path("create-asset/", views.create_asset, name="create-asset"),
    path("search/", views.search, name="search"),
]