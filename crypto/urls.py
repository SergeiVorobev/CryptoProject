from django.urls import path
from . import views
from django.conf.urls.static import static
from django.urls import re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    # re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('', views.home, name='home'),
    path('strategies/', views.show_strategies, name='strategies'),
    path('strategies/add/', views.create_strategy, name='add-strategy'),
    path('strategies/show_strategy/<strategy_id>', views.show_strategy, name='show-strategy'),
    path('strategies/edit_strategy/<strategy_id>', views.edit_strategy, name='edit-strategy'),
    path('strategies/add_strategy', views.create_strategy, name='add-strategy'),
    path('strategies/del_strategy/<strategy_id>', views.del_strategy, name='del-strategy'),
    path('strategies/show_strategy/calculate/<strategy_id>', views.calculate_orders, name='calculate-orders'),

]
