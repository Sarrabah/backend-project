from rest_framework.exceptions import PermissionDenied

from create_quote_request.infrastructure.models import QuoteRequest


def create_quote_request(request, valid_data):

    if getattr(request.user, "role", None) != "archi":
        raise PermissionDenied("Seul l'architecte peut créer une QuoteRequest.")

    new_quote_request = QuoteRequest.objects.create(
        title=valid_data["title"],
        description=valid_data["description"],
        status=valid_data["status"],
        archi_id=request.user,
    )
    return new_quote_request
