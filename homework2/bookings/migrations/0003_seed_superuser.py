from django.db import migrations

# creates a admin login automatically
def seed_superuser(apps, schema_editor):
    from django.contrib.auth.models import User
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            password='admin123!',
            email=''
        )

class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_seed_movies'),
    ]

    operations = [
        migrations.RunPython(seed_superuser),
    ]