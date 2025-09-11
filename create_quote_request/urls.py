from django.urls import path

from create_quote_request.views import QuoteRequestApiView

urlpatterns = [
    path(
        "quoterequest",
        QuoteRequestApiView.as_view(),
        name="add-new-quote-request",
    ),
]
