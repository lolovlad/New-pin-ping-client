from threading import Lock


class Singleton(type):

    _instans = None
    _lock = Lock()

    def __call__(self, *args, **kwargs):
        with self._lock:
            if not self._instans:
                self._instans = super().__call__(*args, **kwargs)
        return self._instans