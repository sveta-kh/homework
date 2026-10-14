#Access Control / Password Required Decorator 

def require_role(allowed_role = "admin"):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role == allowed_role:
                result = func(user_role, *args, **kwargs)
                return result
            else:
                print("Permission Denied: User is not an admin.")
        return wrapper
    return decorator

@require_role()
def access_control(user_role):
    print("Welcome")

access_control("admin")
access_control("guest")

     


