from django.urls import path

from administration.views import items

urlpatterns = [
    path(r'^items/$',items.ItemsView.as_view(),name='listitems'),
    path(r'^detailitem/<str:item_reference>/$',items.ItemView.as_view(),name='item'),
    path(r'^createitem/$',items.CreateItemView.as_view(),name='createitem'),
    path(r'^deleteitem/<str:item_reference>/$',items.DeleteItemView.as_view(),name='deleteitem'),
    path(r'^updateitem/<str:item_reference>/$',items.UpdateItemView.as_view(),name='updateitem'),

]
