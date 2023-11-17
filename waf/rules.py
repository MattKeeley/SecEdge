# waf/rules.py
from waf.security_rules import xss_rule, sql_injection_rule, path_traversal_rule
from waf.path_rules import block_example_path, block_admin_path, block_yeet_path
from waf.rate_limit_rules import check_rate_limit


def check_all_rules(request):
    if xss_rule(request) or sql_injection_rule(request) or path_traversal_rule(request):
        return 406  # HTTP 406 - Not Acceptable
    if (
        block_example_path(request)
        or block_admin_path(request)
        or block_yeet_path(request)
    ):
        return 403  # HTTP 403 - Forbidden
    if check_rate_limit(request):
        return 429  # HTTP 429 - Too Many Requests
    return 200  # HTTP 200 - OK (No rules violated)
