from .db import db


class Service:

    __model__ = None

    def _isinstance(self, model):
        if not isinstance(model, self.__model__):
            raise ValueError(f'{model} not of type {self.__model__}')
        return True

    def create(self, **kwargs):
        return self.save(self.new(**kwargs))

    def delete(self, model):
        self._isinstance(model)
        db.session.delete(model)
        db.session.commit()

    def get(self, id):
        return self.__model__.query.get(id)

    def get_all(self):
        return self.__model__.query.all()

    def new(self, **kwargs):
        return self.__model__(**kwargs)

    def save(self, model):
        self._isinstance(model)
        db.session.add(model)
        db.session.commit()
        return model

    def update(self, model, **kwargs):
        self._isinstance(model)
        for k, v in kwargs.items():
            setattr(model, k, v)
        db.session.commit()
        return model
