# waf/rate_limit_rules.py
from datetime import datetime, timedelta
from flask import request


def check_rate_limit(request):
    client_ip = request.remote_addr
    current_time = datetime.now()

    if "rate_limit_requests" not in request.headers.environ:
        request.headers.environ["rate_limit_requests"] = {}

    requests = request.headers.environ["rate_limit_requests"]

    if client_ip not in requests:
        requests[client_ip] = [(current_time, 1)]
        return False

    requests[client_ip] = [
        (time, count)
        for time, count in requests[client_ip]
        if current_time - time <= timedelta(hours=1)
    ]

    if sum(count for _, count in requests[client_ip]) >= 5:
        return True

    requests[client_ip].append((current_time, 1))
    return False
