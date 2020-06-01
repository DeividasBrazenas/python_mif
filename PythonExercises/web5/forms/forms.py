from django.forms import ModelForm
from forms.models import Invoice, Products


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ("institution", "seller", "series", "commissioners",
                  "sellers_code", "date", "location")


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ("name", "amount_type", "amount", "sum", "reason")
