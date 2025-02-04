# Generated by Django 5.1.3 on 2024-11-28 04:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("county", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "lat",
                    models.DecimalField(
                        blank=True, decimal_places=6, max_digits=8, null=True
                    ),
                ),
                (
                    "lng",
                    models.DecimalField(
                        blank=True, decimal_places=6, max_digits=9, null=True
                    ),
                ),
                ("population", models.BigIntegerField(blank=True, null=True)),
                ("density", models.IntegerField(blank=True, null=True)),
                ("timezone", models.CharField(blank=True, max_length=50, null=True)),
                ("ranking", models.IntegerField(blank=True, null=True)),
                (
                    "manslaughter_by_negligence",
                    models.IntegerField(blank=True, null=True),
                ),
                ("murder_or_manslaughter", models.IntegerField(blank=True, null=True)),
                ("crime_rate", models.FloatField(blank=True, null=True)),
            ],
            options={
                "db_table": "city",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="CityToZipCode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("city_name", models.TextField(blank=True, null=True)),
                ("state_id", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "city_to_zip_code",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="CostOfLivingByCounty",
            fields=[
                (
                    "county",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                (
                    "lat",
                    models.DecimalField(
                        blank=True, decimal_places=4, max_digits=6, null=True
                    ),
                ),
                (
                    "lng",
                    models.DecimalField(
                        blank=True, decimal_places=4, max_digits=7, null=True
                    ),
                ),
                ("population", models.BigIntegerField(blank=True, null=True)),
                ("density", models.IntegerField(blank=True, null=True)),
                ("family_member_count", models.IntegerField()),
                (
                    "housing_cost",
                    models.DecimalField(
                        blank=True, decimal_places=4, max_digits=10, null=True
                    ),
                ),
                (
                    "food_cost",
                    models.DecimalField(
                        blank=True, decimal_places=4, max_digits=10, null=True
                    ),
                ),
                (
                    "healthcare_cost",
                    models.DecimalField(
                        blank=True, decimal_places=4, max_digits=10, null=True
                    ),
                ),
                (
                    "childcare_cost",
                    models.DecimalField(
                        blank=True, decimal_places=4, max_digits=10, null=True
                    ),
                ),
                (
                    "taxes",
                    models.DecimalField(
                        blank=True, decimal_places=4, max_digits=10, null=True
                    ),
                ),
                (
                    "total_cost",
                    models.DecimalField(
                        blank=True, decimal_places=4, max_digits=12, null=True
                    ),
                ),
                (
                    "median_family_income",
                    models.DecimalField(
                        blank=True, decimal_places=4, max_digits=12, null=True
                    ),
                ),
            ],
            options={
                "db_table": "cost_of_living_by_county",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="HomeDatapoint",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("num_homes_sold", models.IntegerField(blank=True, null=True)),
                ("median_sale_price", models.IntegerField(blank=True, null=True)),
                ("start_date", models.DateField(blank=True, null=True)),
                (
                    "median_sale_price_adjusted",
                    models.IntegerField(blank=True, null=True),
                ),
            ],
            options={
                "db_table": "home_datapoint",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Industry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField()),
                ("category", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "industry",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="IndustryCityData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("industry_name", models.TextField(blank=True, null=True)),
                ("name", models.TextField(blank=True, null=True)),
                ("state_id", models.TextField(blank=True, null=True)),
                ("total_employment", models.IntegerField(blank=True, null=True)),
                (
                    "jobs_1000",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "a_mean",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "a_pct10",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "a_pct25",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "a_median",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "a_pct75",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "a_pct90",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "h_mean",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "h_pct10",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "h_pct25",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "h_median",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "h_pct75",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "h_pct90",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
            ],
            options={
                "db_table": "industry_city_data",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="NaturalDisaster",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("incident_type", models.TextField()),
                ("date", models.DateField()),
                ("declaration_type", models.TextField(blank=True, null=True)),
                ("programs_declared", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "natural_disaster",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Neighborhood",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField()),
                ("city", models.TextField(blank=True, null=True)),
                ("state_id", models.TextField(blank=True, null=True)),
                ("zip_code", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "neighborhood",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="State",
            fields=[
                ("name", models.CharField(max_length=255)),
                (
                    "state_id",
                    models.CharField(max_length=2, primary_key=True, serialize=False),
                ),
            ],
            options={
                "db_table": "state",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="UserLikesCity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("city", models.CharField(max_length=255)),
                ("state_id", models.CharField(max_length=2)),
            ],
            options={
                "db_table": "user_likes_city",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="UserLikesNeighborhood",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("neighborhood_id", models.IntegerField()),
            ],
            options={
                "db_table": "user_likes_neighborhood",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="UserLikesState",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "user_likes_state",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="UserLikesZipcode",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("zip_code", models.IntegerField()),
            ],
            options={
                "db_table": "user_likes_zipcode",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="ZipCountyCode",
            fields=[
                ("code", models.IntegerField(primary_key=True, serialize=False)),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                ("county", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "zip_county_code",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "income",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=15, null=True
                    ),
                ),
                (
                    "preferred_city",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="dwello.city",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "user_profile",
            },
        ),
    ]
