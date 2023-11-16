# Generated by Django 4.2.7 on 2023-11-16 23:48

from django.db import migrations, models
import django.db.models.deletion
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit', models.DecimalField(decimal_places=2, default=2000.0, max_digits=10)),
                ('available_credit', models.DecimalField(decimal_places=2, default=2000.0, max_digits=10)),
                ('card_number', encrypted_model_fields.fields.EncryptedCharField()),
                ('cvv', encrypted_model_fields.fields.EncryptedCharField()),
                ('expiration_date', encrypted_model_fields.fields.EncryptedDateField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
        ),
    ]
