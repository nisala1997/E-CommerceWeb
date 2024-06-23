from django.db import migrations, models
from django.utils import timezone  # Updated import

class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20210119_1500'),  # Replace with your actual dependency
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(default=timezone.now),  # Example usage of timezone.now()
        ),
    ]
