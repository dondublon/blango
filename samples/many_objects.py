from django.core.cache import cache
from blog.models import Post

all_posts = Post.objects.all()

posts_to_cache = {f"post_{post.pk}": post for post in all_posts}
print(posts_to_cache)
# {'post_7': <Post: Leo: A Personal Profile>, 'post_6': <Post: Django vs Python>, 'post_5': <Post: Breaking News>, 'post_4': <Post: A Real Post>, 'post_3': <Post: Yet another test post!>, 'post_1': <Post: An Example Post>, 'post_2': <Post: Advanced Django: A Review>}

print(cache.set_many(posts_to_cache, 30))  # Pass dictionary
# []

# How to get many:
# cache.get_many(["post_1", "post_2", "post_1000"])
# we get a dictionary.
 # + delete_many