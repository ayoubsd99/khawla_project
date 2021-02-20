from django.urls import path

from landing.views import items
urlpatterns = [
    path("",items.HomeView.as_view(),name='home'),
    path("Catalog/",items.CatalogView.as_view(),name='catalog'),
    path("About/",items.AboutView.as_view(),name='about'),
    path("Contact/",items.ContactView.as_view(),name='contact'),
    path("api/items_list",items.items_list),

    path("Item/",items.ItemView.as_view(),name='detailsitem'),

]
