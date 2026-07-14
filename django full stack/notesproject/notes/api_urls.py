from rest_framework.routers import DefaultRouter

from .api_views import NoteViewSet


router = DefaultRouter()
router.register("notes", NoteViewSet, basename="note-api")

urlpatterns = router.urls
