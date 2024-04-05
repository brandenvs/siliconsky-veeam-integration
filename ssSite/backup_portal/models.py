from django.contrib.auth.models import User
from django.db import models


class StorageAllocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organizationUid = models.CharField(
        max_length=255, default="3110a9da-7ea1-4857-98cb-c3e5c46b6dd6"
    )
    role = models.CharField(max_length=255, default="CompanyTenant")
    mfaPolicyStatus = models.CharField(max_length=255, default="Disabled")
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255, default="null")
    phone = models.CharField(max_length=20)
    userName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    siteUid = models.CharField(
        max_length=100, default="b65acaf4-e282-4096-9e56-8c840442a3a3"
    )
    companySiteBackupResourceUid = models.CharField(
        max_length=100, default="a2b21ca5-55cc-4616-8b39-6270c0741b26"
    )
    description = models.TextField(default="null")
    vcdUserId = models.CharField(max_length=100, default="null")
    resourceFriendlyName = models.CharField(max_length=100)
    storageQuota = models.BigIntegerField()
    isStorageQuotaUnlimited = models.BooleanField(default=False)

    def __str__(self):
        output = f"""StorageAllocation Model
        # Profile:
        {self.title} {self.firstName} {self.lastName}
        {self.email}
        
        # Credentials:
        {self.userName}
        {self.password}
        
        # Backup Resource:
        {self.resourceFriendlyName}
        {self.vcdUserId}
        {self.description}
        
        ## Storage Quota:
        {self.storageQuota}
        """
        return output
