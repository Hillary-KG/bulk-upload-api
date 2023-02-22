import dask.dataframe as dd
from django.core.management import BaseCommand
from django.utils import timezone
from django.db import IntegrityError
from django.core.files.storage import default_storage


from api.models import UserRecord, FileObject


class Command(BaseCommand):
    help = "Loads products and product categories from CSV file."

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        status = 0
        offset = 0
        no_of_objects = 0
        try:
            start_time = timezone.now()
            file_path = options["file_path"]
            reader = dd.read_csv(file_path, header=0)
            data = [row for _, row in reader.iterrows()]
            user_records = map(lambda record: UserRecord(**record), data)
            if user_records:
                created_objects = UserRecord.objects.bulk_create(
                    user_records, ignore_conflicts=True
                )
            if created_objects:
                no_of_objects = len(created_objects)
                self.stdout.write(
                    self.style.SUCCESS(
                        f"\nCreated {no_of_objects} Objects.\
                        \nProcessing time: \
                        {(timezone.now()-start_time).total_seconds()} seconds."
                    )
                )
                offset = no_of_objects
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"\nNo objects to becreated!\
                            \nProcessing time:\
                             {(timezone.now()-start_time).total_seconds()} seconds."
                    )
                )
            status = 1
        except IntegrityError:
            pass
            self.stdout.write(
                self.style.ERROR(
                    f"\nUpload Failed! Duplicates found.\
                        \nProcessing time: \
                        {(timezone.now()-start_time).total_seconds()} seconds."
                )
            )
            offset = no_of_objects - 1
            status = 1
        finally:
            # create file object
            file_object = FileObject(
                source=file_path,
                status=status,
                offset=offset,
                created_at=timezone.now(),
            )
            file_object.save()
            # delete file
            default_storage.delete(file_path)
