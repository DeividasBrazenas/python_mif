from django.urls import path

from . import views

app_name = 'forms'
urlpatterns = [
    path('', views.index, name='index'),
    path('invoice', views.invoice_form, name="invoice_form"),
    path('invoice/<int:invoice_id>', views.invoice_form_details, name="invoice_form_details"),
    path('invoice/<int:invoice_id>/pdf', views.invoice_form_details_pdf, name="invoice_form_details_pdf"),
    path('invoice/<int:invoice_id>/products', views.product_form, name="product_form"),
]
