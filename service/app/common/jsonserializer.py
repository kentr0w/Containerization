class JsonSerializer:

    __json_public__ = None
    __json_hidden__ = None
    __json_modifiers__ = None

    def to_json(self):
        public = self.__json_public__ or []
        hidden = self.__json_hidden__ or []
        modifiers = self.__json_modifiers__ or dict()
        serialized = dict()

        for key in public:
            serialized[key] = getattr(self, key)

        for key, modifier in modifiers.items():
            value = getattr(self, key)
            serialized[key] = modifier(value, self)

        for key in hidden:
            serialized.pop(key, None)

        return serialized
