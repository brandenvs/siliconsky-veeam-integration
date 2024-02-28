from django.db import models
from django.contrib.auth.models import User

# Integration Site User Model
class StandardUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)



# EOF Branden van Staden