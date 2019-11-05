class FieldWithMeta:
    def __init__(self, **kwargs):
        if 'meta' in kwargs:
            self._meta = kwargs['meta']
            del kwargs["meta"]
        super(self.__class__, self).__init__(**kwargs)

    def get_meta(self):
        return self._meta
