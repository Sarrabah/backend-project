from create_quote_request.models import QuoteRequest


def create_quote_request(request, valid_data):
    new_quote_request = QuoteRequest.objects.create(
        title=valid_data["title"],
        description=valid_data["description"],
        status=valid_data["status"],
        archi_id=request.user,
    )
    return new_quote_request
