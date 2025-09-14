from django.urls import path

from create_quote_request.infrastructure.views import QuoteRequestApiView

urlpatterns = [
    path(
        "quoterequest",
        QuoteRequestApiView.as_view(),
        name="add-new-quote-request",
    ),
]
