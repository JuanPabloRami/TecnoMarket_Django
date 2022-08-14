# validadores personalizados
from django.forms import ValidationError

class MaxFileSizeValidator:
    def __init__(self,max_file_Size=5):
        self.max_file_Size = max_file_Size

    def __call__(self,value):
        size = value.size
        max_size = self.max_file_Size * 1048576

        if size > max_size:
            raise ValidationError(f"Solo puedes subir archivos hasta {self.max_file_Size} mb.")
        
        return value