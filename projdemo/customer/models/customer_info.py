
from django.db import models


class CustomerInfo(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(null=False, blank=False, max_length=255)
    email = models.EmailField(null=False, blank=False, unique=True,
                              error_messages={'unique': 'Customer with this email already exists!'})
    dob = models.DateField(default=None, null=True, blank=True)
    gender = models.SmallIntegerField(default=1, choices=((0, 'female'), (1, 'male')))
    extra = models.JSONField(default=dict, null=True, blank=True)

    class Meta:
        db_table = 'customer_infos'
        ordering = ['-id']

    def __str__(self):
        return self.full_name
