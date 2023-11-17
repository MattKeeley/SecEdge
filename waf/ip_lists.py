# waf/ip_lists.py
import os


def load_ip_list(file_path):
    with open(file_path, "r") as file:
        return set(file.read().splitlines())


allow_list = load_ip_list("waf/lists/allow_list.txt")
deny_list = load_ip_list("waf/lists/deny_list.txt")
