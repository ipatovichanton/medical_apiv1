from django.db import models



class MedicalCard(models.Model):
    user = models.OneToOneField(
        to="users.Ailing",
        related_name="card",
        null=True,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)


class BaseRecord(models.Model):
    doctor = models.ForeignKey(to="users.Doctor", on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    card = models.ForeignKey(
        to=MedicalCard,
        on_delete=models.CASCADE,
        related_name="records"
    )

    class Meta:
        abstract = True
