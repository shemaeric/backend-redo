from django.db.models import QuerySet, Q, Sum

class CustomQuerySet(QuerySet):

    def _active(self):
        """Return only objects that haven't been soft deleted."""
        return self.filter(is_deleted=False)

    def all_objects(self):
        """Return all objects that haven't been soft deleted"""
        return self._active()
