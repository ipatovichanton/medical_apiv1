from django.db import models


class Request(models.Model):
    IN_PROGRESS = 'IN PROGRESS'
    DONE = 'DONE'
    DECLINED = 'DECLINED'
    WAITING = 'WAITING'
    
    STATUSES = [
        (IN_PROGRESS, "In progress"),
        (DONE, "Done"),
        (DECLINED, "Declined"),
        (WAITING, "Waiting")
    ]

    from_user = models.ForeignKey(
        to="users.Ailing",
        related_name="requests",
        on_delete=models.CASCADE
    )
    datetime = models.DateTimeField(auto_now_add=True)
    information = models.TextField()
    to_clinic = models.ForeignKey(
        to="clinics.Clinic",
        related_name="requests",
        on_delete=models.CASCADE,
    )
    status = models.CharField(choices=STATUSES, max_length=20, default=WAITING)
    answer = models.TextField(blank=True)
