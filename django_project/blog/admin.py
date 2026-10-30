from django.contrib import admin
from blog.models import Post   # Render posts from the database in the home view

admin.site.register(Post)