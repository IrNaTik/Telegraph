# # move to a separate module
# #exmpl: https://github.com/encode/django-rest-framework/blob/19655edbf782aa1fbdd7f8cd56ff9e0b7786ad3c/rest_framework/exceptions.py#L140
class HandlerStatusError(Exception): 
    def __init__(self, *args: object) -> None:
        if args:
            self.status = args[0]

    def __str__(self) -> str:
        if self.status:
            return f'{self.status}'
    