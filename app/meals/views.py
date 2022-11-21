from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from xhtml2pdf import pisa

from .forms import ClaimCreateForm
from .models import Claim, ClaimApprover, Staff


class ClaimListView(ListView):
    model = Claim


class ClaimDetailView(DetailView):
    model = Claim


def render_pdf_view(request, *args, **kwargs):
    claim_id = kwargs.get('pk')
    claim = Claim.objects.get(pk=claim_id)
    template_path = "meals/claim_pdf.html"
    context = {"object": claim}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type="application/pdf")
    # response["Content-Disposition"] = 'attachment; filename="report.pdf"'
    response["Content-Disposition"] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse("We had some errors <pre>" + html + "</pre>")
    return response


class ClaimCreateView(LoginRequiredMixin, CreateView):
    model = Claim
    form_class = ClaimCreateForm

    # def test_func(self, form):
    #     return self.request.user == form.instance.

    def form_valid(self, form):
        form.instance.staff = self.request.user.staff
        return super().form_valid(form)

    # def get_initial(self):
    #     # Get the initial dictionary from the superclass method
    #     initial = super(ClaimCreateView, self).get_initial()
    #     # Copy the dictionary so we don't accidentally change a mutable dict
    #     initial = initial.copy()
    #     # provider = User.objects.get(pk=2)
    #     # initial['provider'] = provider
    #     initial["staff"] = self.request.user
    #     # etc...
    #     return initial


class ClaimApproverCreateView(CreateView):
    model = ClaimApprover
    fields = "__all__"


class StaffUpdateView(UpdateView):
    model = Staff
    fields = "__all__"
