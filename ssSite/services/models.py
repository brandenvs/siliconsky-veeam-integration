from django.contrib.auth.models import AbstractUser, User
from django.db import models

# class VSPCUser(AbstractUser):
#     storage_quota = models.BigIntegerField(default=1073741824)


# class VSPCUser(AbstractUser):
#     organizationUid = models.CharField(
#         max_length=255, default="3110a9da-7ea1-4857-98cb-c3e5c46b6dd6"
#     )
#     role = models.CharField(max_length=255, default="Company Owner")
#     mfaPolicyStatus = models.CharField(max_length=255, default="Disabled")
#     firstName = models.CharField(max_length=100)
#     lastName = models.CharField(max_length=100)
#     title = models.CharField(max_length=100)
#     email = models.EmailField()
#     address = models.CharField(max_length=255, null=True, blank=True)
#     phone = models.CharField(max_length=20)
#     userName = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     siteUid = models.CharField(
#         max_length=100, default="b65acaf4-e282-4096-9e56-8c840442a3a3"
#     )
#     companySiteBackupResourceUid = models.CharField(
#         max_length=100, default="a2b21ca5-55cc-4616-8b39-6270c0741b26"
#     )
#     description = models.TextField(null=True, blank=True)
#     vcdUserId = models.CharField(max_length=100, null=True, blank=True)
#     resourceFriendlyName = models.CharField(max_length=100, default="BCloudRepo")
#     storageQuota = models.BigIntegerField(default=1073741824)
#     isStorageQuotaUnlimited = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.firstName} {self.lastName} - {self.email}"


class Organization(models.Model):
    resellerUid = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    taxId = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    country = models.IntegerField()
    state = models.IntegerField()
    countryName = models.CharField(max_length=100)
    regionName = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    notes = models.TextField(null=True, blank=True)
    zipCode = models.IntegerField()
    website = models.URLField(default="www.alpha.com")
    veeamTenantId = models.CharField(max_length=100, null=True, blank=True)
    subscriptionPlanUid = models.CharField(max_length=100, null=True, blank=True)
    isAlarmDetectEnabled = models.BooleanField(default=False)
    isBackupAgentManagementEnabled = models.BooleanField(default=False)
    isFileLevelRestoreEnabled = models.BooleanField(default=False)
    isBackupServerManagementEnabled = models.BooleanField(default=False)
    isVBPublicCloudManagementEnabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name
