# waf/rules.py
from waf.security_rules import xss_rule, sql_injection_rule, path_traversal_rule
from waf.path_rules import block_example_path, block_admin_path, block_yeet_path
from waf.rate_limit_rules import check_custom_rate_limit
import redis

redis_client = redis.StrictRedis(host="redis", port=6379, db=0)


def check_all_rules(request):
    if xss_rule(request) or sql_injection_rule(request) or path_traversal_rule(request):
        return 406  # HTTP 406 - Not Acceptable
    if (
        block_example_path(request)
        or block_admin_path(request)
        or block_yeet_path(request)
    ):
        return 403  # HTTP 403 - Forbidden
    if check_custom_rate_limit(request, redis_client):
        return 429  # Custom rate limit exceeded
    return None  # None (No rules violated)
