# Generated by Django 5.0.3 on 2024-05-08 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VMSapi', '0002_rename_acknowledgement_date_purchase_order_acknowledgment_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='on_time_delivery_rate',
            new_name='on_time_delivery',
        ),
    ]
