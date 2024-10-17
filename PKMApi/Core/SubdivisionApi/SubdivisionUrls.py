from django.urls import path

from .Views.SubdivisionListCreateView import SubdivisionListCreateApiView
from .Views.SubdivisionRetrieveUpdateDestroyView import SubdivisionRetrieveUpdateDestroyApiView

urlpatterns=[
    path('', SubdivisionListCreateApiView.as_view()),
    path('detail/<int:pk>/', SubdivisionRetrieveUpdateDestroyApiView.as_view()),
]