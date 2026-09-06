from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('test_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='country',
            new_name='CountryTemp',
        ),
        migrations.RenameModel(
            old_name='CountryTemp',
            new_name='Country',
        ),
        migrations.RenameModel(
            old_name='ips',
            new_name='IPRecord',
        ),
        migrations.AddIndex(
            model_name='country',
            index=models.Index(fields=['name'], name='country_name_idx'),
        ),
        migrations.AddIndex(
            model_name='iprecord',
            index=models.Index(fields=['ip_address', 'country'], name='ips_ip_country_idx'),
        ),
    ]