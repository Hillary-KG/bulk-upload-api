from pathlib import Path
from django.core.management import call_command
from django.core.files.storage import default_storage
from django.utils import timezone

from celery import shared_task


@shared_task
def upload_records(file):
    """
    async task to read and upload data from csv
    """
    filename = Path(file).name
    print(
        f"----------- Start uploading\
        {filename} at {timezone.now()} ----------"
    )
    try:
        call_command("load_data", default_storage.path(file))
    except Exception as e:
        print(
            f"----------- Fail uploading\
            {filename} at {timezone.now()}. Exception: {e}"
        )
    print(
        f"----------- End uploading\
         {filename} at {timezone.now()} ----------"
    )

    return
