# waf.py
class Rule:
    def __init__(self, name, pattern):
        self.name = name
        self.pattern = pattern

    def matches(self, request):
        return self.pattern in request

class RateLimit:
    def __init__(self, limit):
        self.limit = limit
