# waf/security_rules.py
from flask import request
import logging

logging.basicConfig(level=logging.DEBUG)


def xss_rule(request):
    return (
        "<script>" in request.user_agent.string
        or "<script>" in request.path
        or "%3Cscript%3E" in request.query_string.decode("utf-8")
        or any("<script>" in value for value in request.headers.values())
        or (
            request.method == "POST"
            and any("<script>" in value for value in request.form.values())
        )
    )


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
    if (
        "../" in request.path
        or "/../" in request.path
        or "../" in request.query_string.decode("utf-8")
        or "/../" in request.query_string.decode("utf-8")
    ):
        return True
    return False
