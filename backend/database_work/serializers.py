from .exceptions import *



class BaseSerializer():
    def __init__(self, values: list) -> None:
        self.is_valid = True
        self.error_data = {'error': False}
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
                raise IncorrectTypes(f'Incompatible types of "{el[2]}": {type(el[0])} and {el[1]}')
                break
        

class UserSerializer(BaseSerializer):
    def __init__(self, login, password) -> None:
        try:
            super().__init__([[login, str, 'login'], [password, str, 'password']])

            if self.is_valid:
                self.check_format(login, password)
        except EmptyValue:
            self.error_data['type'] = 'EmptyValue'
            self.error_data['message'] = 'Values must not be empty'
        except IncorrectTypes as error:
            self.error_data['type'] = 'IncorrectTypes'
            self.error_data['message'] = error.error_message
        except IncorrectFormat as error:
            self.error_data['type'] = 'IncorrectFormat'
            self.error_data['message'] = error.error_message


    def check_format(self, login, password):
        if len(login) >= 20:
            self.is_valid = False
            raise IncorrectFormat('Length of "login" must be shorter then 20')
            
        if len(password) <= 8:
            self.is_valid = False
            raise IncorrectFormat('Length of "password" must be longer then 8')
            return
        
class PhotoSerializer(BaseSerializer):
    def __init__(self, path) -> None:
        try:
            super().__init__([[path, str, 'photo_path']])

            if self.is_valid:
                self.check_format(path)
        except EmptyValue:
            self.error_data['type'] = 'EmptyValue'
            self.error_data['message'] = 'Values must not be empty'
        except IncorrectTypes as error:
            self.error_data['type'] = 'IncorrectTypes'
            self.error_data['message'] = error.error_message
        except IncorrectFormat as error:
            self.error_data['type'] = 'IncorrectFormat'
            self.error_data['message'] = error.error_message

    def check_format(self, path): # Нужно прописать уже когда будем с фото работать
        if len(path) <= 8 or len(path) > 60:
            self.is_valid = False
            raise IncorrectFormat('Length of "photo_path" must be shorter then 60 and longer then 8')
            
      
            
        
# class MessageSerializer


# class MessageSerializer(BaseSerializer):




# print(user.is_valid)