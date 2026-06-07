from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable[..., Callable[..., Any]]:
    def wrapper(func: Callable[..., Any]) -> Callable[..., Callable[..., Any]]:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            func_name = func.__name__
            try:

                result = func(*args, **kwargs)

                message = f"{func_name}: Ok"
                if filename is not None:
                    with open(filename, "a") as file:
                        file.write(f"{message}\n")
                else:
                    print(message)
                return result
            except Exception as e:
                error_message = f"{func_name}: Error : {e}\nInputs: args={args}, kwargs={kwargs}"
                if filename is not None:
                    with open(filename, "a") as file:
                        file.write(f"{error_message}\n")
                else:
                    print(error_message)
                raise e

        return inner

    return wrapper
