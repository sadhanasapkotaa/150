from rest_framework.routers import DefaultRouter

from .views import (
    CommentByPostViewset,
    CommentByUserViewset,
    PostByUserViewSet,
    PostViewSet,
    UserViewSet,
)

router = DefaultRouter()

router.register(r"users", UserViewSet)
router.register(r"posts", PostViewSet)
router.register(r"post-by-user", PostByUserViewSet)
router.register(r"comment-by-post", CommentByPostViewset)
router.register(r"comment-by-user", CommentByUserViewset)

urlpatterns = router.urls
