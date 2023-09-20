from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #HTML rendering view
    path('operators/', views.operator_list, name='operator_list'),
    # path('account/',views.account_list,name='account_list'),
    # path('operators/',views.operators_list,name='operators_list'),


    # REST API views
    path('api/operators/', views.OperatorView.as_view(), name='operator-api-list'),
    path('api/accounts/', views.AccountView.as_view(), name='account-api-list'),
    path('api/cards/', views.CardView.as_view(), name='card-api-list'),
    path('api/cardtypes/', views.CardTypeView.as_view(), name='cardtype-api-list'),
    path('api/transactions/', views.TransactionView.as_view(), name='transaction-api-list'),
    path('api/employees/', views.EmployeeView.as_view(), name='employee-api-list'),
    
    # Add other URL patterns for your API views if needed
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)