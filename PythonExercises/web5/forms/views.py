from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from forms.forms import InvoiceForm, ProductForm
from forms.exportPdf import exportPdf
from forms.models import Invoice
from django.db.models import Q


def authorize(current_user, invoice):
    responsible = [u.id for u in invoice.commissioners.all()] + [invoice.responsible_worker.id]
    if current_user.id not in responsible:
        return False

    return True


@login_required()
def index(request):
    invoices = Invoice.objects \
        .filter(Q(commissioners__id=request.user.id) | Q(responsible_worker__id=request.user.id)) \
        .order_by('-date_created') \
        .distinct()

    return render(request, 'forms/index.html', {'invoices': invoices})


@login_required()
def invoice_form(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.responsible_worker = request.user
            temp.save()

            temp.commissioners.add(*(form["commissioners"].value()))

            return redirect('forms:index')
    else:
        form = InvoiceForm()

    return render(request, 'forms/invoiceForm.html', {'form': form})


@login_required()
def invoice_form_details(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    if not authorize(request.user, invoice):
        return redirect('%s?next=%s' % ("/users/login/", request.path))

    total = 0
    for product in invoice.products.all():
        total += product.sum

    return render(request, 'forms/invoiceDetails.html', {'invoice': invoice, 'product_total': total})


@login_required()
def invoice_form_details_pdf(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    if not authorize(request.user, invoice):
        return redirect('%s?next=%s' % ("/users/login/", request.path))

    total = 0
    for product in invoice.products.all():
        total += product.sum

    return exportPdf('forms/invoiceDetailsPdf.html', {
        'invoice': invoice,
        'products_total': total,
        'pagesize': 'A4'
    })


@login_required()
def product_form(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    if not authorize(request.user, invoice):
        return redirect('%s?next=%s' % ("/users/login/", request.path))

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            temp_form = form.save(commit=False)
            temp_form.invoice = invoice

            temp_form.save()

            return redirect('forms:invoice_form_details', invoice_id=invoice_id)
    else:
        form = ProductForm()

    return render(request, 'forms/productForm.html', {'form': form, 'invoice': invoice})
