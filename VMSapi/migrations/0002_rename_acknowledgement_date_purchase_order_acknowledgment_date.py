# Generated by Django 5.0.3 on 2024-05-08 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VMSapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase_order',
            old_name='acknowledgement_date',
            new_name='acknowledgment_date',
        ),
    ]
