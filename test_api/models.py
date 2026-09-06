

from django.db import models


class Country(models.Model):
    class AccessType(models.TextChoices):
        FULL_ACCESS = 'FULL_ACCESS', 'Full Access'
        FULL_DENIED = 'FULL_DENIED', 'Full Denied'
        SEMI_ACCESS = 'SEMI_ACCESS', 'Semi Access'
        SEMI_DENIED = 'SEMI_DENIED', 'Semi Denied'

    name = models.CharField(max_length=100)
    p_type = models.CharField(max_length=100, choices=AccessType.choices, default=AccessType.FULL_DENIED)

    class Meta:
        db_table = 'test_api_country'
        indexes = [
            models.Index(fields=['name'], name='country_name_idx'),
        ]

    def __str__(self):
        return self.name


class IPRecord(models.Model):
    class IPAccessType(models.TextChoices):
        ACCESS = 'ACCESS', 'Access'
        DENIED = 'DENIED', 'Denied'

    ip_address = models.GenericIPAddressField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    p_type = models.CharField(max_length=100, choices=IPAccessType.choices)

    class Meta:
        db_table = 'test_api_ips'
        indexes = [
            models.Index(fields=['ip_address', 'country'], name='ips_ip_country_idx'),
        ]

    def __str__(self):
        return self.ip_address