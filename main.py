# main.py
from flask import Flask, request, abort
from waf.rules import check_all_rules
from waf.ip_lists import load_ip_list, allow_list, deny_list

app = Flask(__name__)


# WAF middleware
@app.before_request
def waf_middleware():
    client_ip = request.remote_addr

    # Check IP against deny list
    if client_ip in deny_list:
        abort(406)  # Block the request directly

    # Check IP against allow list
    if client_ip in allow_list:
        return  # Allow the request, skip further rules

    # Check agains security_rules, path_rules, and rate_limit_rules.
    rule_error_code = check_all_rules(request)

    if rule_error_code is not None:
        abort(rule_error_code)  # Abort with the specified HTTP status code
    else:
        return  # Continue processing the request with a 200 OK response


# Your main route
@app.route("/")
def index():
    return f"Hello, {request.remote_addr}!"


# Your main route
@app.route("/public")
def public():
    return f"Hello, {request.remote_addr}! Welcome to Public Route"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
