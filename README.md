## Run

```bash
(sudo) docker compose up --build
```

## Add first data (russia)

```bash
docker compose exec web python manage.py shell
```

```python
from test_api.models import Country

Country.objects.get_or_create(
    name="russia",
    defaults={"p_type": Country.AccessType.SEMI_ACCESS},
)
```

You can change `p_type` between: `FULL_ACCESS` / `FULL_DENIED` / `SEMI_ACCESS` / `SEMI_DENIED`

To update an existing record:

```python
Country.objects.filter(name="russia").update(p_type=Country.AccessType.SEMI_DENIED)
```

## Test with curl

```bash
curl -i http://localhost:8000/
```

## Mock more IPs with different permission types

```python
from test_api.models import Country, IPRecord

russia = Country.objects.get(name="russia")
IPRecord.objects.create(ip_address="1.1.1.1", country=russia, p_type=IPRecord.IPAccessType.ACCESS)
IPRecord.objects.create(ip_address="2.2.2.2", country=russia, p_type=IPRecord.IPAccessType.DENIED)
```

## More curl tests

```bash
curl -i -H "X-Forwarded-For: 1.1.1.1" http://localhost:8000/
curl -i -H "X-Forwarded-For: 2.2.2.2" http://localhost:8000/
curl -i -H "X-Forwarded-For: 9.9.9.9" http://localhost:8000/
```

Expected:
1. `200 OK`
2. `403 Forbidden`
3. `200 OK`

## Admin panel

You can also add data via `http://localhost:8000/admin`, but don't forget to create a superuser first:

```bash
python manage.py createsuperuser
```