from django.core.cache import cache
sentinel = object()

cache.set("current_user", None, 30)

u = cache.get("current_user", sentinel)

print(u is None)
# True

print(u is sentinel)
#False