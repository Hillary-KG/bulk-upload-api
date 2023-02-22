from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework as filters
from django.core.files.storage import default_storage


from .models import UserRecord
from .serializers import UserRecordSerializer, UploadSerializer
from .tasks import upload_records


# Create your views here.
class UploadViewSet(ViewSet):
    """
    API view definition for file upload and processing
    """

    serializer_class = UploadSerializer

    def create(self, request, *args, **kwargs):
        """
        validate, upload and process a file
        : return Response object
        """
        try:
            file_obj = request.FILES["file"]
            file_name = default_storage.save(file_obj.name, file_obj)
            # push task to queue
            upload_records.delay(default_storage.path(file_name))
            return Response(
                {"success": True, "msg": "upload successful"},
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response(
                {"success": False, "msg": f"Request Failed. An exception occured: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class UserRecordFilter(filters.FilterSet):
    """
    - Handle special filter e.g field range (dob)
    """

    birth_date = filters.DateFromToRangeFilter()

    class Meta:
        model = UserRecord
        fields = ["first_name", "last_name", "birth_date", "phone_number", "email"]


class UserRecordView(ModelViewSet):
    """
    list user records
    :filter by - first_name,
                last_name ,
                birth date range (dob),
                phone_number, email.
    """

    queryset = UserRecord.objects.all()
    serializer_class = UserRecordSerializer
    filter_backends = [
        filters.DjangoFilterBackend,
        # filters.SearchFilter
    ]
    ordering_fields = "__all__"

    filterset_class = UserRecordFilter

    search_fields = ["first_name", "last_name", "birth_date", "phone_number", "email"]
