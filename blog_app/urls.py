from django.urls import path
from .views import (HomeView,PostDetailView,AddPostView,UpdatePostView,DeletePostView,
                    CategoryView,LikePostView,UnlikePostView,LikeListView,UnlikeListView,
                    CreateCommentView,
                    )


urlpatterns = [
    path('',   HomeView.as_view()   , name = 'home'  ),
    path('article/<int:pk>', PostDetailView.as_view() , name='post_detail' ),
    path( 'article/new', AddPostView.as_view(), name='add_post'),
    path('article/<int:pk>/edit', UpdatePostView.as_view(), name='update_post'),
    path( 'article/<int:pk>/delete', DeletePostView.as_view() , name = 'delete_post'  ),
    path('category/<str:categ>' , CategoryView.as_view() , name='category'),
    path('article/<int:pk>/like', LikePostView  , name='like_post'),
    path('article/<int:pk>/unlike', UnlikePostView  , name='unlike_post'),
    path('article/<int:pk>/like/list',  LikeListView.as_view() , name='like_list'),
    path('article/<int:pk>/unlike/list',  UnlikeListView.as_view() , name='unlike_list'),
    path('article/<int:pk>/comment' , CreateCommentView , name = 'create_comment'  ),

]




