from django.urls import path

from . import views

urlpatterns = [
    path(
        'studies/',
        views.StudyListView.as_view(),
        name='studies',
    ),
    path(
        'studies/new/',
        views.StudyCreateView.as_view(),
        name='study_create',
    ),
    path(
        'studies/<int:pk>/',
        views.StudyDetailView.as_view(),
        name='study_detail',
    ),
    path(
        'studies/<int:pk>/edit/',
        views.StudyUpdateView.as_view(),
        name='study_update',
    ),
    path(
        'studies/<int:pk>/delete/',
        views.StudyDeleteView.as_view(),
        name='study_delete',
    ),
    path(
        'subjects/',
        views.SubjectListView.as_view(),
        name='subject_list',
    ),
    path(
        'subjects/new/',
        views.SubjectCreateView.as_view(),
        name='subject_create',
    ),
    path(
        'subjects/<int:pk>/',
        views.SubjectDetailView.as_view(),
        name='subject_detail',
    ),
    path(
        'subjects/<int:pk>/edit/',
        views.SubjectUpdateView.as_view(),
        name='subject_update',
    ),
    path(
        'subjects/<int:pk>/delete/',
        views.SubjectDeleteView.as_view(),
        name='subject_delete',
    ),
]
