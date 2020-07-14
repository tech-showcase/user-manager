from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            "ALTER TABLE users_user ALTER COLUMN created_at SET DEFAULT now();" +
            "ALTER TABLE users_user ALTER COLUMN updated_at SET DEFAULT now();" +
            "ALTER TABLE users_info ALTER COLUMN created_at SET DEFAULT now();" +
            "ALTER TABLE users_info ALTER COLUMN updated_at SET DEFAULT now();" +
            "ALTER TABLE users_role ALTER COLUMN created_at SET DEFAULT now();" +
            "ALTER TABLE users_role ALTER COLUMN updated_at SET DEFAULT now();" +
            "ALTER TABLE users_accessright ALTER COLUMN created_at SET DEFAULT now();" +
            "ALTER TABLE users_accessright ALTER COLUMN updated_at SET DEFAULT now();" +
            "ALTER TABLE users_service ALTER COLUMN created_at SET DEFAULT now();" +
            "ALTER TABLE users_service ALTER COLUMN updated_at SET DEFAULT now();"
        )
    ]
