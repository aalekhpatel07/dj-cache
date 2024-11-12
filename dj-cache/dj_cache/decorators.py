import functools
from .models import Cache


def cached(ttl_seconds: int = None):
    def inner(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return Cache.get_or_set(func, ttl=ttl_seconds, *args, **kwargs)
        return wrapper
    return inner
