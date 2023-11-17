# waf/rate_limit_rules.py
from datetime import datetime, timedelta
from flask import request
import redis
import logging

logging.basicConfig(level=logging.DEBUG)


def check_custom_rate_limit(request, redis_client):
    client_ip = request.remote_addr
    request_path = request.path

    rate_limits = {
        "/public": {"limit": 2, "window": 60 * 60 * 24},
    }

    logging.debug(f"Debug: path: {request_path} and ip: {client_ip}")
    key = f"rate_limit:{client_ip}:{request_path}"
    logging.debug(f"Checking key: {key}")

    current_time = datetime.utcnow()
    window_start_time = current_time - timedelta(
        seconds=rate_limits[request_path]["window"]
    )

    requests = redis_client.zrangebyscore(
        key, window_start_time.timestamp(), current_time.timestamp(), withscores=True
    )

    all_entries = redis_client.zrange(key, 0, -1, withscores=True)

    logging.debug(f"All entries in Redis: {all_entries}")
    logging.debug(f"Key: {key}")

    total_requests = sum(int(count) for _, count in all_entries)

    logging.debug(f"Total Requests: {total_requests}")

    if total_requests >= rate_limits[request_path]["limit"]:
        logging.debug("Rate limit exceeded!")
        return True

    redis_client.zadd(key, {current_time.timestamp(): 1})
    logging.debug("Request within limit. Adding to Redis.")
    return False
