class AppValidationError(Exception):
    def __init__(self, message, field, error_code=400):
        super().__init__(message)
        self.field = field
        self.error_code = error_code

def validate_age(age):
    if not isinstance(age, int):
        raise AppValidationError("Age must be an integer", field="age", error_code=422)
    if age < 18:
        raise AppValidationError("User must be 18 or older", field="age", error_code=400)

try:
    validate_age(15)
except AppValidationError as e:
    print(f"Status Code: {e.error_code}")
    print(f"Invalid Field: {e.field}")
    print(f"Error Message: {e}")