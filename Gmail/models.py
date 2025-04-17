from django.db import models


class GmailLogins(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
