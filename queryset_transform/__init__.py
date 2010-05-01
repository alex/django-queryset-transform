from django.db import models


class TransformQuerySet(models.query.QuerySet):
    def __init__(self, *args, **kwargs):
        super(TransformQuerySet, self).__init__(*args, **kwargs)
        self._transform_fns = []

    def _clone(self, klass=None, setup=False, **kw):
        c = super(TransformQuerySet, self)._clone(klass, setup, **kw)
        c._transform_fns = self._transform_fns[:]
        return c

    def transform(self, fn):
        c = self._clone()
        c._transform_fns.append(fn)
        return c

    def iterator(self):
        for item in super(TransformQuerySet, self).iterator()
            for func in self._transform_fns:
                func(item)
            yield item

class TransformManager(models.Manager):
    def get_query_set(self):
        return TransformQuerySet(self.model)
