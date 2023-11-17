# waf/path_rules.py
def block_example_path(request):
    if request.path == "/example":
        return True  # Block the request
    return False  # Allow the request


def block_admin_path(request):
    if request.path == "/admin":
        return True  # Block the request
    return False  # Allow the request


def block_yeet_path(request):
    if request.path == "/yeet":
        return True  # Block the request
    return False  # Allow the request
