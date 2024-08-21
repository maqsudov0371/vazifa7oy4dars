from django.urls import path
from .views import HomePageView, RegisterView, LoginView, CourseDetailView, AddCourseView, AddCategoryView, AddTagView, UpdateTagView, Tags, DeleteTagView
 

app_name = 'main'

urlpatterns = [
    path('', HomePageView.as_view(), name="home" ),
    path('register', RegisterView.as_view(), name="register" ),
    path('login', LoginView.as_view(), name="kirish" ),
    path('course/<str:slug>', CourseDetailView.as_view(), name="detail" ),
    path('add_course', AddCourseView.as_view(), name="course" ),
    path('add_category', AddCategoryView.as_view(), name="category" ), 
    path('add_tags', AddTagView.as_view(), name="tags" ), 
    path('tags', Tags.as_view(), name="tags" ), 
    path('update_tags/<int:pk>/update/', UpdateTagView.as_view(), name="updatetags" ), 
    path('delete_tag/<int:pk>/delete/', DeleteTagView.as_view(), name='deletetag'),
]
