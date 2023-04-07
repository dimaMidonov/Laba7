def cast(to_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return to_type(result)
            except (ValueError, TypeError):
                return result
        return wrapper
    return decorator
@cast(int)
def get_integer():
    return "123"

@cast(float)
def get_float():
    return "3.14"

@cast(str)
def get_string():
    return 42

print(get_integer())  # 123 (int)
print(get_float())  # 3.14 (float)
print(get_string())  # "42" (str)