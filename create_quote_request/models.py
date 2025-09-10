from django.db import models


class QuoteRequest(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=8)
    archi_id = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "quote_request"
