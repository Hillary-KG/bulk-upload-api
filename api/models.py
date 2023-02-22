from django.db import models


# Create your models here.
class UserRecord(models.Model):
    """
    Defines the blueprint for a user record
    """

    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    national_id = models.CharField(max_length=50, null=False, unique=True)
    birth_date = models.DateField(null=False)
    address = models.CharField(max_length=150, null=False)
    country = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=30, null=False)
    email = models.CharField(max_length=150, null=False, unique=True)
    finger_print_signature = models.CharField(max_length=250, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=False, auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class FileObject(models.Model):
    """
    define the blueprint for the uploaded file
    """

    source = models.CharField(max_length=300, null=False)
    status = models.IntegerField(default=0)  # 0-failed, 1-processed
    offset = models.IntegerField(null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(null=False, auto_now=True)

    class Meta:
        ordering = ["source"]

    def __str__(self) -> str:
        return f"{self.name}"
