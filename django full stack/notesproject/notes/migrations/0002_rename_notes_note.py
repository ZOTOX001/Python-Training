# Rename the model without losing the notes already stored in the database.
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="notes",
            new_name="Note",
        ),
    ]
