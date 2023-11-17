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

    rule_error_code = check_all_rules(request)
    if rule_error_code != 200:
        abort(rule_error_code)


# Your main route
@app.route("/")
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
