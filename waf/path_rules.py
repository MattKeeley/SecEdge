# waf/path_rules.py
def block_example_path(request):
    if request.path == "/example":
        return True
    return False 


def block_admin_path(request):
    if request.path == "/admin":
        return True 
    return False 

