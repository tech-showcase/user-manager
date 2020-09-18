from django.db import models


class APIAccess(models.Model):
    api_name = models.CharField(max_length=50)
    status_code = models.PositiveSmallIntegerField()
    response_time = models.PositiveIntegerField()
    created_at = models.DateTimeField(primary_key=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['created_at']
        managed = False

    def __str__(self):
        return f"{self.api_name}-{self.created_at}"
