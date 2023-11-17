# waf/security_rules.py
from flask import request


def xss_rule(request):
    if (
        "<script>" in request.user_agent.string
        or "<script>" in request.path
        or "<script>" in request.query_string.decode("utf-8")
    ):
        return True
    return False


def sql_injection_rule(request):
    sql_keywords = [
        "SELECT",
        "INSERT",
        "UPDATE",
        "DELETE",
        "DROP",
        "UNION",
        "OR",
        "AND",
    ]
    for keyword in sql_keywords:
        if keyword in request.path or keyword in request.query_string.decode("utf-8"):
            return True
    return False


def path_traversal_rule(request):
    if "../" in request.path or "/../" in request.path:
        return True
    return False
