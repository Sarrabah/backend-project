from django.db import models


class QuoteRequest(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=8)
    archi_id = models.CharField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "quote_request"
