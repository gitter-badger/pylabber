import django_filters

# from django_smb.models import RemoteLocation  # , RemoteFile
from research.models import Subject


class SubjectListFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(label="#")
    first_name = django_filters.CharFilter(label="First Name", lookup_expr="icontains")
    last_name = django_filters.CharFilter(label="Last Name", lookup_expr="icontains")
    id_number = django_filters.CharFilter(label="ID Number", lookup_expr="icontains")
    date_of_birth = django_filters.NumberFilter(
        field_name="date_of_birth", label="Date of Birth"
    )

    date_of_birth__gt = django_filters.NumberFilter(
        field_name="date_of_birth", lookup_expr="year__gt", label="After"
    )
    date_of_birth__lt = django_filters.NumberFilter(
        field_name="date_of_birth", lookup_expr="year__lt", label="Before"
    )

    class Meta:
        model = Subject
        fields = [
            "id",
            "first_name",
            "last_name",
            "sex",
            "gender",
            "date_of_birth",
            "id_number",
        ]


# class SMBFileListFilter(django_filters.FilterSet):
#     id = django_filters.NumberFilter(label='#')
#     path = django_filters.CharFilter(
#         label='Path',
#         lookup_expr='icontains',
#     )
#     source = django_filters.ModelMultipleChoiceFilter(
#         label='Data Source',
#         queryset=RemoteLocation.objects.all(),
#     )
#     is_archived = django_filters.BooleanFilter(label='Archived')

#     class Meta:
#         model = RemoteFile
#         fields = [
#             'id',
#             'path',
#             'source',
#             'is_archived',
#         ]
