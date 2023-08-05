from django.urls import path, include
from watchlist_app.api.views import (
    WatchListAV, WatchListDetailAV, ReviewList, ReviewDetail, ReviewCreate, StreamPlatformVS, WatchListGV
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')
urlpatterns = [
    # path("stream/", StreamPlatformAV.as_view(), name='stream-list'),
    # path("stream/<int:pk>", StreamPlatformDetailAV.as_view(),
    #  name='streamplatform-detail'),
    path('', include(router.urls)),

    path("<int:pk>/reviews/", ReviewList.as_view(),
         name='review-list'),
    path("<int:pk>/review-create/", ReviewCreate.as_view(),
         name='review-create'),
    path("review/<int:pk>/", ReviewDetail.as_view(), name='review-detail'),
    # path("review/", ReviewList.as_view(),
    #      name='review-list'),
    # path("review/<int:pk>", ReviewDetail.as_view(), name='review-detail'),


    path("list2/", WatchListGV.as_view(), name='watch_list'),
    path("list/", WatchListAV.as_view(), name='watch_list'),
    path("<int:pk>/", WatchListDetailAV.as_view(), name='watch_details'),
]
