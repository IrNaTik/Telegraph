from .exceptions import *



class BaseSerializer():
    def __init__(self, values: list) -> None:
        self.is_valid = True
        self.values = values
        self._check_emptity()

        if self.is_valid:
            self._check_types()

    def _check_emptity(self):
        self.is_valid = True
        for el in self.values:
            if not el[0]:
                self.is_valid = False
                raise EmptyValue

    def _check_types(self):
        for el in self.values:
            if type(el[0]) != el[1]:
                self.is_valid = False
                break
        


class UserSerializer(BaseSerializer):
    def __init__(self, login, password) -> None:
        super().__init__([[login, str], [password, str]])

        if self.is_valid:
            self.check_format(login, password)

    def check_format(self, login, password):
        if len(login) >= 20:
            self.is_valid = False
            return

        if len(password) <= 8:
            self.is_valid = False
            return
        
class MessageSerializer


# class MessageSerializer(BaseSerializer):

try:
    user = UserSerializer('', 'jjsadasfdslj')
except EmptyValue:
    print('empty')


# print(user.is_valid)