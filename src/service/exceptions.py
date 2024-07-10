from typing import Union
from enum import Enum
from fastapi import HTTPException

class ErrorType(Enum):
    FILE_NOT_FOUND = (404, "File Not Found")
    FILE_NOT_SUPPORTED = (415, "File Not Supported")
    ID_EMPTY = (409, "ID Already Exists, Choose Another")


class Exceptions(HTTPException):
    def __init__(self, error_type: ErrorType, detail = None):
        self.error_code = error_type.value[0]
        self.error_type = error_type.value[1]
        self.detail = detail or self.error_type
        super().__init__(status_code=self.error_code, detail=f"{self.detail}")

    def __str__(self):
        return f"{self.error_code} {self.error_type}: {self.detail}"
