from django.contrib.auth.models import AbstractUser, User
from django.db import models


class VSPCUser(AbstractUser):
    organizationUid = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    mfaPolicyStatus = models.CharField(max_length=255)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20)
    userName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    siteUid = models.CharField(max_length=100)
    companySiteBackupResourceUid = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    vcdUserId = models.CharField(max_length=100, null=True, blank=True)
    resourceFriendlyName = models.CharField(max_length=100)
    storageQuota = models.BigIntegerField()
    isStorageQuotaUnlimited = models.BooleanField()

    def __str__(self):
        return f"{self.firstName} {self.lastName} - {self.email}"


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
