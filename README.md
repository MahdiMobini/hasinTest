run:
    (sudo) docker compose up --build

add first data (russia) with shell:
    docker compose exec web python manage.py shell

then:
    from test_api.models import Country
    Country.objects.get_or_create(
        name="russia",
        defaults={"p_type": Country.AccessType.SEMI_ACCESS},
    )

you can also change p_type between: FULL_ACCESS / FULL_DENIED /SEMI_ACCESS / SEMI_DENIED

test with curl:
    curl -i http://localhost:8000/

for other IPs and different permission types (mock data with shell):
    from test_api.models import Country, IPRecord
    russia = Country.objects.get(name="russia")
    IPRecord.objects.create(ip_address="1.1.1.1", country=russia, p_type=IPRecord.IPAccessType.ACCESS)
    IPRecord.objects.create(ip_address="2.2.2.2", country=russia, p_type=IPRecord.IPAccessType.DENIED)

more curl tests:
    curl -i -H "X-Forwarded-For: 1.1.1.1" http://localhost:8000/
    curl -i -H "X-Forwarded-For: 2.2.2.2" http://localhost:8000/
    curl -i -H "X-Forwarded-For: 9.9.9.9" http://localhost:8000/

expected:
    1. 200 OK
    2. 403 Forbidden
    3. 200 OK