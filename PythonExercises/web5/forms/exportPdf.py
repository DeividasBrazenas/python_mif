from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse


def exportPdf(templateSrc, ctx):
    template = get_template(templateSrc)
    html = template.render(ctx)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result, encoding="utf-8")
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('Internal error <pre>%s</pre>' % html.escape(html))
