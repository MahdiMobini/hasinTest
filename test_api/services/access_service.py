from __future__ import annotations

from typing import Optional

from test_api.models import Country, IPRecord


class AccessDecisionService:
    @staticmethod
    def get_client_ip(request) -> Optional[str]:
        forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if forwarded_for:
            return forwarded_for.split(',')[0].strip()
        print(f"Client IP: {request.META.get('REMOTE_ADDR')}")
        return request.META.get('REMOTE_ADDR')

  

    @staticmethod
    def has_access_for_ip_record(ip_record) -> bool:
        if ip_record is None:
            return False

        country_obj = Country.objects.get(name="russia")
        
        ip_type = IPRecord.objects.filter(ip_address=ip_record).values_list('p_type', flat=True).first()

        print(f"IP Type: {ip_type}, Country Type: {country_obj.p_type}")
        if country_obj.p_type == Country.AccessType.FULL_ACCESS:
            return True

        if country_obj.p_type == Country.AccessType.FULL_DENIED:
            return False

        if country_obj.p_type == Country.AccessType.SEMI_ACCESS:
            return ip_type != IPRecord.IPAccessType.DENIED

        if country_obj.p_type == Country.AccessType.SEMI_DENIED:
            return ip_type == IPRecord.IPAccessType.ACCESS

        return False

    @classmethod
    def can_access_for_request(cls, request) -> bool:
        ip_record = cls.get_client_ip(request)
        return cls.has_access_for_ip_record(ip_record)
