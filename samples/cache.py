from time import sleep
from django.core.cache import cache
from blog.models import Post
post_pk = 1
p = Post.objects.get(pk=1)
cache.set(f"post_{post_pk}", p, 30)
p1 = cache.get(f"post_{post_pk}")
print(p == p1)
# True
sleep(30)
print(cache.get(f"post_{post_pk}"))
# None - cache is expired.
cache.delete(f"post_{post_pk}")

