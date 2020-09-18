from django.db import migrations, models
import django.db.models.deletion
import datetime
import math
import calendar


def add_months(start_date, month_increase):
    month = ((start_date.month - 1 + month_increase) % 12) + 1
    year = start_date.year + math.floor((start_date.month - 1 + month_increase) / 12)
    return datetime.datetime(year, month, 1)


def get_end_date(start_date):
    return start_date.replace(
        day=calendar.monthrange(
            start_date.year,
            start_date.month)[1],
        hour=23, minute=59, second=59)


def create_partitions(apps, schema_editor):
    start_date = datetime.datetime(2020, 1, 1)
    numbers_of_partition = 15

    table_name = "activities_apiaccess"
    partitions_creation_sql = ""
    for i in range(numbers_of_partition):
        partition_start_date = add_months(start_date, i)
        partition_end_date = get_end_date(partition_start_date)

        partition_table_name = f"{table_name}_y{partition_start_date.year}m{partition_start_date.month}"

        partitions_creation_sql = partitions_creation_sql + (
            f"""CREATE TABLE {partition_table_name} PARTITION OF {table_name}
                FOR VALUES FROM ('{partition_start_date.strftime("%Y-%m-%dT%H:%M:%S")}') 
                    TO ('{partition_end_date.strftime("%Y-%m-%dT%H:%M:%S")}');
            """
        )

        partitions_creation_sql = partitions_creation_sql + (
            f"CREATE INDEX ON {partition_table_name} (created_at);"
        )

    partitions_creation_sql = partitions_creation_sql + (
        f"CREATE TABLE {table_name}_default PARTITION OF {table_name} DEFAULT;"
    )

    schema_editor.execute(partitions_creation_sql)


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('users', '0003_auto_20200729_1431'),
    ]

    operations = [
        migrations.RunSQL(
            """CREATE TABLE "activities_apiaccess" (
                "id" serial NOT NULL, 
                "api_name" varchar(50) NOT NULL, 
                "status_code" smallint NOT NULL CHECK ("status_code" >= 0), 
                "response_time" integer NOT NULL CHECK ("response_time" >= 0), 
                "created_at" timestamp with time zone NOT NULL, 
                "updated_at" timestamp with time zone NOT NULL, 
                "user_id" integer NOT NULL,
                PRIMARY KEY ("id", "created_at")
            ) PARTITION BY RANGE (created_at);"""
        ),
        migrations.RunSQL(
            """ALTER TABLE "activities_apiaccess" 
                ADD CONSTRAINT "activities_apiaccess_user_id_9b306f34_fk_users_user_id" 
                    FOREIGN KEY ("user_id") 
                    REFERENCES "users_user" ("id") 
                    DEFERRABLE INITIALLY DEFERRED;
            """
        ),
        migrations.RunPython(create_partitions)
    ]
