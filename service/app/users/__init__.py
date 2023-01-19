from ..common.service import Service
from .users_models import UserModel


class UsersService(Service):

    __model__ = UserModel

    def get_all(self):
        return self.__model__.query.all()
